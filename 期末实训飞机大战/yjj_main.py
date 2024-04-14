from yjj_sprites import *
from yjj_music import *

# 设置窗口名
pygame.display.set_caption("宇将军飞踢")

pygame.init()


class YjjGame(object):

    def __init__(self):
        print("游戏初始化")

        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        lb = pygame.image.load("./images/cover.jpg")
        self.screen.blit(lb, (0, 0))
        pygame.display.update()
        lb_sound = pygame.mixer.Sound("./sounds/cover.wav")
        lb_sound.play()
        pygame.time.wait(3000)
        # 背景音乐
        back_music()
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

        # 设置定时事件
        # 敌机出现时间
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(CREATE_DY_EVENT, 10000)
        # 子弹出现时间
        pygame.time.set_timer(YJJ_FIRE_EVENT, 500)

    def __create_sprites(self):

        # 背景精灵和精灵组
        bg1 = Background("./images/background1.png")
        # 0,0
        bg2 = Background("./images/background2.png")
        bg2.rect.y = -bg2.rect.height
        bg3 = Background("./images/background3.png")
        bg3.rect.y = -bg3.rect.height * 2
        bg4 = Background("./images/background4.png")
        bg4.rect.y = -bg4.rect.height * 3
        bg5 = Background("./images/background5.png")
        bg5.rect.y = -bg5.rect.height * 4
        self.back_group = pygame.sprite.Group(bg1, bg2, bg3, bg4, bg5)

        # 创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        self.dy_group = pygame.sprite.Group()

        # 创建英雄的精灵和精灵组
        self.yjj = Yjj()
        self.yjj_group = pygame.sprite.Group(self.yjj)

    def start_game(self):
        print("游戏开始")

        while True:
            # 刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新/绘制精灵组
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    def __event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                YjjGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机精灵
                enemy = Enemy()
                # 添加到敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == CREATE_DY_EVENT:
                dy = Dy()
                self.dy_group.add(dy)
            # 子弹
            elif event.type == YJJ_FIRE_EVENT:
                self.yjj.fire()
                # 开火音乐
                fire_music()

        # 键盘指令移动
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a]:
            self.yjj.left()
        if keys_pressed[pygame.K_d]:
            self.yjj.right()
        if keys_pressed[pygame.K_w]:
            self.yjj.up()
        if keys_pressed[pygame.K_s]:
            self.yjj.down()

    def __check_collide(self):
        # 子弹摧毁敌机
        lx = pygame.sprite.groupcollide(self.yjj.bullets, self.enemy_group, True, True)
        if len(lx) > 0:
            lx_sound = pygame.mixer.Sound("./sounds/biu.wav")
            lx_sound.play()
        dy = pygame.sprite.groupcollide(self.yjj.bullets, self.dy_group, True, True)
        if len(dy) > 0:
            dy_sound = pygame.mixer.Sound("./sounds/ddyl.wav")
            dy_sound.play()
        # 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.yjj, self.enemy_group, True)
        if len(enemies) > 0:
            # 摧毁英雄
            self.yjj.kill()
            # 停止音乐音效
            pygame.mixer.music.stop()
            pygame.mixer.stop()
            # 坠机
            game_over_music()
            # 结束游戏
            YjjGame.__game_over()
        dy2 = pygame.sprite.spritecollide(self.yjj, self.dy_group, True)
        if len(dy2) > 0:
            # 摧毁英雄
            self.yjj.kill()
            # 停止音乐音效
            pygame.mixer.music.stop()
            pygame.mixer.stop()
            # 坠机
            game_over_music()
            # 结束游戏
            YjjGame.__game_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.dy_group.update()
        self.dy_group.draw(self.screen)

        self.yjj_group.update()
        self.yjj_group.draw(self.screen)

        self.yjj.bullets.update()
        self.yjj.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        pygame.mixer.music.stop()
        pygame.mixer.stop()
        pygame.mixer.music.load('./sounds/game_over.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = YjjGame
    game().start_game()
