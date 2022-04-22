from ..data.characters import CHARACTERS
from ..data.notes import get_notes
from ..events.parsing_functions import (ParsingFunction, parse_action,
                                        parse_encounter, parse_roll,
                                        parse_stat_update)
from .base_tracker import TrackerUI


class ActionsTracker(TrackerUI):
    """Widget used to track damage, critical chance,
    escape chance and miss chance rng.
    """
    def get_default_input_data(self) -> str:
        return get_notes(ACTIONS_NOTES_FILE, self.parser.gamestate.seed)

    def get_parsing_functions(self) -> dict[str, ParsingFunction]:
        """Returns a dictionary with strings as keys
        and parsing functions as values.
        """
        parsing_functions = {
            'roll': parse_roll,
            'waste': parse_roll,
            'advance': parse_roll,
            'encounter': parse_encounter,
            'stat': parse_stat_update,
            'action': parse_action,
        }
        return parsing_functions

    def edit_input(self, input_text: str) -> str:
        input_lines = input_text.splitlines()
        for index, line in enumerate(input_lines):
            match line.lower().split():
                case ['encounter', condition, *_]:
                    type_ = 'boss'
                    if 'simulated'.startswith(condition):
                        type_ = 'simulated'
                        name = 'simulation_(dummy)'
                    elif 'preemptive'.startswith(condition):
                        name = 'dummy_preemptive'
                    elif 'ambush'.startswith(condition):
                        name = 'dummy_ambush'
                    else:
                        name = 'dummy'
                    line = f'encounter {type_} {name} false'
                case ['encounter']:
                    line = 'encounter boss dummy false'
                case [character, *params] if character in CHARACTERS:
                    line = ' '.join(['action', character, *params])
            input_lines[index] = line
        return '\n'.join(input_lines)

    def edit_output(self, output: str) -> str:
        # if the text contains /// it hides the lines before it
        if output.find('///') >= 0:
            output = output.split('///')[-1]
            output = output[output.find('\n') + 1:]
        output = output.replace(' - Simulation: Dummy Normal', ': Simulation')
        output = output.replace(' - Boss: Dummy', ':')
        output = output.replace('Normal', '          ')
        output = output.replace('Ambush', 'Ambush    ')
        return output


ACTIONS_NOTES_FILE = 'actions_notes.txt'