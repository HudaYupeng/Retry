# 请在下面添加代码
###### Begin ######
cu=input()
while cu not in ['N','n'] :
    if cu[:3] in ['CNY']:
            b=eval(cu[3:])/7.0227
            print("兑换成美元是{:.2f}元".format(b))
    elif cu[:3] in ['USD']:
            b=eval(cu[3:])*7.0227
            print("兑换成人民币是{:.2f}元".format(b))
    else :
        print("输入格式错误")
    cu = input()





###### End ######