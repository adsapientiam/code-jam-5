"""All game contstants."""

import logging
from pathlib import Path, PurePath


LOG_LEVEL = logging.DEBUG

FPS = 60

WIDTH = 1285
HEIGHT = 725

SHOW_FPS = True

# Biomes are transformed to squares
# Width of a single biome (biomes can be chained together)
BIOME_WIDTH: int = 600
# Tile height is scaled based on how much the width scaled
# Width of a single tile (BIOME_WIDTH should be divisable by TILE_WIDTH)
TILE_WIDTH: int = 75
# Number of tile columns per biome
TILE_COLS: int = int(BIOME_WIDTH // TILE_WIDTH)
# Number of tile rows per biome
TILE_ROWS: int = 4

INDICATOR_WIDTH: int = 100

# How many pixels the background is allowed to move in 1 game tick
BG_SCROLL_SPEED = 20
BG_CLOUDS_SCROLL_SPEED = 1
FG_CLOUDS_SCROLL_SPEED = 2


PATH_PROJECT = PurePath(__file__).parent

PATH_DATA = PurePath(PATH_PROJECT).joinpath("data")

PATH_BACKGROUNDS = PurePath(PATH_PROJECT).joinpath("assets/images/background")
PATH_TILES = PurePath(PATH_PROJECT).joinpath("assets/images/tiles")

PATH_BUTTONS = PurePath(PATH_PROJECT).joinpath("assets/images/UI/buttons")
PATH_UI_BACKGROUNDS = PurePath(PATH_PROJECT).joinpath("assets/images/UI/backgrounds")
PATH_OTHER = PurePath(PATH_PROJECT).joinpath("assets/images/other")


USER_SETTINGS = PurePath(PATH_DATA).joinpath("user_settings.json")
# Game assets

# Background images
DESERT_BGS = list(Path(PATH_BACKGROUNDS).joinpath("desert").glob("*.png"))
CITY_BGS = list(Path(PATH_BACKGROUNDS).joinpath("city").glob("*.png"))
FOREST_BGS = list(Path(PATH_BACKGROUNDS).joinpath("forest").glob("*.png"))
MOUNTAINS_BGS = list(Path(PATH_BACKGROUNDS).joinpath("mountains").glob("*.png"))

# Background cloud layer will be behind foreground cloud layer
PATH_CLOUD_LAYERS = PurePath(PATH_BACKGROUNDS).joinpath("clouds/layers")
CLOUD_LAYERS_BG = [
    PurePath(PATH_CLOUD_LAYERS).joinpath("cloudLayer1.png"),
    PurePath(PATH_CLOUD_LAYERS).joinpath("cloudLayerB1.png"),
]
CLOUD_LAYERS_FG = [
    PurePath(PATH_CLOUD_LAYERS).joinpath("cloudLayer2.png"),
    PurePath(PATH_CLOUD_LAYERS).joinpath("cloudLayerB2.png"),
]

INDICATOR_ARROW = PurePath(PATH_OTHER).joinpath("indicator.png")

# Tiles

TILES_GRASS = list(Path(PATH_TILES).joinpath("grass").glob("*"))
TILES_WATER = list(Path(PATH_TILES).joinpath("water").glob("*"))

# UI assets

# Backgrounds
MAIN_MENU_BG = PurePath(PATH_UI_BACKGROUNDS).joinpath("main_menu2.png")

# Button images
PLAY_BTN = PurePath(PATH_BUTTONS).joinpath("play-btn-1.png")
PLAY_BTN_HOVER = PurePath(PATH_BUTTONS).joinpath("play-btn-1-hover.png")

OPT_BTN = PurePath(PATH_BUTTONS).joinpath("options-btn.png")
OPT_BTN_HOVER = PurePath(PATH_BUTTONS).joinpath("options-btn-hover.png")

CREDITS_BTN = PurePath(PATH_BUTTONS).joinpath("credits-btn.png")
CREDITS_BTN_HOVER = PurePath(PATH_BUTTONS).joinpath("credits-btn-hover.png")

QUIT_BTN = PurePath(PATH_BUTTONS).joinpath("quit-btn.png")
QUIT_BTN_HOVER = PurePath(PATH_BUTTONS).joinpath("quit-btn-hover.png")

BACK_BTN = PurePath(PATH_BUTTONS).joinpath("back-btn.png")
BACK_BTN_HOVER = PurePath(PATH_BUTTONS).joinpath("back-btn-hover.png")


class Color:
    """Represent RGB color values."""

    black = (0, 0, 0)

    white = (255, 255, 255)

    red = (255, 0, 0)

    aqua = (0, 255, 255)

    sky = (207, 239, 252)


class WindowState:
    """Represents windows states."""

    game = "game"
    main_menu = "main_menu"
    options = "options"
    credit = "credit"
    quited = "quit"


class ButtonProperties:
    """Represents buttons properties."""

    main_btn_w = 400
    main_btn_h = 100
    btn_gap = 20

    back_btn_x = 20
    back_btn_y = 20

    back_btn_w = 200
    back_btn_h = 100


class SliderProperties:
    """Represents slider properties."""

    margin_y = 0.2
    body_y = 200
    body_height = 10

    indicator_w = 20
    indicator_h = 60
