#!/usr/bin/env python3
#其中#!称为Shebang，目的是告诉shell要使用Python3解释器执行以下代码

#获取sys模块的命令参数
import sys

#异常处理
#有可能出现异常的代码
try:
#判断：输入的参数是否大于1个（其中[0]是脚本名称[1]为第一个参数 所以要>2）              or 输入的参数是否小于0  
    if len(sys.argv) > 2 or int(sys.argv[1]) < 0:
#抛出一个IndexError异常    
        raise IndexError()
 


#其中各项社会保险费social insurance在本程序中设置为0
    ins = 0

#起征点threshold为3500元
    thr = 3500


#计算应纳税所得额taxable income，将参数转化为整数使用int()
    tin = int(sys.argv[1]) - ins - thr

#使用if作为流程控制，求应纳税额tax payable
    if tin <= 1500:
        tp = tin * 0.03 - 0

#使用elif进一步判断是否选择该路径
    elif tin > 1500 and tin <= 4500:
        tp = tin * 0.1 - 105

    elif tin > 4500 and tin <= 9000:
        tp = tin * 0.2 - 555   

    elif tin > 9000 and tin <=35000:
        tp = tin * 0.25 - 1005

    elif tin > 35000 and tin <= 55000:
        tp = tin * 0.3 - 2755

    elif tin > 55000 and tin <= 80000:
        tp = tin * 0.35 - 5505

    else:
        tp = tin * 0.45 - 13505

#使用字符串的format函数格式化让输出保留两位小数
    print(format(tp, ".2f"))

#可能抛出异常的代码结束

#解决异常 打印错误信息
except IndexError:
    print("Parameter Error")
except ValueError:
    print("Parameter Error")


