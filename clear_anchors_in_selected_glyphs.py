from modules.rf import get_glyphs


if __name__ == '__main__':
    f = CurrentFont()
    glyphs = get_glyphs()
    for g in glyphs:
        with g.undo('clear anchors'):
            g.clearAnchors()
            g.changed()
