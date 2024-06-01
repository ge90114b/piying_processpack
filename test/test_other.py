#测试杂货店

import numpy as np
import pygame as pg

def processcore(points:list,orgPoint:np.ndarray):
    arrayList,newPoints = [],[]    
    if len(points) == 11:           #正式用，调试不用
        for i1 in [0,5,6,9,10]:
            for i2 in [0,1]:
                if points[i1][i2]==0:
                    return "\n未识别到有效人体关键点！"
            #坐标转换 将手臂中点移向坐标原点（orgPoint）
        points = [points[0],points[5],points[6],points[9],points[10]]
    for i1 in points:
        arrayList.append(np.array(i1)) #将列表转为数组
    midP = arrayList[1] + (arrayList[2] - arrayList[1])/2 #计算中点（向量法）
    vector = orgPoint - midP #转换向量
    for i in arrayList:
        newPoints.append(i + vector)
    return newPoints


pg.init() #初始化
 
screen = pg.display.set_mode((400, 400)) #建立一个400x400的窗口
pg.display.set_caption("Pygame窗口")

orgp = (20,200)

while True:
    pg.draw.circle(screen, (255,60,0), orgp, 5, 10)
    newp = processcore([[-50,20],[-10,60],[-30,10],[90,50],[-10,10]],np.array(orgp))
    for index,i in enumerate(newp):
        if index in [1,2]:
            pg.draw.circle(screen, (0,60,255), i.tolist(), 5, 10)
        else:
            pg.draw.circle(screen, (255,255,255), i.tolist(), 5, 10)
    pg.display.flip()
    for event in pg.event.get(): #获取用户事件
        if event.type == pg.QUIT: #如果事件为关闭窗口
            pg.quit()