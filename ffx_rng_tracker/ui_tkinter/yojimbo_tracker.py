from ..data.actions import YOJIMBO_ACTIONS
from ..data.notes import get_notes
from ..events.parsing_functions import (ParsingFunction,
                                        parse_compatibility_update,
                                        parse_death, parse_yojimbo_action)
from .base_widgets import BaseTracker


class YojimboTracker(BaseTracker):
    """Widget used to track Yojimbo rng."""

    def get_tags(self) -> dict[str, str]:
        tags = {
            'yojimbo low gil': ' [0-9]{1,7}(?= gil) ',
            'yojimbo high gil': ' [0-9]{10,}(?= gil) ',
            'stat update': '^.*changed to.+$',
        }
        tags.update(super().get_tags())
        return tags

    def get_parsing_functions(self) -> dict[str, ParsingFunction]:
        parsing_functions = super().get_parsing_functions()
        parsing_functions['death'] = parse_death
        parsing_functions['compatibility'] = parse_compatibility_update
        parsing_functions['yojimboaction'] = parse_yojimbo_action
        return parsing_functions

    def get_default_input_text(self) -> str:
        return get_notes('yojimbo_notes.txt', self.gamestate.seed)

    def get_input(self) -> str:
        input_data = super().get_input()
        input_lines = input_data.split('\n')
        for index, line in enumerate(input_lines):
            match line.lower().split():
                case ['death', *_]:
                    line = 'death yojimbo'
                case [action_name, *params] if action_name in YOJIMBO_ACTIONS:
                    line = ' '.join(['yojimboaction', action_name, *params])
            input_lines[index] = line
        return '\n'.join(input_lines)

    def parse_input(self) -> None:
        self.gamestate.reset()
        events_sequence = self.parser.parse(self.get_input())
        data = '\n'.join(str(e) for e in events_sequence)
        # if the text contains /// it hides the lines before it
        if data.find('///') >= 0:
            data = data.split('///')[-1]
            data = data[data.find('\n') + 1:]

        # update the text widget
        self.print_output(data)
