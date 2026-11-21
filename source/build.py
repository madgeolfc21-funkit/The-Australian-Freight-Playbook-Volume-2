import re, html, json, base64, pathlib, markdown

ROOT = pathlib.Path(__file__).resolve().parent
PARTS = [
    ('A', 'Freight Basics', 'Everyone: the shared language, map and rules', ['f97c1022-b30d', '74ee98f6-f6d6', 'c10e8897-d7f3', '1458725c-9628', 'cd619dd8-41fa']),
    ('B', 'The Shipper', 'For the person who buys freight', ['c8bb82c3-14f3', 'b62cdc1b-84ee', 'df1e552d-c808']),
    ('C', 'The Driver', 'For the person behind the wheel', ['fd597ee1-46bc', 'd9ac66be-7ffa', 'c77e68a4-3fb9', 'af5a8add-6025', '4683b7b7-0024', 'cb6ad2e2-6ef0']),
    ('D', 'The Operator', 'For the business that runs the trucks', ['5f141171-2a35', 'ed4f9f00-251c', '9e6b766d-8aeb', '705f1a20-e012', '18bdddfc-ead4', '17bfbcd3-afc7']),
    ('E', 'Growing the Business', 'From one truck to a 3PL', ['3a8f45a7-dd82', '8dfc387e-fe34', 'b0277428-59fe', '821f5eee-5a66']),
    ('F', 'Rail, Air, Sea and Last Mile', 'The other modes, at working depth', ['f9672b2e-2cff']),
    ('G', 'Numbers and Tool Index', 'KPIs, the 28 tools, the update calendar and the gaps', ['0a0aac09-cf27']),
]
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
        blocks[k] = f'<figure><img src="img/{wid}.png" alt=""><figcaption>{html.escape(cap)}</figcaption></figure>'
        return '\n' + k + '\n'
    md_body = re.sub(r'^&#91;embedded content: (.*?)\\\]\s*$', fig, md_body, flags=re.M)
    left = list(figs)
    assert not left, (part, left)
    # task lists
    md_body = re.sub(r'^- \[ \] ', '- ☐ ', md_body, flags=re.M)
    md_body = re.sub(r'^- \[x\] ', '- ☑ ', md_body, flags=re.M)
    out = markdown.markdown(md_body, extensions=['tables', 'sane_lists'])
    for k, v in blocks.items():
        out = out.replace(f'<p>{k}</p>', v).replace(k, v)
    # US dates from chips, e.g. Nov 21, 2026
    out = re.sub(r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (\d{1,2}), (\d{4})', lambda m: f'{m.group(2)} {MON3[m.group(1)]} {m.group(3)}', out)
    # bold lead in paragraphs that introduce a list or table: keep with next
    out = re.sub(r'<p><strong>([^<]*)</strong></p>', r'<p class="leadin"><strong>\1</strong></p>', out)
    return out


def main():
    src_parts = []
    for letter, title, aud, widgets in PARTS:
        md_text = (ROOT / 'md' / f'part_{letter}.md').read_text()
        body = convert(letter, md_text, widgets)
        src_parts.append(f'<section class="part" data-part="{letter}" data-title="{html.escape(title)}" data-aud="{html.escape(aud)}">{body}</section>')
    tpl = (ROOT / 'template.html').read_text()
    page = tpl.replace('<!--SOURCE-->', '\n'.join(src_parts))
    (ROOT / 'book.html').write_text(page)
    print('written', len(page))


main()
