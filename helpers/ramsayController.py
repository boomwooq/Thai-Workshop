"""
ramsayController with glyph name autocomplete
"""

import objc
import ezui
from AppKit import NSObject
from mojo.subscriber import Subscriber, registerGlyphEditorSubscriber
from lib.tools.debugTools import ClassNameIncrementer

try:
    from ramsayStData import RamsayStData
except ImportError:
    pass


class DummyRamsayData(object):
    def __init__(self):
        self.data = dict()


class ComboBoxDataSource(NSObject, metaclass=ClassNameIncrementer):
    def init(self):
        self = objc.super(ComboBoxDataSource, self).init()
        self._glyphNames = []
        return self

    def setGlyphNames_(self, names):
        self._glyphNames = names

    def comboBox_completedString_(self, comboBox, text):
        if text in self._glyphNames:
            return text
        for name in self._glyphNames:
            if name.startswith(text):
                return name
        return text

    def comboBox_indexOfItemWithStringValue_(self, comboBox, text):
        if text not in self._glyphNames:
            return -1
        return self._glyphNames.index(text)

    def comboBox_objectValueForItemAtIndex_(self, comboBox, index):
        return self._glyphNames[index]

    def numberOfItemsInComboBox_(self, comboBox):
        return len(self._glyphNames)


class RamsayController(ezui.WindowController):
    def build(self):
        try:
            from ramsayStData import RamsayStData
        except ImportError:
            RamsayStData = DummyRamsayData()

        self.g = CurrentGlyph()
        self.glyph_order = list(self.g.font.glyphOrder)

        if self.g.isEmpty():
            self.gname = None
        else:
            self.gname = self.g.name
        gn_left, gn_right = RamsayStData.data.get(self.gname, ("n", "n"))

        content = f"""
        = HorizontalStack
        [_ {gn_left} ...] @left
        {self.gname} @middle
        [_ {gn_right} ...] @right
        (OK) @button
        """

        descriptionData = dict(
            left=dict(width=180, items=self.glyph_order),
            right=dict(width=180, items=self.glyph_order),
        )
        self.w = ezui.EZPanel(
            content=content,
            descriptionData=descriptionData,
            controller=self,
            size=(460, "auto"),
        )
        self.data_source = ComboBoxDataSource.alloc().init()
        self.data_source.setGlyphNames_(self.glyph_order)
        for item_name in ("left", "right"):
            item = self.w.getItem(item_name)
            cb = item.getNSComboBox()
            cb.setUsesDataSource_(True)
            cb.setDataSource_(self.data_source)

        button = self.w.getItem("button")
        button.bind(chr(13), [])
        self.w.getNSWindow().setTitleVisibility_(False)

    def started(self):
        self.w.open()

    def fieldCallback(self, sender):
        try:
            from ramsayStData import RamsayStData
        except ImportError:
            RamsayStData = DummyRamsayData()

        gn_left = self.w.getItem("left").get()
        gn_right = self.w.getItem("right").get()
        if RamsayStData.data.get(self.gname) != (gn_left, gn_right):
            RamsayStData.data[self.gname] = (gn_left, gn_right)
            RamsayStData.save()
            # sometimes it does not update in real time
            self.g.changed()

    def buttonCallback(self, sender):
        # try:
        #     from ramsayStData import RamsayStData
        # except ImportError:
        #     RamsayStData = DummyRamsayData()

        # gn_left = self.w.getItem('left').get()
        # gn_right = self.w.getItem('right').get()
        # if RamsayStData.data.get(self.gname) != (gn_left, gn_right):
        #     RamsayStData.data[self.gname] = (gn_left, gn_right)
        #     RamsayStData.save()
        #     self.g.changed()
        self.fieldCallback(sender)
        self.w.close()


class RamsayControllerMenuItem(Subscriber):
    def glyphEditorWantsContextualMenuItems(self, info):
        def _edit_ramsay(sender):
            RamsayController()

        menu_items = [
            ("Edit RamsaySt Neigbors", _edit_ramsay),
        ]

        info["itemDescriptions"].extend(menu_items)


registerGlyphEditorSubscriber(RamsayControllerMenuItem)
