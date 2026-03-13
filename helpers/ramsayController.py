import ezui
from mojo.subscriber import (
    Subscriber,
    registerGlyphEditorSubscriber)

try:
    from ramsayStData import RamsayStData
except ImportError:
    pass


class DummyRamsayData(object):

    def __init__(self):
        self.data = dict()


class RamsayController(ezui.WindowController):

    def build(self):
        try:
            from ramsayStData import RamsayStData
        except ImportError:
            RamsayStData = DummyRamsayData()

        self.g = CurrentGlyph()

        if self.g.isEmpty():
            self.gname = None
        else:
            self.gname = self.g.name
        gn_left, gn_right = RamsayStData.data.get(self.gname, ('n', 'n'))

        content = f"""
        = HorizontalStack
        [_ {gn_left} _] @left
        {self.gname} @middle
        [_ {gn_right} _] @right
        (OK) @button
        """

        descriptionData = dict(
            left=dict(
                callback='fieldCallback',
                continuous=True,
            ),
            right=dict(
                callback='fieldCallback',
                continuous=True,
            ),
        )

        self.w = ezui.EZPanel(
            content=content,
            controller=self,
            descriptionData=descriptionData,
            size=(100, 'auto'),
        )

        button = self.w.getItem('button')
        button.bind(chr(13), [])
        self.w.getNSWindow().setTitleVisibility_(False)

    def started(self):
        self.w.open()

    def fieldCallback(self, sender):
        try:
            from ramsayStData import RamsayStData
        except ImportError:
            RamsayStData = DummyRamsayData()

        gn_left = self.w.getItem('left').get()
        gn_right = self.w.getItem('right').get()
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
