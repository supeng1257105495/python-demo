# import random

# # 定义骰子


# def roll_dice(num=2):  # n 默认值为2
#     total = 0
#     for _ in range(num):
#         total += random.randint(1, 6)
#     return total


# index = 0
# plearA = 0
# plearB = 0
# money = 10000000

# while money > 0:
#     print('玩家总资产', money)
#     #
#     index += 1
#     while True:
#         # mon = input('请下注： ')
#         # if(index % 2 == 0):
#         #     mon = '100'
#         # else:
#         mon = '100000'
#         if(mon.isdigit()):
#             debt = int(mon)
#         else:
#             debt = int(0)
#         if 0 < debt <= money:  # (if debt >0 and debt <= money)
#             break
#     first_point = roll_dice()
#     # print('玩家摇出了%d点' % first_point)
#     go_on = False
#     if first_point == 7 or first_point == 11:
#         # print('玩家胜!')
#         money += debt
#         plearA += 1
#     elif first_point == 2 or first_point == 3 or first_point == 12:
#         # print('庄家胜!')
#         money -= debt
#         plearB += 1
#     else:
#         go_on = True
#     while go_on:
#         current_point = roll_dice()
#         # print('庄家摇出了%d点' % current_point)
#         if current_point == 7:
#             # print('庄家胜!')
#             money -= debt
#             go_on = False
#             plearB += 1
#         elif current_point == first_point:
#             # print('玩家胜!')
#             money += debt
#             go_on = False
#             plearA += 1

# if __name__ == '__main__':
#     print('你已经破产，游戏结束！')
#     print('玩家胜利次数%d' % plearA)
#     print('庄家胜利次数%d' % plearB)

# ------------------------------------------------------------------------
# import pandas as pd
# import random


# class gambler():
#     def __init__(self):
#         self.deposit = 1000000  # 百万存款，这里不考虑不动产
#         self.bet = 20000  # 赌资
#         self.usury = 0  # 借贷
#         self.lose = 0  # 连输局数


# # 创建人物
# Cathala = gambler()  # 赌博商人卡达拉
# Cathala.bet = 100000000
# Cathala.deposit = 100000000

# Geralt = gambler()  # Geralt是一名狂热的赌博爱好者


# bet = 1000  # 每一把1000块
# count = 0
# gambling_list = []  # 记录每局比赛的输赢


# def gambling(gambler_a, gambler_b, bet, count):  # a是庄家，b是闲家，bet是当局赌注，count是当前的赌局编号
#     point = random.randint(2, 12)  # 骰子点数
#     guess = random.randint(0, 1)  # 猜大小，0为小，1为大
#     if (point > 7 and guess == 1) or (point <= 7 and guess == 0):  # 猜对了
#         Geralt.bet += bet
#         Cathala.bet -= bet
#         return True
#     else:
#         Geralt.bet -= bet
#         Cathala.bet += bet
#         return False


# def One_day_gambling():
#     Geralt.bet = 20000
#     bet = 1000
#     count = 0
#     while True:
#         gambling_list.append(gambling(Cathala, Geralt, bet,  count))
#         count += 1
#         if count > 3 and gambling_list[count - 3] == gambling_list[count - 2] == gambling_list[count - 1] == False:
#             bet = bet * 1.5  # 连输三局加赌注，加完之后如果还输继续加，赢了赌注保持不变
#         if Geralt.bet <= -5000 or count >= 100:  # 每天最多只敢借五千的高利贷，每天最多100局，其实大部分都玩不到100局就输光了
#             break
#     return Geralt.bet-20000  # 返回每天独居结束时的负债或盈利


# def record_daily_gambling():
#     debt = []  # 记录每一天的最终盈亏
#     for i in range(3000):
#         n = One_day_gambling()
#         if n < 0:  # 小于零就要借高利贷了，计一天的利息
#             n = n*1.00167
#         debt.append(n)
#         if sum(debt) <= -1000000:  # 一百万输光算破产
#             return (sum(debt), i)  # 破产后记下最终输掉的资金，以及破产时间
#     return (sum(debt), 3000)  # 一直没有破产的人


# def main():
#     every_example = pd.DataFrame()
#     lost_money = []
#     bankrupt_time = []
#     for j in range(1000):
#         m = record_daily_gambling()
#         lost_money.append(m[0])
#         bankrupt_time.append(m[1])
#         print(j)
#     every_example['lost_money'] = lost_money
#     every_example['bankrupt_time'] = bankrupt_time
#     every_example.to_csv('experiment_data.csv', index=False, sep=',')


# if __name__ == "__main__":
#     main()
# ----------------------------------------------------------------------
# import random


# def select_sort(origin_items, comp=lambda x, y: x < y):
#     # 简单选择排序
#     items = origin_items[:]
#     for i in range(len(items) - 1):
#         min_index = i
#         for j in range(i + 1, len(items)):
#             if comp(items[j], items[min_index]):
#                 min_index = j
#         items[i], items[min_index] = items[min_index], items[i]
#     return items


# list = [6, 8, 4, 5, 6, 3, 6, 9, 8, 5, 1, 9,
#         2, 3, 6, 6, 9, 8, 5, 2, 21, 2, 3, 4, 5]
# print(select_sort(list))


# print("\t**************************")
# print("\t*                        *")
# print("\t*      Hey  Welcome!     *")
# print("\t*  游戏采用是三局两胜制  *")
# print("\t*  GoodLuck  Have Fun!   *")
# print("\t*                        *")
# print("\t**************************")

# mode = ['剪刀', '石头', '布']
# win_list = [['石头', '剪刀', ], ['剪刀', '布'], ['布', '石头']]
# prompt = """
# \t[0] 剪刀
# \t[1] 石头
# \t[2] 布
# \t请选择出拳的姿势："""

