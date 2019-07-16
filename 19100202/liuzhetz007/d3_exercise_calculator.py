#这是一个计算器程序，它的功能是实现：加、减、乘、除。
print("Welcome!这是一个计算器小程序，它的功能是实现：加、减、乘、除。\n")   #打印：欢迎界面

print("以下是关于本程序的说明：\n")   #打印：本程序的说明
print("1.本程序仅接受整数的加减乘除运算,且只能进行二元计算;\n")
print("2.退出程序请输入“.”（重要）;\n")
print("3.使用本程序时请确认已切换到全英文输入法;\n")
print("4.请根据提示一步一步进行，谢谢合作!\n")

def calculator(a,b,c):   #定义一个能够接收3个变量函数，它的功能是实现加、减、乘、除
    if b=='+':   #判断第二个参数是否为‘+’
        return int(a)+int(c)    #将加法的运算结果值返回

    if b=='-':   #判断第二个参数是否为‘-’
        return int(a)-int(c)    #将减法的运算结果值返回

    if b=='*':   #判断第二个参数是否为‘*’
        return int(a)*int(c)    #将乘法的运算结果值返回

    if b=='/':   #判断第二个参数是否为‘/’
        return int(a)/int(c)    #将除法的运算结果值返回


d0 = input("退出计算请输入“.”，继续运算请输入任意值，请输入：")   #打印：输入提示，并将用户输入的值赋给d0

while d0 != '.':    #用while语句（循环语句）判断：当d0不等于'.'时，开始循环
    d1 = input("请输入第一个整数：")    #打印：输入第一个整数的提示，并将用户输入的值赋给d1

    while not d1.isdigit():   #用while语句（循环语句）判断：当d1不是整数时，开始循环
        d1 = input("\n您的输入有误，请重新输入第一个整数：")    #重新为d1赋值，直到用户输入为整数时，循环结束

    else:   #当循环结束时，执行以下程序
        d2 = input("\n请输入运算符号（+，-，*，/）：")   #打印：输入运算符号的提示，并将用户输入的值赋给d2

        while d2 != '+' and d2 != '-' and d2 !='*' and d2 != '/':   #用while语句判断：当d2不等于‘+’，‘-’，‘*’，‘/’中任意一个时，开始循环
            d2 = input("\n您输入的不是+，-，*，/，请重新输入运算符：")   #重新为d2赋值，直到用户输入‘+’，‘-’，‘*’，‘/’中任意一个时，循环结束

        else:   #当循环结束时，执行以下程序
            d3 = input("\n请输入第二个整数：")   #打印：输入运算符号的提示，并将用户输入的值赋给d3

            while not d3.isdigit():   #用while语句判断：当d3不是整数时，开始循环
                    d3 = input("\n您的输入有误，请重新输入第二个整数：")     #重新为d3赋值，直到用户输入为整数时，循环结束

            else:   #当循环结束时，执行以下程序
                    print("计算结果为：")   #打印
                    print(d1,d2,d3,'=',calculator(d1,d2,d3))    #打印：运算结果，这里调用了之前定义的calculator（a,b,c）函数，通过计算，返回一个值，即为运算结果
                    d0 = input("\n继续运算请输入任意值，退出计算请输入“.”，请输入：")   #打印：询问用户是否继续运算，并将用户输入的值赋给d0，循环继续，返回到第27行开始执行

else:   #当d0等于'.'时，不执行循环，程序结束
    print("再见！")   #打印程序结束的提示