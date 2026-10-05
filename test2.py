import time
baka_list = ["","ｲｨﾁ","ﾆｨ","ｻｧﾝ","ﾖｫﾝ","ｺﾞｫ","ﾛｫｸ","ﾅﾅｧ","ﾊｧﾁ","ｷｭｳ"]
baka_list_keta = ["","ｼﾞｭｳ","ﾋｬｸ","ｾﾝ"]
def be_baka (num):
    for i in range(len(str(num))):
        print(i,len(str(num))-1-i)
        print((i == len(str(num))-1),(num != 1))
        if (i == len(str(num))-1)and(num != 1):
            print(baka_list[int(str(num)[-(i)])],end = "")
        print(baka_list_keta[len(str(num))-i-1],end = "")
    print("!")
n = 1
while(1):
    print(n,":",end = "")
    if (n % 3 == 0)or("3" in str(n) ):
        be_baka(n)
    else:
        print(n)
        time.sleep(0.2)
    n =n+1