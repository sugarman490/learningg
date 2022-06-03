import random
player = int(input("输入你要出的拳："))  # 石头1，剪刀2，布3
computer = random.randint(1, 3)
print("玩家出的是%s,电脑出的是%s" % (player, computer))
# 判断胜负
if (player == 1 and computer == 2) \
        or (player == 2 and computer == 3) \
        or (player == 3 and computer == 1):
    print("玩家胜利")
elif player == computer:
    print("平局")
else:
    print("电脑胜利")
print("1"*100)
