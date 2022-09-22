from enum import Enum, IntEnum


class StringEnum(str, Enum):
    """Enum subclass that creates enumerated constants
    that are also subclasses of str.
    """

    def __str__(self) -> str:
        return str.__str__(self)


class EncounterCondition(StringEnum):
    PREEMPTIVE = 'Preemptive'
    NORMAL = 'Normal'
    AMBUSH = 'Ambush'


class EquipmentSlots(IntEnum):
    MIN = 1
    MAX = 4


class Element(StringEnum):
    FIRE = 'Fire'
    ICE = 'Ice'
    THUNDER = 'Thunder'
    WATER = 'Water'
    HOLY = 'Holy'


class ElementalAffinity(StringEnum):
    ABSORBS = 'Absorbs'
    IMMUNE = 'Immune'
    RESISTS = 'Resists'
    WEAK = 'Weak'
    NEUTRAL = 'Neutral'


class Status(StringEnum):
    DEATH = 'Death'
    ZOMBIE = 'Zombie'
    PETRIFY = 'Petrify'
    POISON = 'Poison'
    POWER_BREAK = 'Power Break'
    MAGIC_BREAK = 'Magic Break'
    ARMOR_BREAK = 'Armor Break'
    MENTAL_BREAK = 'Mental Break'
    CONFUSE = 'Confuse'
    BERSERK = 'Berserk'
    PROVOKE = 'Provoke'
    THREATEN = 'Threaten'
    SLEEP = 'Sleep'
    SILENCE = 'Silence'
    DARK = 'Dark'
    PROTECT = 'Protect'
    SHELL = 'Shell'
    REFLECT = 'Reflect'
    NULBLAZE = 'NulBlaze'
    NULFROST = 'NulFrost'
    NULSHOCK = 'NulShock'
    NULTIDE = 'NulTide'
    REGEN = 'Regen'
    HASTE = 'Haste'
    SLOW = 'Slow'
    DEFEND = 'Defend'
    SHIELD = 'Shield'
    BOOST = 'Boost'
    DELAY = 'Delay'
    POWER_DISTILLER = 'Power Distiller'
    MANA_DISTILLER = 'Mana Distiller'
    SPEED_DISTILLER = 'Speed Distiller'
    ABILITY_DISTILLER = 'Ability Distiller'
    GUARD = 'Guard'
    SENTINEL = 'Sentinel'
    SCAN = 'Scan'
    LIFE = 'Life'
    AUTOLIFE = 'Auto-Life'
    EJECT = 'Eject'
    DOOM = 'Doom'
    CURSE = 'Curse'
    DELAY_WEAK = 'Delay (Weak)'
    DELAY_STRONG = 'Delay (Strong)'


class Character(StringEnum):
    TIDUS = 'Tidus'
    YUNA = 'Yuna'
    AURON = 'Auron'
    KIMAHRI = 'Kimahri'
    WAKKA = 'Wakka'
    LULU = 'Lulu'
    RIKKU = 'Rikku'
    SEYMOUR = 'Seymour'
    VALEFOR = 'Valefor'
    IFRIT = 'Ifrit'
    IXION = 'Ixion'
    SHIVA = 'Shiva'
    BAHAMUT = 'Bahamut'
    ANIMA = 'Anima'
    YOJIMBO = 'Yojimbo'
    CINDY = 'Cindy'
    SANDY = 'Sandy'
    MINDY = 'Mindy'
    UNKNOWN = 'Unknown'


class Rarity(StringEnum):
    COMMON = 'Common'
    RARE = 'Rare'


class EquipmentType(StringEnum):
    WEAPON = 'Weapon'
    ARMOR = 'Armor'


class DamageType(StringEnum):
    HP = 'HP'
    STRENGTH = 'Strength'
    SPECIAL_STRENGTH = 'Special Strength'
    MAGIC = 'Magic'
    MAGIC_MP = 'Magic (MP)'
    SPECIAL_MAGIC = 'Special Magic'
    ITEM = 'Item'
    ITEM_MP = 'Item (MP)'
    FIXED = 'Fixed'
    PERCENTAGE_TOTAL = 'Percentage (Total)'
    PERCENTAGE_CURRENT = 'Percentage (Current)'
    HEALING = 'Healing'
    GIL = 'Gil'


