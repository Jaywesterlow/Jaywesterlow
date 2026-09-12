from textpath import text_path
import os
OUT='/home/user/Jaywesterlow/design/brand/logos'
INK='#132340'; ORANGE='#2F6FD6'; SNOW='#F8FBFD'
BRI='fonts/bricolage.woff2'; INS='fonts/instrument.woff2'
def word(text,size,wght=700,opsz=96,ls=0):
    return text_path(text,BRI,size,{'wght':wght,'opsz':opsz},letter_spacing=ls)

def svg(w,h,body,bg=None):
    r=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
    if bg: r+=f'<rect width="{w}" height="{h}" fill="{bg}"/>'
    return r+body+'</svg>'

# ---------- Direction A: "Venster" — window grid whose top panes hold two peaks
def markA(x,y,s,fill=INK,acc=ORANGE):
    # s = size. Rounded square frame (stroke), 2x2 panes, peaks in the top row as filled shapes.
    st=s*0.075
    p=f'<g transform="translate({x},{y})">'
    p+=f'<rect x="{st/2}" y="{st/2}" width="{s-st}" height="{s-st}" rx="{s*0.12}" fill="none" stroke="{fill}" stroke-width="{st}"/>'
    # vertical + horizontal mullions
    p+=f'<rect x="{s/2-st/2}" y="{st/2}" width="{st}" height="{s-st}" fill="{fill}"/>'
    p+=f'<rect x="{st/2}" y="{s/2-st/2}" width="{s-st}" height="{st}" fill="{fill}"/>'
    # peaks: left pane a peak, right pane a peak with orange sun
    g=st*1.6
    p+=f'<path d="M{g},{s/2-g} L{s*0.30},{s*0.16} L{s/2-g},{s/2-g} Z" fill="{fill}"/>'
    p+=f'<path d="M{s/2+g},{s/2-g} L{s*0.74},{s*0.20} L{s-g},{s/2-g} Z" fill="{fill}"/>'
    p+=f'<circle cx="{s*0.61}" cy="{s*0.27}" r="{s*0.045}" fill="{acc}"/>'
    return p+'</g>'

def lockupA(fill=INK,acc=ORANGE,bg=None):
    d1,w1=word('Huis',64); d2,w2=word('Hinterglemm',64)
    W=int(112+max(w1,w2)+16); H=132
    b=markA(8,8,96,fill,acc)
    b+=f'<path transform="translate(120,60)" d="{d1}" fill="{fill}"/>'
    b+=f'<path transform="translate(120,118)" d="{d2}" fill="{fill}"/>'
    return svg(W,H,b,bg)

def stackedA(fill=INK,acc=ORANGE,bg=None):
    d1,w1=word('Huis Hinterglemm',40)
    W=int(max(w1,120)+48); H=232
    b=markA((W-120)/2,16,120,fill,acc)
    b+=f'<path transform="translate({(W-w1)/2},196)" d="{d1}" fill="{fill}"/>'
    return svg(W,H,b,bg)

# ---------- Direction B: "Dak" — one continuous sleek line: gable becomes ridge. Thin stroke, sharp joins.
def markB(x,y,s,fill=INK,acc=ORANGE):
    st=s*0.055
    # gable 45°/45°, then a symmetric summit: both flanks ~ equal slope so the top reads as a mountain
    pts=[(s*0.10,s*0.92),(s*0.10,s*0.50),(s*0.32,s*0.28),(s*0.50,s*0.46),(s*0.70,s*0.14),(s*0.90,s*0.40),(s*0.90,s*0.92)]
    d='M'+' L'.join(f'{a:.1f},{b:.1f}' for a,b in pts)
    p=f'<g transform="translate({x},{y})">'
    p+=f'<path d="{d}" fill="none" stroke="{fill}" stroke-width="{st}" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="6"/>'
    p+=f'<rect x="{s*0.10-st/2}" y="{s*0.92-st/2}" width="{s*0.80+st}" height="{st}" fill="{fill}"/>'
    # door sits on top of the baseline, not across it
    p+=f'<rect x="{s*0.245}" y="{s*0.70}" width="{s*0.11}" height="{s*0.22-st/2}" fill="{acc}"/>'
    return p+'</g>'

