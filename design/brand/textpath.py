"""Shape a string with HarfBuzz and return an SVG path (y-down, units = font size px)."""
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.recordingPen import RecordingPen
import io, functools

@functools.lru_cache(None)
def _load(path):
    data=open(path,'rb').read()
    tt=TTFont(io.BytesIO(data))  # decompress woff2 for glyph outlines
    buf=io.BytesIO(); tt.flavor=None; tt.save(buf)
    face=hb.Face(buf.getvalue()); font=hb.Font(face)
    return tt, face, font

def text_path(text, path, size=100, variations=None, letter_spacing=0.0, features=None):
    tt, face, font = _load(path)
    upem=face.upem
    if variations:
        font.set_variations(variations)
        from fontTools.varLib.instancer import instantiateVariableFont
        tt_i=instantiateVariableFont(tt, variations, inplace=False)
    else:
        tt_i=tt
    glyphset=tt_i.getGlyphSet()
    order=tt_i.getGlyphOrder()
    buf=hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
    hb.shape(font, buf, features or {"kern":True,"liga":True})
    scale=size/upem
    x=0.0; pen=SVGPathPen(glyphset)
    for info,pos in zip(buf.glyph_infos, buf.glyph_positions):
        gname=order[info.codepoint]
        tp=TransformPen(pen,(scale,0,0,-scale,(x+pos.x_offset)*scale,-pos.y_offset*scale))
        glyphset[gname].draw(tp)
        x+=pos.x_advance+letter_spacing*upem/size
    return pen.getCommands(), x*scale

if __name__=="__main__":
    d,w=text_path("Huis Hinterglemm","fonts/bricolage.woff2",100,{"wght":700,"opsz":96})
    print(len(d), w)
