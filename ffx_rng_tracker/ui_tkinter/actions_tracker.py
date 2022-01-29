from ..data.characters import CHARACTERS
from ..data.file_functions import get_notes
from ..data.monsters import MONSTERS
from ..events import Comment
from ..ui_functions import (parse_action, parse_encounter, parse_roll,
                            parse_stat_update)
from .base_widgets import BaseWidget, BetterText


class ActionsTracker(BaseWidget):
    """Widget used to track damage, critical chance,
    escape chance and miss chance rng.
    """

    def __init__(self, parent, *args, **kwargs):
        self.monster_names = sorted(list(MONSTERS.keys()))
        self.default_notes = get_notes('actions_notes.txt')
        super().__init__(parent, *args, **kwargs)

    def make_input_widget(self) -> BetterText:
        widget = super().make_input_widget()
        widget.set(self.default_notes)
        return widget

    def get_input(self):
        self.rng_tracker.reset()
        for character in CHARACTERS.values():
            character.reset_stats()

        input_lines = self.input_widget.get('1.0', 'end').split('\n')
        # parse through the input text
        for line in input_lines:
            words = line.lower().split()
            # if the line is empty or starts with # add it as a comment
            if words == [] or words[0][0] == '#' or words[0][:3] == '///':
                event = Comment(line)
            # if the line is not a comment use it to call a function
            else:
                event_name, *params = words
                if event_name in ('roll', 'waste', 'advance'):
                    event = parse_roll(*params)
                elif event_name == 'encounter':
                    if params and 'simulated'.startswith(params[0]):
                        enc_type = 'simulated'
                        name = 'Simulation (Miihen)'
                        forced_condition = 'normal'
                    else:
                        enc_type = 'set'
                        name = 'Klikk 1'
                        forced_condition = params[0] if params else 'normal'
                    event = parse_encounter(
                        enc_type, name, 'initiative', forced_condition)
                elif event_name == 'stat':
                    event = parse_stat_update(*params)
                # in this case its parsed as a character action
                elif event_name in CHARACTERS:
                    event = parse_action(*words)
                else:
                    event = Comment(f'No event called {event_name!r}')
            self.rng_tracker.events_sequence.append(event)

    def set_tags(self) -> list[tuple[str, str, bool]]:
        tags = [
            ('Encounter', 'encounter', False),
            ('Preemptive', 'preemptive', False),
            ('Ambush', 'ambush', False),
            ('Crit', 'crit', False),
            ('^.*changed to.+$', 'stat update', True),
            ('^#(.+?)?$', 'comment', True),
        ]
        tags.extend(super().set_tags())
        return tags

    def print_output(self) -> None:
        self.get_input()
        data = []
        for event in self.rng_tracker.events_sequence:
            line = str(event)
            # if the text contains /// it hides the lines before it
            if '///' in line:
                data.clear()
            elif line.startswith('Encounter'):
                icvs = ''
                for index, (c, icv) in enumerate(event.icvs.items()):
                    if index >= 7:
                        break
                    icvs += f'{c[:2]}[{icv}] '
                condition = str(event.condition)
                if condition == 'Normal':
                    condition = ''
                data.append(f'Encounter {event.index:3} {condition:10} {icvs}')
            else:
                data.append(line)

        data = '\n'.join(data)

        # update the text widget
        self.output_widget.config(state='normal')
        self.output_widget.set(data)
        self.highlight_patterns()
        self.output_widget.config(state='disabled')
