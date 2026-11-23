import re, html, json, sys, pathlib, markdown

ENGINE = pathlib.Path(__file__).resolve().parent
BOOK = pathlib.Path(sys.argv[1]).resolve()
ONLY = sys.argv[2].split(',') if len(sys.argv) > 2 else None
CFG = json.loads((BOOK / 'book.json').read_text())
PARTS = CFG['parts']
MONTHS = 'January February March April May June July August September October November December'.split()
MON3 = {m[:3]: m for m in MONTHS}


def latex_to_html(src):
    s = src.strip()
    s = s.replace('\\times', '×').replace('\\sin\\theta', 'sin θ').replace('\\mu', 'μ')
    s = re.sub(r'\\text\{([^{}]*)\}', r'\1', s)
    s = re.sub(r'([A-Za-z])_\{([^{}]*)\}', r'\1<sub>\2</sub>', s)

    def frac(m):
        return f'<span class="frac"><span class="num">{m.group(1)}</span><span class="den">{m.group(2)}</span></span>'
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r'\\frac\{([^{}]*)\}\{([^{}]*)\}', frac, s)
    s = s.replace(' - ', ' − ')
    return f'<div class="formula">{s}</div>'


def convert(part, md_text, widgets):
    lines = md_text.split('\n')
    # drop the H1 title and byline (rebuilt on the part opener)
    body_start = 0
    for i, l in enumerate(lines):
        if l.startswith('## '):
            body_start = i
            break
    md_body = '\n'.join(lines[body_start:])
    # latex blocks
    blocks = {}

    def keep(m):
        k = f'@@F{len(blocks)}@@'
        blocks[k] = latex_to_html(m.group(1))
        return '\n' + k + '\n'
    md_body = re.sub(r'```latex\n(.*?)\n```', keep, md_body, flags=re.S)
    # figures
    figs = iter(widgets)

    def fig(m):
        cap = m.group(1).strip()
        wid = next(figs)
        k = f'@@F{len(blocks)}@@'
        if wid.startswith('svg:'):
            art = (BOOK / 'img' / (wid[4:] + '.svg')).read_text()
            blocks[k] = f'<figure class="diagram">{art}<figcaption>{html.escape(cap)}</figcaption></figure>'
        else:
            blocks[k] = f'<figure><img src="../{BOOK.name}/img/{wid}.png" alt=""><figcaption>{html.escape(cap)}</figcaption></figure>'
        return '\n' + k + '\n'
    md_body = re.sub(r'^&#91;embedded content: (.*?)\\\]\s*$', fig, md_body, flags=re.M)
    left = list(figs)
    assert not left, (part, left)
    def sketch(m):
        sid, size = m.group(1), m.group(2)
        k = f'@@F{len(blocks)}@@'
        f = BOOK / 'img' / 'sketches' / f'{sid}.png'
        inner = f'<img src="../{BOOK.name}/img/sketches/{sid}.png" alt="">' if f.exists() else f'<span class="ph">Sketch {sid}<br>{size} page</span>'
        blocks[k] = f'<div class="sketch {size}" data-id="{sid}">{inner}</div>'
        return '\n' + k + '\n'
    md_body = re.sub(r'^\[\[sketch (\w+) (quarter|half|third|fifth)\]\]\s*$', sketch, md_body, flags=re.M)
    # task lists
    md_body = re.sub(r'^- \[ \] ', '- ☐ ', md_body, flags=re.M)
    md_body = re.sub(r'^- \[x\] ', '- ☑ ', md_body, flags=re.M)
    out = markdown.markdown(md_body, extensions=['tables', 'sane_lists', 'md_in_html'])
    for k, v in blocks.items():
        out = out.replace(f'<p>{k}</p>', v).replace(k, v)
    # US dates from chips, e.g. Nov 21, 2026
    out = re.sub(r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (\d{1,2}), (\d{4})', lambda m: f'{m.group(2)} {MON3[m.group(1)]} {m.group(3)}', out)
    # bold lead in paragraphs that introduce a list or table: keep with next
    out = re.sub(r'<p><strong>([^<]*)</strong></p>', r'<p class="leadin"><strong>\1</strong></p>', out)
    return out


def main():
    src_parts = []
    front = BOOK / 'md' / 'front.md'
    if front.exists() and not ONLY:
        src_parts.append(f'<section class="front">{convert("front", front.read_text(), [])}</section>')
    for letter, title, aud, widgets in PARTS:
        if ONLY and letter not in ONLY:
            continue
        md_text = (BOOK / 'md' / f'part_{letter}.md').read_text()
        body = convert(letter, md_text, widgets)
        src_parts.append(f'<section class="part" data-part="{letter}" data-title="{html.escape(title)}" data-aud="{html.escape(aud)}">{body}</section>')
    tpl = (ENGINE / 'template.html').read_text()
    page = tpl.replace('<!--SOURCE-->', '\n'.join(src_parts)).replace('/*CFG*/null', json.dumps({k: v for k, v in CFG.items() if k != 'parts'}))
    (ENGINE / 'book.html').write_text(page)
    print('written', len(page))


main()
