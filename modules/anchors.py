import math
from fontPens.marginPen import MarginPen
from collections import Counter


def get_margins_at(g, y):
    mp = MarginPen(g.font, y)
    g.draw(mp)
    return mp.getMargins()


def italic_x_offset(y_dist, angle):
    if angle:
        angle = math.radians(angle)
        x_offset = math.tan(-angle) * y_dist
        return int(round(x_offset))
    return 0


def most_likely_right_margin(g, resolution=10):
    it_angle = g.font.info.italicAngle
    collected_margins = []
    if g.bounds:
        bottom = int(round(g.bounds[1]))
        top = int(round(g.bounds[3]))
        for y in range(bottom, top, resolution):
            margins = get_margins_at(g, y)
            if margins:
                rm = margins[-1]
                offset = italic_x_offset(y, it_angle)
                rm_unskewed = rm - offset
                collected_margins.append(int(round(rm_unskewed)))
        most_common_margin, occurrence = Counter(collected_margins).most_common(1)[0]
        return most_common_margin
    return
