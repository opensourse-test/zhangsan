
num=int(input("输入一个600以内的整数:"))
if num==int(input("请输入第一次猜的数字:")):
    print("恭喜你猜对了")
elif num==int(input("不对，再猜一次:")):
    print("恭喜你猜对了")
elif num==int(input("不对，再猜最后一次:")):
    print("恭喜你猜对了")
else :
    print("很遗憾，三次都猜错了，我心里的数字是",num)
