// Builds hand drawn pencil style SVG diagrams from small specs in <book>/diagrams/*.json
// Usage: node diagrams.js ../vol2
const fs = require('fs');
const path = require('path');
const rough = require('roughjs/bundled/rough.cjs.js');

const GRAPHITE = '#3A3A3A', SOFT = '#8C8C8C', ORANGE = '#F26A1B', YELLOW = '#F2C200';
const gen = rough.generator();
let seed = 7;
const opt = o => Object.assign({ roughness: 1.5, bowing: 1.1, stroke: GRAPHITE, strokeWidth: 1.4, seed: seed++ }, o);

function paths(drawable) {
  return gen.toPaths(drawable).map(p =>
    `<path d="${p.d}" stroke="${p.stroke}" stroke-width="${p.strokeWidth}" fill="${p.fill || 'none'}" stroke-linecap="round" stroke-linejoin="round"/>`).join('');
}
const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');

function text(x, y, str, o = {}) {
  const size = o.size || 15, weight = o.weight || 400, fill = o.fill || GRAPHITE, anchor = o.anchor || 'start';
  return `<text x="${x}" y="${y}" font-size="${size}" font-weight="${weight}" fill="${fill}" text-anchor="${anchor}"${o.halo ? ' stroke="#fff" stroke-width="6" stroke-linejoin="round" paint-order="stroke"' : ''}>${esc(str)}</text>`;
}

function box(b) {
  let out = '';
  const fillKind = b.fill; // undefined, 'shade', 'orange', 'yellow'
  const o = opt({ strokeWidth: b.group ? 1.1 : 1.4, stroke: b.dashed ? SOFT : GRAPHITE });
  if (b.dashed) o.strokeLineDash = [7, 6];
  if (fillKind === 'shade') Object.assign(o, { fill: '#9A9A9A', fillStyle: 'hachure', hachureAngle: -41, hachureGap: 7, fillWeight: 0.6 });
  if (fillKind === 'orange') Object.assign(o, { fill: ORANGE, fillStyle: 'hachure', hachureAngle: -41, hachureGap: 6, fillWeight: 0.9 });
  if (fillKind === 'yellow') Object.assign(o, { fill: YELLOW, fillStyle: 'hachure', hachureAngle: -41, hachureGap: 6, fillWeight: 0.9 });
  if (!b.group) out += `<rect x="${b.x}" y="${b.y}" width="${b.w}" height="${b.h}" fill="#fff"/>`;
  if (fillKind) {
    // shading pass at low opacity so it reads as pencil, then a clean outline
    const shade = gen.rectangle(b.x, b.y, b.w, b.h, Object.assign({}, o, { stroke: 'none' }));
    out += `<g opacity="${fillKind === 'shade' ? 0.35 : 0.55}">${paths(shade)}</g>`;
  }
  if (fillKind && fillKind !== 'shade') {
    const n = (b.title ? 1 : 0) + (b.lines || []).length, th = (b.title ? 28 : 0) + (b.lines || []).length * 25 + 14;
    const ih = Math.min(b.h - 28, th + 2), iy = b.y + (b.h - ih) / 2;
    out += `<rect x="${b.x + 16}" y="${iy}" width="${b.w - 32}" height="${ih}" rx="3" fill="#fff" opacity="0.92"/>`;
  }
  out += paths(gen.rectangle(b.x, b.y, b.w, b.h, Object.assign({}, o, { fill: undefined })));
  const pad = b.group ? 16 : 14;
  let ty = b.y + 32;
  if (b.title) {
    const cx = b.center ? b.x + b.w / 2 : b.x + pad;
    out += text(cx, ty, b.title, { size: 21, weight: 700, anchor: b.center ? 'middle' : 'start', halo: !!fillKind });
    ty += 28;
  }
  (b.lines || []).forEach(l => {
    const cx = b.center ? b.x + b.w / 2 : b.x + pad;
    out += text(cx, ty, l, { size: 18.5, anchor: b.center ? 'middle' : 'start', fill: '#4A4A4A', halo: !!fillKind });
    ty += 25;
  });
  return out;
}

function diamond(d) {
  const pts = [[d.cx, d.cy - d.h / 2], [d.cx + d.w / 2, d.cy], [d.cx, d.cy + d.h / 2], [d.cx - d.w / 2, d.cy]];
  let out = `<polygon points="${pts.map(p => p.join(',')).join(' ')}" fill="#fff"/>`;
  if (d.fill) out += `<g opacity="0.5">${paths(gen.polygon(pts, opt({ stroke: 'none', fill: d.fill === 'orange' ? ORANGE : YELLOW, fillStyle: 'hachure', hachureAngle: -41, hachureGap: 6 })))}</g>`;
  out += paths(gen.polygon(pts, opt({})));
  const n = d.lines.length, lh = 25;
  d.lines.forEach((l, k) => { out += text(d.cx, d.cy + (k - (n - 1) / 2) * lh + 7, l, { size: 18.5, anchor: 'middle' }); });
  return out;
}

function arrow(a) {
  const pts = a.points;
  const o = opt({ strokeWidth: 1.3, stroke: a.dashed ? SOFT : GRAPHITE, roughness: 0.9 });
  if (a.dashed) o.strokeLineDash = [6, 6];
  let out = paths(gen.linearPath(pts, o));
  const [x1, y1] = pts[pts.length - 2], [x2, y2] = pts[pts.length - 1];
  const ang = Math.atan2(y2 - y1, x2 - x1), L = 11, W = 0.45;
  const p1 = [x2 - L * Math.cos(ang - W), y2 - L * Math.sin(ang - W)];
  const p2 = [x2 - L * Math.cos(ang + W), y2 - L * Math.sin(ang + W)];
  out += paths(gen.linearPath([p1, [x2, y2], p2], opt({ strokeWidth: 1.5, stroke: a.dashed ? SOFT : GRAPHITE, roughness: 0.5 })));
  if (a.label) out += text(a.label[0], a.label[1], a.label[2], { size: 18.5, fill: '#4A4A4A', anchor: a.label[3] || 'start' });
  return out;
}

function render(spec) {
  let body = '';
  if (spec.title) body += text(0, 26, spec.title, { size: 25, weight: 700 });
  if (spec.subtitle) body += text(0, 58, spec.subtitle, { size: 18.5, fill: '#5A5A5A' });
  for (const it of spec.items) {
    if (it.type === 'box') body += box(it);
    else if (it.type === 'arrow') body += arrow(it);
    else if (it.type === 'diamond') body += diamond(it);
    else if (it.type === 'line') body += paths(gen.linearPath(it.points, opt({ strokeWidth: 1.3, roughness: 0.9 })));
    else if (it.type === 'text') body += text(it.x, it.y, it.text, it);
  }
  return `<svg class="pencil" viewBox="-6 -6 ${spec.w + 12} ${spec.h + 12}" xmlns="http://www.w3.org/2000/svg" font-family="InterW, Inter, sans-serif">${body}</svg>`;
}

const book = path.resolve(process.argv[2]);
const dir = path.join(book, 'diagrams');
const outDir = path.join(book, 'img');
for (const f of fs.readdirSync(dir).filter(f => f.endsWith('.json'))) {
  seed = 7;
  const spec = JSON.parse(fs.readFileSync(path.join(dir, f), 'utf8'));
  fs.writeFileSync(path.join(outDir, f.replace('.json', '.svg')), render(spec));
  console.log('diagram', f);
}