class TargetType(StringEnum):
    SELF = 'Self'
    SINGLE = 'Single'
    ALL = 'All'
    SINGLE_CHARACTER = 'Single character'
    ALL_CHARACTERS = 'All characters'
    SINGLE_MONSTER = 'Single monster'
    ALL_MONSTERS = 'All monsters'
    LAST_CHARACTER = 'Last character'
    LOWEST_HP_CHARACTER = 'Lowest HP character'


class MonsterSlot(IntEnum):
    MONSTER_1 = 0
    MONSTER_2 = 1
    MONSTER_3 = 2
    MONSTER_4 = 3
    MONSTER_5 = 4
    MONSTER_6 = 5
    MONSTER_7 = 6
    MONSTER_8 = 7


class Stat(StringEnum):
    HP = 'HP'
    MP = 'MP'
    STRENGTH = 'Strength'
    DEFENSE = 'Defense'
    MAGIC = 'Magic'
    MAGIC_DEFENSE = 'Magic defense'
    AGILITY = 'Agility'
    LUCK = 'Luck'
    EVASION = 'Evasion'
    ACCURACY = 'Accuracy'
    CHEER = 'Cheer'
    FOCUS = 'Focus'


class Item(StringEnum):
    POTION = 'Potion'
    HI_POTION = 'Hi-Potion'
    X_POTION = 'X-Potion'
    MEGA_POTION = 'Mega-Potion'
    ETHER = 'Ether'
    TURBO_ETHER = 'Turbo Ether'
    PHOENIX_DOWN = 'Phoenix Down'
    MEGA_PHOENIX = 'Mega Phoenix'
    ELIXIR = 'Elixir'
    MEGALIXIR = 'Megalixir'
    ANTIDOTE = 'Antidote'
    SOFT = 'Soft'
    EYE_DROPS = 'Eye Drops'
    ECHO_SCREEN = 'Echo Screen'
    HOLY_WATER = 'Holy Water'
    REMEDY = 'Remedy'
    POWER_DISTILLER = 'Power Distiller'
    MANA_DISTILLER = 'Mana Distiller'
    SPEED_DISTILLER = 'Speed Distiller'
    ABILITY_DISTILLER = 'Ability Distiller'
    AL_BHED_POTION = 'Al Bhed Potion'
    HEALING_WATER = 'Healing Water'
    TETRA_ELEMENT = 'Tetra Element'
    ANTARCTIC_WIND = 'Antarctic Wind'
    ARCTIC_WIND = 'Arctic Wind'
    ICE_GEM = 'Ice Gem'
    BOMB_FRAGMENT = 'Bomb Fragment'
    BOMB_CORE = 'Bomb Core'
    FIRE_GEM = 'Fire Gem'
    ELECTRO_MARBLE = 'Electro Marble'
    LIGHTNING_MARBLE = 'Lightning Marble'
    LIGHTNING_GEM = 'Lightning Gem'
    FISH_SCALE = 'Fish Scale'
    DRAGON_SCALE = 'Dragon Scale'
    WATER_GEM = 'Water Gem'
    GRENADE = 'Grenade'
    FRAG_GRENADE = 'Frag Grenade'
    SLEEPING_POWDER = 'Sleeping Powder'
    DREAM_POWDER = 'Dream Powder'
    SILENCE_GRENADE = 'Silence Grenade'
    SMOKE_BOMB = 'Smoke Bomb'
    SHADOW_GEM = 'Shadow Gem'
    SHINING_GEM = 'Shining Gem'
    BLESSED_GEM = 'Blessed Gem'
    SUPREME_GEM = 'Supreme Gem'
    POISON_FANG = 'Poison Fang'
    SILVER_HOURGLASS = 'Silver Hourglass'
    GOLD_HOURGLASS = 'Gold Hourglass'
    CANDLE_OF_LIFE = 'Candle of Life'
    PETRIFY_GRENADE = 'Petrify Grenade'
    FARPLANE_SHADOW = 'Farplane Shadow'
    FARPLANE_WIND = 'Farplane Wind'
    DESIGNER_WALLET = 'Designer Wallet'
    DARK_MATTER = 'Dark Matter'
    CHOCOBO_FEATHER = 'Chocobo Feather'
    CHOCOBO_WING = 'Chocobo Wing'
    LUNAR_CURTAIN = 'Lunar Curtain'
    LIGHT_CURTAIN = 'Light Curtain'
    STAR_CURTAIN = 'Star Curtain'
    HEALING_SPRING = 'Healing Spring'
    MANA_SPRING = 'Mana Spring'
    STAMINA_SPRING = 'Stamina Spring'
    SOUL_SPRING = 'Soul Spring'
    PURIFYING_SALT = 'Purifying Salt'
    STAMINA_TABLET = 'Stamina Tablet'
    MANA_TABLET = 'Mana Tablet'
    TWIN_STARS = 'Twin Stars'
    STAMINA_TONIC = 'Stamina Tonic'
    MANA_TONIC = 'Mana Tonic'
    THREE_STARS = 'Three Stars'
    POWER_SPHERE = 'Power Sphere'
    MANA_SPHERE = 'Mana Sphere'
    SPEED_SPHERE = 'Speed Sphere'
    ABILITY_SPHERE = 'Ability Sphere'
    FORTUNE_SPHERE = 'Fortune Sphere'
    ATTRIBUTE_SPHERE = 'Attribute Sphere'
    SPECIAL_SPHERE = 'Special Sphere'
    SKILL_SPHERE = 'Skill Sphere'
    WHT_MAGIC_SPHERE = 'Wht Magic Sphere'
    BLK_MAGIC_SPHERE = 'Blk Magic Sphere'
    MASTER_SPHERE = 'Master Sphere'
    LV_1_KEY_SPHERE = 'Lv. 1 Key Sphere'
    LV_2_KEY_SPHERE = 'Lv. 2 Key Sphere'
    LV_3_KEY_SPHERE = 'Lv. 3 Key Sphere'
    LV_4_KEY_SPHERE = 'Lv. 4 Key Sphere'
    HP_SPHERE = 'HP Sphere'
    MP_SPHERE = 'MP Sphere'
    STRENGTH_SPHERE = 'Strength Sphere'
    DEFENSE_SPHERE = 'Defense Sphere'
    MAGIC_SPHERE = 'Magic Sphere'
    MAGIC_DEF_SPHERE = 'Magic Def Sphere'
    AGILITY_SPHERE = 'Agility Sphere'
    EVASION_SPHERE = 'Evasion Sphere'
    ACCURACY_SPHERE = 'Accuracy Sphere'
    LUCK_SPHERE = 'Luck Sphere'
    CLEAR_SPHERE = 'Clear Sphere'
    RETURN_SPHERE = 'Return Sphere'
    FRIEND_SPHERE = 'Friend Sphere'
    TELEPORT_SPHERE = 'Teleport Sphere'
    WARP_SPHERE = 'Warp Sphere'
    MAP = 'Map'
    RENAME_CARD = 'Rename Card'
    MUSK = 'Musk'
    HYPELLO_POTION = 'Hypello Potion'
    SHINING_THORN = 'Shining Thorn'
    PENDULUM = 'Pendulum'
    AMULET = 'Amulet'
    DOOR_TO_TOMORROW = 'Door to Tomorrow'
    WINGS_TO_DISCOVERY = 'Wings to Discovery'
    GAMBLER_S_SPIRIT = 'Gambler\'s Spirit'
    UNDERDOG_S_SECRET = 'Underdog\'s Secret'
    WINNING_FORMULA = 'Winning Formula'


