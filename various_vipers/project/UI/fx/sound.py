from pygame import mixer

from project.constants import BG_MUSIC, SOUNDS_BUTTONS as SND
from project.utils.user_data import UserData


user_data = UserData()


class Sound:
    """Represents all sounds and settings for the UI."""

    mixer.pre_init(44100, -16, 2, 2048)
    mixer.init()
    mixer.music.set_volume(0)
    mixer.music.load(str(BG_MUSIC))
    mixer.music.play(-1)

    click = mixer.Sound(str(SND["click3"]))
    check = mixer.Sound(str(SND["switch1"]))

    task_completed = mixer.Sound(str(SND["twoTone2"]))
    task_failed = mixer.Sound(str(SND["phaserUp1"]))

    task_click = mixer.Sound(str(SND["pepSound3"]))  # or powerUp4 phaserUp3 phaseJump1
    game_over = mixer.Sound(str(SND["powerUp3"]))

    @staticmethod
    def update():
        """Updates the volume of the sounds and music."""
        # edit the volume to be in 0.0 - 1.0 range

        if user_data.sound_mute:
            user_data.sound_volume = 0
            sound_vol = 0
        else:
            sound_vol = user_data.sound_volume / 100

        if user_data.music_mute:
            user_data.music_volume = 0
            music_vol = 0
        else:
            music_vol = user_data.music_volume / 100

        Sound.click.set_volume(sound_vol)
        Sound.check.set_volume(sound_vol)
        Sound.task_completed.set_volume(sound_vol)
        Sound.task_failed.set_volume(sound_vol)
        Sound.task_click.set_volume(sound_vol)
        Sound.game_over.set_volume(sound_vol)

        mixer.music.set_volume(music_vol)
