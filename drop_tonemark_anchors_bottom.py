from importlib import reload
from modules import settings
reload(settings)

from modules import THAI_TONEMARKS, get_thai_glyphs_by_category
from modules.anchors import most_likely_right_margin, italic_x_offset
from modules.settings import BOR_HEIGHT
from modules.rf import get_glyphs


if __name__ == '__main__':
    f = CurrentFont()
    bottom_tonemarks = get_thai_glyphs_by_category(f, [0x0E38, 0x0E39, 0x0E3A])
    glyphs = get_glyphs()
    for g in glyphs:
        if g.name in bottom_tonemarks:
            print(f'✅ dropping anchors in {g.name}')
            rm = most_likely_right_margin(g)
            tonemark_bottom = g.bounds[1]

            # drop _bottom anchor
            _bottom_anchor_coords = rm, 0
            g.appendAnchor('_bottom', _bottom_anchor_coords)

            # drop bottom anchor
            x_offset = italic_x_offset(tonemark_bottom, f.info.italicAngle)
            bottom_anchor_coords = int(round(rm + x_offset)), tonemark_bottom
            g.appendAnchor('bottom', bottom_anchor_coords)

        else:
            print(f'⛔️ {g.name} not a bottom tone mark')