class Autoability(StringEnum):
    SENSOR = 'Sensor'
    FIRST_STRIKE = 'First Strike'
    INITIATIVE = 'Initiative'
    COUNTERATTACK = 'Counterattack'
    EVADE_AND_COUNTER = 'Evade & Counter'
    MAGIC_COUNTER = 'Magic Counter'
    MAGIC_BOOSTER = 'Magic Booster'
    ALCHEMY = 'Alchemy'
    AUTO_POTION = 'Auto-Potion'
    AUTO_MED = 'Auto-Med'
    AUTO_PHOENIX = 'Auto-Phoenix'
    PIERCING = 'Piercing'
    HALF_MP_COST = 'Half MP Cost'
    ONE_MP_COST = 'One MP Cost'
    DOUBLE_OVERDRIVE = 'Double Overdrive'
    TRIPLE_OVERDRIVE = 'Triple Overdrive'
    SOS_OVERDRIVE = 'SOS Overdrive'
    OVERDRIVE_TO_AP = 'Overdrive -> AP'
    DOUBLE_AP = 'Double AP'
    TRIPLE_AP = 'Triple AP'
    NO_AP = 'No AP'
    PICKPOCKET = 'Pickpocket'
    MASTER_THIEF = 'Master Thief'
    BREAK_HP_LIMIT = 'Break HP Limit'
    BREAK_MP_LIMIT = 'Break MP Limit'
    BREAK_DAMAGE_LIMIT = 'Break Damage Limit'
    GILLIONAIRE = 'Gillionaire'
    HP_STROLL = 'HP Stroll'
    MP_STROLL = 'MP Stroll'
    NO_ENCOUNTERS = 'No Encounters'
    FIRESTRIKE = 'Firestrike'
    FIRE_WARD = 'Fire Ward'
    FIREPROOF = 'Fireproof'
    FIRE_EATER = 'Fire Eater'
    ICESTRIKE = 'Icestrike'
    ICE_WARD = 'Ice Ward'
    ICEPROOF = 'Iceproof'
    ICE_EATER = 'Ice Eater'
    LIGHTNINGSTRIKE = 'Lightningstrike'
    LIGHTNING_WARD = 'Lightning Ward'
    LIGHTNINGPROOF = 'Lightningproof'
    LIGHTNING_EATER = 'Lightning Eater'
    WATERSTRIKE = 'Waterstrike'
    WATER_WARD = 'Water Ward'
    WATERPROOF = 'Waterproof'
    WATER_EATER = 'Water Eater'
    DEATHSTRIKE = 'Deathstrike'
    DEATHTOUCH = 'Deathtouch'
    DEATHPROOF = 'Deathproof'
    DEATH_WARD = 'Death Ward'
    ZOMBIESTRIKE = 'Zombiestrike'
    ZOMBIETOUCH = 'Zombietouch'
    ZOMBIEPROOF = 'Zombieproof'
    ZOMBIE_WARD = 'Zombie Ward'
    STONESTRIKE = 'Stonestrike'
    STONETOUCH = 'Stonetouch'
    STONEPROOF = 'Stoneproof'
    STONE_WARD = 'Stone Ward'
    POISONSTRIKE = 'Poisonstrike'
    POISONTOUCH = 'Poisontouch'
    POISONPROOF = 'Poisonproof'
    POISON_WARD = 'Poison Ward'
    SLEEPSTRIKE = 'Sleepstrike'
    SLEEPTOUCH = 'Sleeptouch'
    SLEEPPROOF = 'Sleepproof'
    SLEEP_WARD = 'Sleep Ward'
    SILENCESTRIKE = 'Silencestrike'
    SILENCETOUCH = 'Silencetouch'
    SILENCEPROOF = 'Silenceproof'
    SILENCE_WARD = 'Silence Ward'
    DARKSTRIKE = 'Darkstrike'
    DARKTOUCH = 'Darktouch'
    DARKPROOF = 'Darkproof'
    DARK_WARD = 'Dark Ward'
    SLOWSTRIKE = 'Slowstrike'
    SLOWTOUCH = 'Slowtouch'
    SLOWPROOF = 'Slowproof'
    SLOW_WARD = 'Slow Ward'
    CONFUSEPROOF = 'Confuseproof'
    CONFUSE_WARD = 'Confuse Ward'
    BERSERKPROOF = 'Berserkproof'
    BERSERK_WARD = 'Berserk Ward'
    CURSEPROOF = 'Curseproof'
    CURSE_WARD = 'Curse Ward'
    AUTO_SHELL = 'Auto-Shell'
    AUTO_PROTECT = 'Auto-Protect'
    AUTO_HASTE = 'Auto-Haste'
    AUTO_REGEN = 'Auto-Regen'
    AUTO_REFLECT = 'Auto-Reflect'
    SOS_SHELL = 'SOS Shell'
    SOS_PROTECT = 'SOS Protect'
    SOS_HASTE = 'SOS Haste'
    SOS_REGEN = 'SOS Regen'
    SOS_REFLECT = 'SOS Reflect'
    SOS_NULTIDE = 'SOS NulTide'
    SOS_NULFROST = 'SOS NulFrost'
    SOS_NULSHOCK = 'SOS NulShock'
    SOS_NULBLAZE = 'SOS NulBlaze'
    STRENGTH_3 = 'Strength +3%'
    STRENGTH_5 = 'Strength +5%'
    STRENGTH_10 = 'Strength +10%'
    STRENGTH_20 = 'Strength +20%'
    MAGIC_3 = 'Magic +3%'
    MAGIC_5 = 'Magic +5%'
    MAGIC_10 = 'Magic +10%'
    MAGIC_20 = 'Magic +20%'
    DEFENSE_3 = 'Defense +3%'
    DEFENSE_5 = 'Defense +5%'
    DEFENSE_10 = 'Defense +10%'
    DEFENSE_20 = 'Defense +20%'
    MAGIC_DEF_3 = 'Magic Def +3%'
    MAGIC_DEF_5 = 'Magic Def +5%'
    MAGIC_DEF_10 = 'Magic Def +10%'
    MAGIC_DEF_20 = 'Magic Def +20%'
    HP_5 = 'HP +5%'
    HP_10 = 'HP +10%'
    HP_20 = 'HP +20%'
    HP_30 = 'HP +30%'
    MP_5 = 'MP +5%'
    MP_10 = 'MP +10%'
    MP_20 = 'MP +20%'
    MP_30 = 'MP +30%'
    CAPTURE = 'Capture'
    AEON_RIBBON = 'Aeon Ribbon'
    DISTILL_POWER = 'Distill Power'
    DISTILL_MANA = 'Distill Mana'
    DISTILL_SPEED = 'Distill Speed'
    DISTILL_ABILITY = 'Distill Ability'
    RIBBON = 'Ribbon'
    EXTRA_1 = 'Extra 1'
    EXTRA_2 = 'Extra 2'
    EXTRA_3 = 'Extra 3'
    EXTRA_4 = 'Extra 4'
    EXTRA_5 = 'Extra 5'


