#2019-10-22上传
import random
import pygame
import os
#定义屏幕大小的常量
SCREEN_RECT=pygame.Rect(0,0,449,613)
#刷新的帧率
FRAME_PRE_SEC=60
#创建事件的定时常量
CREATE_ENEMY_EVENT=pygame.USEREVENT
#英雄发射子弹事件
HERO_FIRE_EVENT=pygame.USEREVENT+1

class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self,image_name,speed=1):
        #调用父类的初始化方法
        super().__init__()
        #定义对象属性

        self.image=pygame.image.load(image_name)
        self.rect=self.image.get_rect()#image.get_rect()返回的元组是（0，0，（图片长宽元组））
        self.speed=speed
    #重新父类update方法
    def update(self):
        # super().update()
        #在屏幕的垂直方向上移动
        self.rect.y+=self.speed
class Background(GameSprite):
    """游戏背景精灵"""
    def __init__(self,is_alt=False):
        #1.调用父类方法实现精灵的创建（image/rect/speed）
        super().__init__('./photo/ditu.png')
        #2.判断是否交替图像，如果是，需要设置初始化位置
        if is_alt:
            self.rect.y=self.rect .height

    def update(self):
        #1.调用父类的方法实现
        super().update()
        #2.判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕上方
        if self.rect.y>=SCREEN_RECT.height:
            self.rect.y=-self.rect.height
class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        #1.调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./photo/diren.png")
        #2.指定敌机初始随机速度1-3
        self.speed=random.randint(1,3)
        #3.指定敌机初始随机位置
        self.rect.bottom=0
        max_x=SCREEN_RECT.width-self.rect.width
        self.rect.x=random.randint(0,max_x)
        pass
    def update(self):
        #1.调用父类方法，保持垂直方向飞行
        super().update()
        #2.判断是否飞出屏幕，如果是，需要精灵组删除敌机
        if self.rect.y>=SCREEN_RECT.height:
            # print("飞机飞出屏幕，需要从敌机组删除飞机...")
            #kill方法可以将精灵从所有精灵组中移除，精灵就会自动销毁--def--才会调用
            self.kill()
        pass
    def __del__(self):
        # print("敌机挂了%s"%self.rect)
        pass
class Hero(GameSprite):
    """英雄精灵"""
    def __init__(self):
        #1.调用父类方法，设置image&speed
        super().__init__("./photo/hero.png",0)
        #2.设置英雄的初始位置
        self.rect.centerx=SCREEN_RECT.centerx
        self.rect.bottom=SCREEN_RECT.bottom-120
        #3.创建子弹精灵组
        self.bullets=pygame.sprite.Group()
    def update(self):
        #英雄在水平方向移动

        self.rect.x +=self.speed
        #控制英雄不能离开屏幕
        if self.rect.x<0:
            self.rect.x=0
        elif self.rect.right>SCREEN_RECT.right:
            self.rect.right=SCREEN_RECT.right
    def fire(self):
        print("发射子弹...")
        for i in(0,1):
            #1.创建子弹精灵
            bullet=Bullet()
            #2.设置精灵的位置
            bullet.rect.bottom=self.rect.y-i*20
            bullet.rect.centerx=self.rect.centerx
            #3.将精灵添加到精灵组
            self.bullets.add(bullet)
class Bullet(GameSprite):
    """子弹精灵"""
    def __init__(self):
        #调用父类方法，设置子弹图片，设置初始速度
        super().__init__("./photo/zidan.png",-2)
        pass
    def update(self):
        #调用父类方法，让子弹沿垂直方向飞行
        super().update()
        #判断子弹是否飞出屏幕
        if self.rect.bottom<0:
            self.kill()
        pass
    def __del__(self):
        print("子弹被销毁...")
        #haha