import re

def Start(First_Date, Second_Date, First_Name, Second_Name):
    First = re.compile(f'^{First_Date} .* {First_Name}$')  # 个人聊天
    Second = re.compile(f'^{Second_Date} .* {Second_Name}$')  # 群内匹配
    First_Count = 0  # 个人聊天条数
    Second_Cound = 0  # 群内条数
    with open(First_Dic, 'r', encoding='UTF-8') as f:
        for i in f:
            p = re.match(First, i)
            if not p == None:
                First_Count += 1

    with open(Second_Dic, 'r', encoding='UTF-8') as f:
        for i in f:
            p = re.match(Second, i)
            if not p == None:
                Second_Cound += 1
    return First_Count, Second_Cound

First_Date = r'2020-02-23'#第一聊天记录：检查的日期
Second_Date = r'2020-02-23'#第二聊天记录：检查的日期
First_Name = r'xxx'#群内昵称(备注昵称)
Second_Name = r'yyy'#群内昵称(备注昵称)
First_Dic = r'xxxx.txt'#聊天记录的位置
Second_Dic = r'xxxx.txt'#聊天记录的位置

First_Count,Second_Cound = Start(First_Date,Second_Date,First_Name,Second_Name)
print(f'聊天条数1:{First_Count}')
print(f'聊天条数2:{Second_Cound}')
