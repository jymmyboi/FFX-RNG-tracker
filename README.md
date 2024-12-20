# FFX RNG Tracker
I forked this after being contacted by [Syo](https://www.twitch.tv/syotv) about updating this for the PS2 JP release.

To use the program download it from the [releases page](https://github.com/Grayfox96/FFX-RNG-tracker/releases), unzip it and open `FFX RNG tracker vXX.XX.XX.exe`.

To install the `ffx_rng_tracker` library run `pip install .` while in the main directory (where `pyproject.toml` is located).

To build the .exe run `python ffx_rng_tracker_pyinstaller.py` (the latest pyinstaller version is required, install with `pip install pyinstaller`).

GUI programs that implement the widgets:
* ffx_rng_tracker_ui: main program, implements all widgets;
* monster_data_viewer: shows information about monsters;
* encounters_tracker: tracks RNG related to encounters;
* seedfinder: used to find a seed given a series of action and the corresponding damage rolls.

# Configs
Game version and category can be changed in the configs file.
It's possible to switch to dark theme, use the default theme and change the font size.

# Notes
Place personalized notes files (*actions_notes.txt*, *drops_notes.txt*, *yojimbo_notes.txt*, *encounters_notes.csv*, *steps_notes.csv*) in one of the *ffx_rng_tracker_notes/* directories to override default ones. Prepend the notes filename with a seed number (e.g. *3556394350_actions_notes.txt*) to open them when the tracker is open with that specific seed.

# Credits
Credits to the #big-nerds channel in the [FFX/X-2 Speedruns Discord](https://discord.gg/X3qXHWG) for ideas and useful discussions.

Credits to [Rossy__](https://twitter.com/Rossy__TTV) for the disassembly for most of the in-game functions used, for testing a lot of random stuff and for providing the mon-data and shop-arms files.

Credits to [CrimsonInferno](https://www.twitch.tv/crimsoninferno9) for the initial idea and for providing the encounter formations and a lot of other useful information.

Credits to [OddMog](https://www.twitch.tv/oddmog), [ChrisTenarium](https://www.twitch.tv/christenarium) and [Loftus](https://www.twitch.tv/loftus) for initial testing and feedback.

Credits to [Madhyama](https://www.twitch.tv/madhyama) for testing the actions tracker and compiling the default actions notes.

Credits to [Camp4r](https://www.twitch.tv/camp4r) for the idea and design of the Encounters Table and Planner widgets.

Credits to [Mtbanger](https://www.twitch.tv/mtbanger) for fixing the Boosters% notes.

Credits to [Karifean](https://github.com/Karifean) for providing the decompilations of game files (Monsters/Actions/Encounters).

Using the [Azure](https://github.com/rdbende/Azure-ttk-theme) theme for ttk.