class GameVersion(StringEnum):
    PS2NA = 'PS2 NA'
    HD = 'HD'


class SpeedrunCategory(StringEnum):
    ANYPERCENT = 'AnyPercent'
    BOOSTERS = 'Boosters'
    NSG = 'No Sphere Grid'
    NEMESIS = 'Nemesis'


HIT_CHANCE_TABLE = (25, 30, 30, 40, 40, 50, 60, 80, 100)

RNG_CONSTANTS_1 = (
    2100005341, 1700015771, 247163863, 891644838, 1352476256, 1563244181,
    1528068162, 511705468, 1739927914, 398147329, 1278224951, 20980264,
    1178761637, 802909981, 1130639188, 1599606659, 952700148, -898770777,
    -1097979074, -2013480859, -338768120, -625456464, -2049746478, -550389733,
    -5384772, -128808769, -1756029551, 1379661854, 904938180, -1209494558,
    -1676357703, -1287910319, 1653802906, 393811311, -824919740, 1837641861,
    946029195, 1248183957, -1684075875, -2108396259, -681826312, 1003979812,
    1607786269, -585334321, 1285195346, 1997056081, -106688232, 1881479866,
    476193932, 307456100, 1290745818, 162507240, -213809065, -1135977230,
    -1272305475, 1484222417, -1559875058, 1407627502, 1206176750, -1537348094,
    638891383, 581678511, 1164589165, -1436620514, 1412081670, -1538191350,
    -284976976, 706005400,
)

