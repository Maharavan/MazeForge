# game/assets_loader.py
import pygame

def load_assets(cell_size, width, height):
    return {
        'wall': pygame.transform.scale(pygame.image.load('assets/images/wall.png').convert_alpha(), (cell_size, cell_size)),
        'path': pygame.transform.scale(pygame.image.load('assets/images/path.png').convert_alpha(), (cell_size, cell_size)),
        'jerry': pygame.transform.scale(pygame.image.load('assets/images/jerry.png').convert_alpha(), (cell_size, cell_size)),
        'tom': pygame.transform.scale(pygame.image.load('assets/images/tom.png').convert_alpha(), (cell_size, cell_size)),
        'spike': pygame.transform.scale(pygame.image.load('assets/images/spike.png').convert_alpha(), (cell_size, cell_size)),
        'bones': pygame.transform.scale(pygame.image.load('assets/images/bones.png').convert_alpha(), (cell_size, cell_size)),
        'wool': pygame.transform.scale(pygame.image.load('assets/images/wool.png').convert_alpha(), (cell_size, cell_size)),
        'cheese': pygame.transform.scale(pygame.image.load('assets/images/cheese.png').convert_alpha(), (cell_size, cell_size)),
        'icon': pygame.image.load('assets/images/icon.png').convert_alpha(),
        'background': pygame.transform.scale(pygame.image.load('assets/images/background.png').convert(), (width, height)),
        'welcome': pygame.transform.scale(pygame.image.load('assets/images/welcome.png').convert(), (width, height)),
        ('jerry','cheese'): pygame.transform.scale(pygame.image.load('assets/images/jerry.png').convert_alpha(), (200, 200)),
        ('tom','wool'): pygame.transform.scale(pygame.image.load('assets/images/tom.png').convert_alpha(), (200, 200)),
        ('spike','bones'): pygame.transform.scale(pygame.image.load('assets/images/spike.png').convert_alpha(), (200, 200)),
        ('easy', (7,)): pygame.transform.scale(pygame.image.load('assets/images/easy.png').convert_alpha(), (100, 100)),
        ('medium', (9, 11)): pygame.transform.scale(pygame.image.load('assets/images/medium.png').convert_alpha(), (120, 120)),
        ('hard', (13,)): pygame.transform.scale(pygame.image.load('assets/images/hard.png').convert_alpha(), (100, 100)),
        'gameover': pygame.transform.scale(pygame.image.load('assets/images/gameover.png').convert_alpha(), (300, 300)),
        'choosesize': pygame.transform.scale(pygame.image.load('assets/images/difficulty.png').convert_alpha(), (200, 200)),
        'character': pygame.transform.scale(pygame.image.load('assets/images/character.png').convert_alpha(), (200, 200)),
        'highscore': pygame.transform.scale(pygame.image.load('assets/images/highscore.png').convert_alpha(), (200, 200)),
        'currentscore': pygame.transform.scale(pygame.image.load('assets/images/score.png').convert_alpha(), (200, 200)),
        'start_button': pygame.transform.scale(pygame.image.load('assets/images/start.png').convert_alpha(), (100, 100)),
        'end_button': pygame.transform.scale(pygame.image.load('assets/images/quit.png').convert_alpha(), (100, 100)),
        'menu':pygame.transform.scale(pygame.image.load('assets/images/menu.png').convert_alpha(), (150, 150)),
        'leaderboard':pygame.transform.scale(pygame.image.load('assets/images/leaderboard.png').convert_alpha(), (200, 200)),

    }