def lockupB(fill=INK,acc=ORANGE,bg=None):
    d1,w1=word('Huis Hinterglemm',56,wght=500,opsz=48,ls=-0.5)
    W=int(96+16+w1+12); H=112
    b=markB(4,8,96,fill,acc)
    b+=f'<path transform="translate(116,76)" d="{d1}" fill="{fill}"/>'
    return svg(W,H,b,bg)

def stackedB(fill=INK,acc=ORANGE,bg=None):
    d1,w1=word('Huis Hinterglemm',36,wght=500,opsz=48,ls=-0.3)
    W=int(max(w1,140)+48); H=228
    b=markB((W-140)/2,8,140,fill,acc)
    b+=f'<path transform="translate({(W-w1)/2},196)" d="{d1}" fill="{fill}"/>'
    return svg(W,H,b,bg)

# ---------- Direction C: "HH" monogram — two H's sharing a stem, crossbar drawn as a ridge
def markC(x,y,s,fill=INK,acc=ORANGE):
    st=s*0.16   # stem width
    p=f'<g transform="translate({x},{y})">'
    # three stems (H H share the middle stem)
    for cx in (s*0.10, s*0.42, s*0.74):
        p+=f'<rect x="{cx}" y="{s*0.10}" width="{st}" height="{s*0.80}" fill="{fill}"/>'
    # ridge crossbar: zigzag polygon spanning stem 1..3, sitting at mid height
    yb=s*0.50; a=s*0.085
    top=[(s*0.10+st,yb-a),(s*0.30,yb-a*2.2),(s*0.42,yb-a*0.4),(s*0.58+st*0.1,yb-a*2.6),(s*0.74,yb-a)]
    bot=[(s*0.74,yb+a),(s*0.58+st*0.1,yb-a*0.6),(s*0.42,yb+a*1.6),(s*0.30,yb-a*0.2),(s*0.10+st,yb+a)]
    d='M'+' L'.join(f'{u:.1f},{v:.1f}' for u,v in top+bot)+' Z'
    p+=f'<path d="{d}" fill="{fill}"/>'
    p+=f'<circle cx="{s*0.58+st*0.1}" cy="{s*0.24}" r="{s*0.05}" fill="{acc}"/>'
    return p+'</g>'

def lockupC(fill=INK,acc=ORANGE,bg=None):
    d1,w1=word('HUIS HINTERGLEMM',34,wght=800,opsz=12,ls=3)
    W=int(96+20+w1+12); H=112
    b=markC(8,8,96,fill,acc)
    b+=f'<path transform="translate(124,68)" d="{d1}" fill="{fill}"/>'
    return svg(W,H,b,bg)

def stackedC(fill=INK,acc=ORANGE,bg=None):
    d1,w1=word('HUIS HINTERGLEMM',26,wght=800,opsz=12,ls=3)
    W=int(max(w1,128)+48); H=224
    b=markC((W-128)/2,8,128,fill,acc)
    b+=f'<path transform="translate({(W-w1)/2},196)" d="{d1}" fill="{fill}"/>'
    return svg(W,H,b,bg)

sets={'a-venster':(markA,lockupA,stackedA),'b-dak':(markB,lockupB,stackedB),'c-monogram':(markC,lockupC,stackedC)}
for key,(mk,lk,stk) in sets.items():
    open(f'{OUT}/{key}-lockup.svg','w').write(lk())
    open(f'{OUT}/{key}-lockup-mono.svg','w').write(lk(INK,INK))
    open(f'{OUT}/{key}-lockup-reversed.svg','w').write(lk(SNOW,ORANGE,INK))
    open(f'{OUT}/{key}-stacked.svg','w').write(stk())
    open(f'{OUT}/{key}-lockup-white.svg','w').write(lk(SNOW,ORANGE))
    open(f'{OUT}/{key}-mark-white.svg','w').write(svg(128,128,mk(0,0,128,SNOW,ORANGE)))
    open(f'{OUT}/{key}-mark.svg','w').write(svg(128,128,mk(0,0,128)))
    open(f'{OUT}/{key}-mark-reversed.svg','w').write(svg(160,160,'<rect width="160" height="160" rx="24" fill="'+INK+'"/>'+mk(16,16,128,SNOW,ORANGE)))
    open(f'{OUT}/{key}-mark-orange.svg','w').write(svg(160,160,'<rect width="160" height="160" rx="24" fill="'+ORANGE+'"/>'+mk(16,16,128,SNOW,INK)))
print(os.listdir(OUT))
