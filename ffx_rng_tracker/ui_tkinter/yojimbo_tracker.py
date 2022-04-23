import tkinter as tk

from ..ui_abstract.yojimbo_tracker import YojimboTracker
from .input_widget import TkInputWidget
from .output_widget import TkOutputWidget


class TkYojimboOutputWidget(TkOutputWidget):

    def get_tags(self) -> dict[str, str]:
        tags = {
            'yojimbo low gil': ' [0-9]{1,7}(?= gil) ',
            'yojimbo high gil': ' [0-9]{10,}(?= gil) ',
            'stat update': '^.*changed to.+$',
        }
        tags.update(super().get_tags())
        return tags


class TkYojimboTracker(tk.Frame):

    def __init__(self, parent, seed: int, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        input_widget = TkInputWidget(self)
        input_widget.pack(fill='y', side='left')

        output_widget = TkYojimboOutputWidget(self)
        output_widget.pack(expand=True, fill='both', side='right')

        self.tracker = YojimboTracker(
            seed=seed,
            input_widget=input_widget,
            output_widget=output_widget,
            )
