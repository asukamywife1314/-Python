#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：邓证渝
日期：2020/4/8
"""

import random
def name_to_number(name):
  if name=="石头":
     return 0
  elif name=="史波克":
     return 1
  elif name=="布":
     return 2
  elif name=="蜥蜴":
     return 3
  elif name=="剪刀":
     return 4
  else :
     return None

def number_to_name(number):
    if number==0:
     return "石头"
    elif number==1:
     return "史波克"
    elif number==2:
     return "布"
    elif number==3:
     return "蜥蜴"
    elif number==4:
     return "剪刀"

   


def rpsls(player_choice):
    computer_number=random.randrange(0,4)
    player_number=name_to_number(player_choice)
    computer_name=number_to_name(computer_number)
    print("您的选择为：%s"%(choice_name))
    print("计算机的选择为：%s"%(computer_name))
    a=(computer_number-player_number)%5
    if   a==1 or a==2:
           print("您赢了!")
    elif a==3 or a==4:
	       print("机器赢了!")
    elif a==0:
		   print("平局")
		          
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)
