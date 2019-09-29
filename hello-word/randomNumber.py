import random

secretNum = random.randint(1, 20)

print('这是一个1 ~ 100之间的数字')

# 设定用户可以猜测5次
for number in range(1, 6):
    print("请输入猜测的数：")
    guess = int(input())
    if guess == 0:
        break
    if guess < secretNum:
        print("太小啦")
    elif guess > secretNum:
        print("太大啦")
    else:
        break

if(guess == secretNum):
    print("真厉害，猜对啦，就是", str(guess))
else:
    print("很遗憾，正确的答案应该是", str(secretNum))
