#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ���֤��
���ڣ�2020/4/8
"""

import random
def name_to_number(name):
  if name=="ʯͷ":
     return 0
  elif name=="ʷ����":
     return 1
  elif name=="��":
     return 2
  elif name=="����":
     return 3
  elif name=="����":
     return 4
  else :
     return None

def number_to_name(number):
    if number==0:
     return "ʯͷ"
    elif number==1:
     return "ʷ����"
    elif number==2:
     return "��"
    elif number==3:
     return "����"
    elif number==4:
     return "����"

   


def rpsls(player_choice):
    computer_number=random.randrange(0,4)
    player_number=name_to_number(player_choice)
    computer_name=number_to_name(computer_number)
    print("����ѡ��Ϊ��%s"%(choice_name))
    print("�������ѡ��Ϊ��%s"%(computer_name))
    a=(computer_number-player_number)%5
    if   a==1 or a==2:
           print("��Ӯ��!")
    elif a==3 or a==4:
	       print("����Ӯ��!")
    elif a==0:
		   print("ƽ��")
		          
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)
