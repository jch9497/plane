import random
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 550, 800)
# 刷新的帧率
FRAME_PER_SEC = 60
# 敌机定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
CREATE_DY_EVENT = pygame.USEREVENT + 1
# 发射子弹
YJJ_FIRE_EVENT = pygame.USEREVENT + 2


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_name, speed=5):
        # 调用父类的初始化方法
        super().__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 向下移动
        self.rect.y += self.speed


class Background(GameSprite):
    # 背景循环

    def __init__(self, image_name):
        super().__init__("./images/background1.png")
        self.image = pygame.image.load(image_name)

    def update(self):
        # 调用父类
        super().update()
        # 判断是否移出屏幕，屏幕上方归位
        for i in (4, 3, 2, 1, 0):
            if self.rect.y >= SCREEN_RECT.height:
                self.rect.y = -self.rect.height * i


class Enemy(GameSprite):
    def __init__(self):
        # 调用父类
        super().__init__("./images/lx.png")
        # 初始随机速度
        self.speed = random.randint(1, 10)
        # 随机位置
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 调用父类
        super().update()
        # 飞出屏幕，删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        # print("lx挂了%s" % self.rect)
        pass


class Dy(GameSprite):
    def __init__(self):
        # 调用父类
        super().__init__("./images/dy.png")
        # 初始随机速度
        self.speed = random.randint(1, 3)
        # 随机位置
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 调用父类
        super().update()
        # 飞出屏幕，删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        # print("lx挂了%s" % self.rect)
        pass


class Yjj(GameSprite):
    def __init__(self):
        super().__init__("./images/yjj.png", 0)
        # 位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 50
        # 移动速度
        self.speed = 10
        # 子弹
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 控制在屏幕内
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        # 控制在屏幕
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.bottom > SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

    def up(self):  # 上
        self.rect.y -= self.speed

    def down(self):  # 下
        self.rect.y += self.speed

    def left(self):  # 左
        self.rect.x -= self.speed

    def right(self):  # 右
        self.rect.x += self.speed

    def fire(self):
        for i in (0, 1, 2):
            # 子弹
            bullet = Bullet()
            # 子弹位置
            bullet.rect.bottom = self.rect.y  # - i * 20
            bullet.rect.centerx = self.rect.centerx
            # 组
            self.bullets.add(bullet)


class Bullet(GameSprite):
    # 子弹
    def __init__(self):
        super().__init__("./images/ddx.png", -10)

    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        pass
