import pyglet

loader = pyglet.resource.Loader(path="../resources")


def load_image(filename: str, centered: bool = False):
    image = loader.image(filename)

    if centered:
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2

    return image


ENEMY_IMAGE = load_image("evil_business_man.png", centered=True)
PLAYER_IMAGE = load_image("penguin.png", centered=True)
SNOWBALL_IMAGE = load_image("snowball.png", centered=True)
ROCKET_IMAGE = load_image('rocket.png', centered=True)
SNOWSPLOSION_IMAGE = load_image('snowsplosion.png', centered=True)
