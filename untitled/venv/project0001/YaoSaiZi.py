import random

#设置生成随机数，骰子1到6
number = random.randint(1,6)
print(number)

#摇色子游戏
while 1:
 getNum=int(input('请输入你猜测的数字：'))
 if getNum==number:
  print('恭喜你猜对了！奖励你20元现金')

 elif getNum==100:
     print('恭喜你猜对了！是100块，奖励你20元现金')

 elif getNum>number:
  print('很遗憾！你猜的数字大了，扣除你1元现金')
 else:
  print('很遗憾!你猜的数字小了，扣除你1元现金')