RNG_CONSTANTS_2 = (
    10259, 24563, 11177, 56952, 46197, 49826, 27077, 1257, 44164, 56565, 31009,
    46618, 64397, 46089, 58119, 13090, 19496, 47700, 21163, 16247, 574, 18658,
    60495, 42058, 40532, 13649, 8049, 25369, 9373, 48949, 23157, 32735, 29605,
    44013, 16623, 15090, 43767, 51346, 28485, 39192, 40085, 32893, 41400, 1267,
    15436, 33645, 37189, 58137, 16264, 59665, 53663, 11528, 37584, 18427,
    59827, 49457, 22922, 24212, 62787, 56241, 55318, 9625, 57622, 7580, 56469,
    49208, 41671, 36458,
)

ZANMATO_RESISTANCES = (0.8, 0.8, 0.8, 0.4, 0.4, 0.4)

ICV_BASE = (
    28, 28, 26, 24, 20, 16, 16, 15, 15, 15, 14, 14, 13, 13, 13, 12, 12, 11, 11,
    10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5,
    5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
    5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
    4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
    4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
    4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
    3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
)

ICV_VARIANCE = (
    0, 1, 1, 1, 1, 1, 2, 1, 2, 3, 1, 2, 1, 2, 3, 1, 2, 1, 2, 1, 2, 3, 4, 1, 2,
    3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 2, 2, 3, 3,
    4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4,
    4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 1, 1,
    1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4,
    4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7,
    7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4,
    4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
    6, 6, 6, 6, 6, 6,
)