# player_win = 0
# computer_win = 0

# while True:

#     computer = random.choice(mode)
#     ind = int(input(prompt))

#     if ind > 2:
#         print("\t\033[31;1m你的输入有误,请重新输入\033[0m")
#         continue
#     else:
#         player = mode[ind]

# # 判断出拳胜负者以及胜利次数统计：
#     print(" \n       ****** Result ******      ")
#     print("\nPlayer:%s,Computer:%s" % (player, computer))
#     if player == computer:
#         print("\t\033[32;1m平局！再来一次！\033[0m")

#     elif [player, computer] in win_list:
#         print("'\t\033[31;1m甘拜下风，YOU WIN!!!\033[0m")
#         player_win += 1

#     else:
#         print("'\t'\n\033[34;1m手气不佳，YOU LOSE!!!\033[0m")
#         computer_win += 1

# # 根据统计的胜负次数，判断三局两胜制谁胜谁负：

#     print("\nPlayer Win Count:", player_win,
#           "\tComputer Win Count:", computer_win)
#     if player_win >= 3 and computer_win < 3:
#         print("\n\033[31;1m****** Player Win,Game Over!!! ******\033[0m")
#         print("\n\033[31;1m******        Bye              ******\033[0m")
#         exit()
#     elif computer_win >= 3 and player_win < 3:
#         print("\n\033[35;1m****** Computer Win，GookLuck!!! ******\033[0m")
#         print("\n\033[35;1m******          Bye              ******\033[0m")
#         exit()

# -----------------------------------------------------------
# # 1.让用户输入 最大和 最小数
# from random import randint
# # import random
# max_num = int(input('来了老弟, 请你输入要猜的最大数字吧'))
# min_num = int(input('来了老弟, 请你输入要猜的最小数字吧'))
# # 2. 生成[min_num, max_num] 的一个随机数
# generate_num = randint(min_num, max_num)
# # random.randint(min_num, max_num)
# # 3. 声明一个猜数字次数的变量,并进入循环
# count = 0
# while True:
#     count += 1
#     guess_num = int(input('老弟, 请开始你的表演'))
#     # 进行判断
#     if guess_num < generate_num:
#         print('老弟,这数猜小了哦')
#     elif guess_num > generate_num:
#         print('老弟,这回猜大了')
#     else:
#         if count == 1:
#             print('你也太厉害了, {}次就猜中了'.format(count))
#         elif count > 1 and count < 10:
#             print('恭喜你用了{}次对的数字'.format(count))
#         else:
#             print('你也太菜了, 用{}次才猜出来,洗洗睡吧'.format(count))
#         break

# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
# fish = 6
# while True:
#     total = fish
#     enough = True
#     for _ in range(5):
#         if (total - 1) % 5 == 0:
#             total = (total - 1) // 5 * 4
#         else:
#             enough = False
#             break
#     if enough:
#         print(fish)
#         break
#     fish += 5

# print(5 // 20)
# ---------------------------------------------------------------------------------

# str = "C语言中文网"
# print(str[0], "==", str[-6])
# print(str[5], "==", str[-1])

# str = "C语言中文网"
# # 取索引区间为[0,2]之间（不包括索引2处的字符）的字符串
# print(str[:2])
# # 隔 1 个字符取一个字符，区间是整个字符串
# print(str[::2])
# # 取整个字符串，此时 [] 中只需一个冒号即可
# print(str[:])

# str="c.biancheng.net"
# print("C语言"+"中文网:"+str)

# str = "C语言中文网"
# print(str*3)

# list = [None]*5
# print(list)

# s_age = input("请输入您的年龄:")
# age = int(s_age)
# assert 20 < age < 80
# print("您输入的年龄在20和80之间")

# #循环的初始化条件
# num = 1
# # 当 num 小于100时，会一直执行循环体
# while num < 100 :
#     print("num=", num)
#     # 迭代语句
#     num += 1
# print("循环结束!")

# a_tuple = ('fkit', 'crazyit', 'Charli')
# i = 0
# # 只有i小于len(a_list)，继续执行循环体
# while i < len(a_tuple):
#     print(a_tuple[i]) # 根据i来访问元组的元素
#     i += 1

# src_list = [12, 45, 34,13, 100, 24, 56, 74, 109]
# a_list = [] # 定义保存整除3的元素
# b_list = [] # 定义保存除以3余1的元素
# c_list = [] # 定义保存除以3余2的元素
# # 只要src_list还有元素，继续执行循环体
# while len(src_list) > 0:
#     # 弹出src_list最后一个元素
#     ele = src_list.pop()
#     # 如果ele % 2不等于0
#     if ele % 3 == 0 :
#         a_list.append(ele) # 添加元素
#     elif ele % 3 == 1:
#         b_list.append(ele) # 添加元素
#     else:
#         c_list.append(ele) # 添加元素
# print("整除3:", a_list)
# print("除以3余1:",b_list)
# print("除以3余2:",c_list)

# my_dict = {'语文': 89, '数学': 92, '英语': 80}
# # 通过items()方法遍历所有key-value对
# # 由于items方法返回的列表元素是key-value对，因此要声明两个变量
# for key, value in my_dict.items():
#     print('key:', key)
#     print('value:', value)
# print('-------------')
# # 通过keys()方法遍历所有key
# for key in my_dict.keys():
#     print('key:', key)
#     # 在通过key获取value
#     print('value:', my_dict[key])
# print('-------------')
# # 通过values()方法遍历所有value
# for value in my_dict.values():
#     print('value:', value)

# a_range = range(10)
# 对a_range执行for表达式
# a_list = [x * x for x in a_range]
# a_list集合包含10个元素
# print(a_range)