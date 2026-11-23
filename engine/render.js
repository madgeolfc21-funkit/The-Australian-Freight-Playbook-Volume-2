// node render.js <output.pdf>
const { chromium } = require('playwright');
const path = require('path');
const OUT = path.resolve(process.argv[2] || 'out.pdf');
(async () => {
  const b = await chromium.launch({ executablePath: '/usr/bin/google-chrome' });
  const p = await b.newPage({ viewport: { width: 794, height: 1123 } });
  p.on('pageerror', e => console.log('ERR', e.message));
  await p.goto('file://' + path.join(__dirname, 'book.html'));
  await p.waitForFunction(() => window.__done === true, null, { timeout: 90000 });
  console.log(JSON.stringify(await p.evaluate(() => window.__report)));
  const issues = await p.evaluate(() => {
    const out = [];
    document.querySelectorAll('.page').forEach((pg, k) => {
      const b = pg.querySelector('.body'); if (!b) return;
      if (b.scrollHeight > b.clientHeight + 1) out.push(['overflow', k + 1]);
      const kids = Array.from(b.children).filter(c => !c.classList.contains('gapslot'));
      const last = kids.pop();
      if (last && (/^H[23]$/.test(last.tagName) || last.classList.contains('leadin'))) out.push(['stranded heading', k + 1, last.textContent.slice(0, 50)]);
    });
    return out;
  });
  console.log('ISSUES', JSON.stringify(issues));
  await p.pdf({ path: OUT, preferCSSPageSize: true, printBackground: true });
  await b.close();
})();
