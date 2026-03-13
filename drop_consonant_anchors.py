from importlib import reload
from modules import settings
reload(settings)

from modules import THAI_CONSONANTS, get_thai_glyphs_by_category
from modules.anchors import most_likely_right_margin, italic_x_offset
from modules.settings import BOR_HEIGHT
from modules.rf import get_glyphs


if __name__ == '__main__':
    f = CurrentFont()
    consonants = get_thai_glyphs_by_category(f, THAI_CONSONANTS)
    glyphs = get_glyphs()
    for g in glyphs:
        if g.name in consonants:
            print(f'✅ dropping anchors in {g.name}')
            rm = most_likely_right_margin(g)

            # drop top anchor
            x_offset = italic_x_offset(BOR_HEIGHT, f.info.italicAngle)
            top_anchor_coords = int(round(rm + x_offset)), BOR_HEIGHT
            g.appendAnchor('top', top_anchor_coords)

            # drop bottom anchor
            x_offset = italic_x_offset(BOR_HEIGHT, f.info.italicAngle)
            bottom_anchor_coords = int(round(rm)), 0
            g.appendAnchor('bottom', bottom_anchor_coords)

        else:
            print(f'⛔️ {g.name} not a consonant')
