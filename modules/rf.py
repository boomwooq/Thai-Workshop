from mojo.UI import CurrentWindow


def get_glyphs():
    current_window = CurrentWindow()
    if current_window.doodleWindowName == 'GlyphWindow':
        glyph = current_window.getGlyph().asFontParts()
        return [glyph]

    elif current_window.doodleWindowName == 'FontWindow':
        font = current_window.document.font.asFontParts()
        return font.selectedGlyphs

    else:
        return []
