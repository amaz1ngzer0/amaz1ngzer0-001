#!/usr/bin/env python3
#其中#!称为Shebang，目的是告诉shell要使用Python3解释器执行以下代码

#获取sys模块的命令参数
import sys
nums = [] #工号
salaries = [] #税前工资
netpays = [] #税后工资

#异常处理
#有可能出现异常的代码
try:
    for arg in sys.argv[1:]:  #使用 for 循环取出每个参数
        num_salary = (arg.split(':'))  #使用这个字符串的 arg.split(':') 分成两部分的列表
        nums.append(int(num_salary[0]))
        salaries.append(int(num_salary[1]))


    for salary in salaries:

#其中各项社会保险费social insurance 不考虑社保缴费基数
        ins = salary * (0.08 + 0.02 + 0.005 + 0 + 0 + 0.06)

#起征点threshold为3500元
        thr = 3500


#计算应纳税所得额taxable income，将参数转化为整数使用int()
        tin = salary - ins - thr

#使用if作为流程控制，求应纳税额tax payable
        if tin <= 1500 and tin > 0:
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

        elif tin > 80000:
            tp = tin * 0.45 - 13505
        else:
            tp = 0
       
        netpay = salary - ins - tp
    
        netpays.append(netpay)

    for n in range(len(names)):
        print(str(nums[n]) + ':' + format(netpays[n],'.2f'))

#可能抛出异常的代码结束

#解决异常 打印错误信息
except IndexError:
    print("Parameter Error")
except ValueError:
    print("Parameter Error")


