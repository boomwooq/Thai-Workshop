from importlib import reload
from modules import settings
reload(settings)

from modules import THAI_TONEMARKS, get_thai_glyphs_by_category
from modules.anchors import most_likely_right_margin, italic_x_offset
from modules.settings import BOR_HEIGHT
from modules.rf import get_glyphs


if __name__ == '__main__':
    f = CurrentFont()
    tonemarks = get_thai_glyphs_by_category(f, THAI_TONEMARKS)
    tonemarks_level_1 = [gn for gn in tonemarks if '.small' not in gn]
    glyphs = get_glyphs()
    for g in glyphs:
        if g.name in tonemarks_level_1:
            print(f'✅ dropping anchors in {g.name}')
            rm = most_likely_right_margin(g)
            tonemark_top = g.bounds[3]

            # drop _top anchor
            x_offset = italic_x_offset(BOR_HEIGHT, f.info.italicAngle)
            _top_anchor_coords = int(round(rm + x_offset)), BOR_HEIGHT
            g.appendAnchor('_top', _top_anchor_coords)

            # drop top anchor
            x_offset = italic_x_offset(tonemark_top, f.info.italicAngle)
            top_anchor_coords = int(round(rm + x_offset)), tonemark_top
            g.appendAnchor('top', top_anchor_coords)

        else:
            print(f'⛔️ {g.name} not a level 1 tone mark')
