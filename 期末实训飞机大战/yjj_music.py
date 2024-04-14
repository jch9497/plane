import pygame


def fire_music():
    pass
    # 设置开火音乐
    pygame.mixer.init()
    effect = pygame.mixer.Sound('./sounds/fire.wav')
    pygame.mixer.Sound.play(effect)


def game_over_music():
    # 坠机音效
    pygame.mixer.init()
    pygame.mixer.music.load('./sounds/xg.wav')
    pygame.mixer.music.play()
    # 延时
    while pygame.mixer.music.get_busy():
        pass


def back_music():
    # 背景音乐
    pygame.mixer.init()
    # 加载播放音乐
    pygame.mixer.music.load('./sounds/yjj.mp3')
    pygame.mixer.music.play()
    back_sound = pygame.mixer.Sound('./sounds/yjjsong.mp3')
    back_sound.set_volume(0.1)
    back_sound.play(-1)
