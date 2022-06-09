import numpy as np
import os
# 这是一个简单的程序
# 利用python实现各种重复性的操作
  

def DeletRepetitiveJPG(path):
    # 删除文件夹中重复的图片
    # 通过判断文件的名字是否包含")."来进行筛选
    files = os.listdir(path) #获得路径下面所有的文件名称
    for file in files:
        if (file[-5] == ")"): #判断文件名称倒是第四位是不是)
            os.remove(path+ "\\" + file) # 删除文件
        elif (")." in file): # 通过判断文件的名字是否包含")."
            os.remove(path+ "\\" + file)
        else:
            continue

def DeletRepetitiveJPGDrive():
    # 删除文件夹中重复的图片的子程序的驱动器
    print("***************************************************************")
    print("这是一个删除重复的JPG图片的一个小脚本")
    print("\n")
    path = input("请输入你的图片保存的文件夹路径：")
    DeletRepetitiveJPG(path)
    print("\n"+"删除完成")
    print("***************************************************************")

def main():
     DeletRepetitiveJPGDrive()

main()