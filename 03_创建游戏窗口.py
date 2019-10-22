import pygame
import os
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
while True: #游戏循环
    pass
pygame.quit()

