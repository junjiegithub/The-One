#
#



msg = "你真是一个小天才"

say ="老师说："

print(say+msg)

print(type(msg))

print(msg+msg+msg)

print(msg*3)

# 可以使用索引去获取字符串中的字符   索引  字符串中的每一个字符都有索引， 下表
# 程序中数数   而是从0开始数数

print(msg[7])

# 计算 开始结束是左闭右开  [  )

start =1
end =3

print(msg[start:end])

# 索引支持负数    负索引是从-1开始的
print(msg[:5])

# 截取时  不写开始 代表从0开始，  不写结束 代表到最后
print(msg[:])

# 我性别男，今年18岁
sex ='男'
age ="18"
age_int=18

print('我性别'+sex+','+'今年'+age+'岁')
print('我性别%s，今年%s岁'%(sex, age))

print('我性别%s,今年%d岁'%(sex,age_int))
#
# f = 1.16
#
# print("今年体重又增长了%f公斤" % (f))
# print("今年体重又增长了%.1f公斤" % f)
#
# print("今年\"体重\"又增加了1.2公斤")
#
# print("今年'体重'又增加了1.2公斤")
#
# print('今年\'体重\'又增加了1.2公斤')
#
# print("床前明月光,\n疑是地上霜")
#
# print("今天是个好日子，\t你买的彩票中奖了")
#
# print(r"今天\t好日子")

f=1.16
print('今年体重又增长了%f公斤'%(f))
print('今年体重又增长了%.1f公斤'%f)
print("今年\"体重\"又增加了1.2公斤")
print("今年\'体重\'又增加了1.2公斤")
print("床前明月光，\n疑是地上霜。")
print("今天是个好日子，\t你买的彩票中奖了")
print(r"今天\好日子")




















'''
多重if判断
1，停车管理系统
 进场，输入车牌，出场，输入车牌，查询，输入车牌，判断有没有进场统计：数量，退出系统
2，银行管理系统
# # '''
# choice = int(input('请选择功能：1.进场 2.出场 3.查询 4.统计 5.退出'))
# car_location = [] #停车场
# if choice ==1:
#  car_in = input('输入车牌号：')
#  print(car_in+'进场了')
#  car_location.append(car_in)
# elif choice ==2:
#  car_out = input('输入查询的车牌号：')
#  print(car_out+'出场了')
#  car_location.remove(car_out)
# elif choice ==3:
#  car_inquire = input('输入查询的车牌号')
#  if car_inquire in car_location:
#    print('车辆在场')
#  else:
#    print('车辆不在')
# elif choice ==4:
#  print('停车场使用数量:',len(car_location))
# elif choice==5:
#  print('退出系统')
# else:
#  print('输入有误')

# import random
# choice = int(input('请选择你要办理的功能（1.办卡 2.存钱 3.取钱 4.修改密码 5.解锁 6.转账 7.退出）'))
#
# if choice ==1:
#  #办卡
#  print("办卡功能")
#  d1=random.randint(0,9)
#  d2=random.randint(0,9)
#  d3=random.randint(0,9)
#  card =  str(d1)+str(d2)+str(d3)
#  print('您的卡号是:%s'%card)
#
# elif choice ==2:
#  print('存钱功能')
#
# elif choice ==3:
#  print('取钱功能')
# elif choice ==4:
#  print('修改密码功能')
# elif choice ==5:
#  print('解锁功能')
# elif choice ==6:
#  print('转账功能')
# elif choice ==7:
#  print('退出系统')
# else:
#  print('您输入有误，请重新输入.....')
#
#











# str1 = '我们今天不去上学，我们去踢足球'
#
# print(str1.startswith('我们'))
# print(str1.endswith('我们'))
#
# # pos1 =str1.find('我们')
# #
# # print(pos1)
#
#
#














# #去掉前后的空格，中间的不会去掉
# print('   小 李：88  '.strip())
#
#
# #去掉最左边的空格
# print('   小 李：88  '.lstrip())
# #去掉最字符串后面的空格
# print('   小 李：88  '.rstrip())
# #去掉所有空格
# print('   小 李：88  '.replace(' ',''))
#
#










#
# str1= '小张:79| 小李：88 | 小赵：83'
#
# pos1 = str1.split('|')
#
# print(pos1)
#
# print('|'.join(pos1))

















#var1 是一个列表对象
# var1 =[1,2,3,4,5,6,7]
#
# #列表对象都有reverse方法
# var1.reverse()
# print(var1)


#print('我们今天不去上学，我们去踢足球'.count('我们'))
#
# str1 = '我们今天不去上学，我们去踢足球'
#
# posl = str1.find('我们',5)
#









#
# def squarep(num1,num2):
#  return num1**2 + num2**2
#
# ret = squarep(88,299)
# print(ret)
#
#
#
















#
# def job(name,GongSi):
#  print('今天9点20上班', name)
#  print('公司名字',GongSi)
#  return'面试结果'
# ret=job('吴俊杰','玉衡')
#
# print('返回结果')
# print(ret)
#
#












#
# try:
#  open('1.txt','r')
# except Exception as e:
#   print(e)
# finally:
#   print('hello')
















# import random
#
# number = random.randint(1,6)
# print(number)
#
# #摇色子游戏
# while 1:
#  getNum=int(input('请输入你猜测的数字：'))
#  if getNum==number:
#   print('恭喜你猜对了！奖励你20元现金')
#   break
#  elif getNum>number:
#   print('很遗憾！你猜的数字大了，扣除你1元现金')
#  else:
#   print('很遗憾!你猜的数字小了，扣除你1元现金')