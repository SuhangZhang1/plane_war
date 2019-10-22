import pygame
import os
from plane_sprites import *
#form 跟import的导入区别是from导入的可以直接使用模块内部的工具，不需要模块名.调用了

#游戏初始化
pygame.init()
#创建游戏的窗口449*613
screen=pygame.display.set_mode((449,613))
#绘制背景图像
#1.加载图像数据
# 加载图片代码
bg=pygame.image.load(os.path.join('photo', 'ditu.png'))
# 2.blit 绘制图像（0，0）坐标原点
screen.blit(bg,(0,0))
# 3.update更新屏幕图像
pygame.display.update()
#绘制英雄机
hero=pygame.image.load(os.path.join('photo', 'hero.png'))
# 2.blit 绘制图像（0，0）坐标原点
screen.blit(hero,(200,530))
# 3.update更新屏幕图像
pygame.display.update()#可以在完成所有的display.blit()后在统一调用
#创建时钟对象
clock =pygame.time.Clock()
#1.定义rect记录飞机的初始位置
hero_rect=pygame.Rect(200,530,92,85)


#创建敌机的精灵
enemy=GameSprite("photo/diren.png",1)
enemy1=GameSprite("photo/diren.png",2)
# 创建敌机的精灵组
enemy_group=pygame.sprite.Group(enemy,enemy1)



#游戏循环->意味者游戏的正式开始！
while True: #游戏循环
    clock.tick(60)#每秒刷新60次
    #捕获事件
    # event_list=pygame.event.get()
    # if len(event_list)>0:
    #     print(event_list)
    #2修改飞机的位置
    for event in pygame.event.get():
        #判断事件类是否是退出事件
        if event.type==pygame.QUIT:
            print("游戏退出。。。")
            #quit卸载所有模块
            pygame.quit()
            #exit()直接退出系统(直接退出当前的代码)
            exit()
    hero_rect.y-=1
    if hero_rect.y<-85:
        hero_rect.y=613
    #3调用blit方法绘制图像
    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)
    #让精灵组调用两个方法
    #update方法
    enemy_group.update()

    #draw方法
    enemy_group.draw(screen)
    #调用update方法更新显示
    pygame.display.update()

pygame.quit()

