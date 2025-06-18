import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.music_played = False

    def play_music(self, audio, loop=-1):
        if not self.music_played:
            pygame.mixer.music.load(audio)
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(loop)
            self.music_played = True

    def stop_music(self):
        pygame.mixer.music.stop()
        self.music_played = False
