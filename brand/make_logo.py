import math, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
F='/home/claude/jag-playbook/engine/fonts/'
def text_path(txt, font, size, x, y, track=0.0, anchor='middle'):
    f=TTFont(F+font); gs=f.getGlyphSet(); cmap=f.getBestCmap(); upm=f['head'].unitsPerEm
    sc=size/upm; adv=[]
    for ch in txt: adv.append(gs[cmap[ord(ch)]].width*sc + track*size)
    w=sum(adv)-track*size
    cx = x - (w/2 if anchor=='middle' else 0)
    out=[]
    for ch,a in zip(txt,adv):
        g=gs[cmap[ord(ch)]]; pen=SVGPathPen(gs)
        g.draw(TransformPen(pen,(sc,0,0,-sc,cx,y)))
        d=pen.getCommands()
        if d: out.append(d)
        cx+=a
    return ' '.join(out), w

C=math.cos(math.pi/6); S=200
def M(o,ex,ey):  # map 0..100 square: (x,y) -> o + x/100*ex + y/100*ey
    return f'matrix({ex[0]/100:.5f},{ex[1]/100:.5f},{ey[0]/100:.5f},{ey[1]/100:.5f},{o[0]:.3f},{o[1]:.3f})'
A_=(-C*S,-0.5*S); B_=(0,0); E_=(C*S,-0.5*S); T_=(0,-S)
GAP=7
left = M((A_[0]-GAP*C, A_[1]+GAP*0.5), (C*S,0.5*S), (0,S))
right= M((GAP*C, GAP*0.5), (C*S,-0.5*S), (0,S))
TOPS = {'t1': M((T_[0], T_[1]-GAP), (C*S,0.5*S), (-C*S,0.5*S)), 't2': M((A_[0], A_[1]-GAP), (C*S,-0.5*S), (C*S,0.5*S)), 't3': M((E_[0], E_[1]-GAP), (-C*S,-0.5*S), (-C*S,0.5*S))}
top = TOPS[sys.argv[1] if len(sys.argv)>1 else 't1']   # x toward E, y toward A: letter reads upright on the lid
SW=25
LET = {
 'J':'M22 16 H78 V60 Q78 84 54 84 H46 Q22 84 22 62 V54',
 'A':'M21 100 V38 Q21 15 44 15 H56 Q79 15 79 38 V100 M21 60 H79',
 'G':'M84 15 H44 Q21 15 21 38 V62 Q21 85 44 85 H56 Q79 85 79 62 V52 H52',
}
def mark(navy, accent, solid=False):
    faces=''
    if solid:
        for t in (left,right,top):
            col = accent if t is top else navy
            faces+=f'<rect x="0" y="0" width="100" height="100" rx="3" fill="{col}" transform="{t}"/>'
        lc = {'J':'#FFFFFF','A':'#FFFFFF','G':'#FFFFFF'}
    else:
        lc = {'J':accent,'A':navy,'G':navy}
    g='<defs><clipPath id="f"><rect x="0" y="0" width="100" height="100" rx="3"/></clipPath></defs>'
    for L,t in (('J',top),('A',left),('G',right)):
        g+=f'<g transform="{t}"><path d="{LET[L]}" clip-path="url(#f)" fill="none" stroke="{lc[L]}" stroke-width="{SW}" stroke-linecap="butt" stroke-linejoin="round"/></g>'
    return faces+g

def svg(navy, accent, solid=False, words=True, wordcol=None, bg='#FFFFFF'):
    wordcol = wordcol or navy
    body=f'<g transform="translate(300,250)">{mark(navy,accent,solid)}</g>'
    h=500
    if words:
        d2,_=text_path('JUST ASK GEORGE','inter-latin-700-normal.woff2',31,300,545,0.3)
        body+=f'<path d="{d2}" fill="{accent if not solid else navy}"/>'
        h=580
    rect = f'<rect width="600" height="{h}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 {h}" width="600" height="{h}">{rect}{body}</svg>'

NAVY='#0F2439'
variants_all = {
 'A_gold': svg(NAVY,'#C69B3F'),
 'B_safety_yellow': svg(NAVY,'#F2C200'),
 'C_safety_orange': svg(NAVY,'#F26A1B'),
 'D_solid_cube': svg(NAVY,'#F26A1B',solid=True),
 'E_one_colour': svg('#000000','#000000'),
 'F_reversed': svg('#FFFFFF','#F2C200',wordcol='#FFFFFF',bg=NAVY),
}
variants = {'final': svg(NAVY,'#F26A1B',solid=True,bg=None), 'final_no_tagline': svg(NAVY,'#F26A1B',solid=True,words=False,bg=None)}
for k,v in variants.items(): open(f'jag_logo_{k}.svg','w').write(v)