# Yojimbo-related constants
BASE_COMPATIBILITY = {
    GameVersion.PS2NA: 50,
    GameVersion.HD: 128,
}
COMPATIBILITY_MODIFIER = {
    GameVersion.PS2NA: 30,
    GameVersion.HD: 10,
}
OVERDRIVE_MOTIVATION = {
    GameVersion.PS2NA: 2,
    GameVersion.HD: 20,
}
GIL_MOTIVATION_MODIFIER = {
    GameVersion.PS2NA: 2,
    GameVersion.HD: 4,
}

ELEMENTAL_AFFINITY_MODIFIERS = {
    ElementalAffinity.ABSORBS: -1.0,
    ElementalAffinity.IMMUNE: 0.0,
    ElementalAffinity.RESISTS: 0.5,
    ElementalAffinity.WEAK: 1.5,
    ElementalAffinity.NEUTRAL: 1.0,
}

EQUIPMENT_SLOTS_GIL_MODIFIERS = (1, 1, 1.5, 3, 5)
EQUIPMENT_EMPTY_SLOTS_GIL_MODIFIERS = (1, 1, 1.5, 3, 400)

TEMPORARY_STATS = {
    Stat.CHEER,
    Stat.FOCUS,
}

NO_RNG_STATUSES = {
    Status.DEFEND,
    Status.SHIELD,
    Status.BOOST,
    Status.DELAY,
    Status.POWER_DISTILLER,
    Status.MANA_DISTILLER,
    Status.SPEED_DISTILLER,
    Status.ABILITY_DISTILLER,
    Status.GUARD,
    Status.SCAN,
    Status.LIFE,
    Status.AUTOLIFE,
    Status.EJECT,
    Status.DOOM,
    Status.CURSE,
    Status.DELAY_WEAK,
    Status.DELAY_STRONG,
}
TEMPORARY_STATUSES = {
    Status.DEFEND,
    Status.SHIELD,
    Status.BOOST,
    Status.GUARD,
    Status.SENTINEL,
}
