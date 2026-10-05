#小遣い決定プログラム
import random
kodukai = int(input("基本額は？"))
grade  = str(input("成績は？"))
grade = grade.upper()
result = {"A":kodukai*3,"B":kodukai*random.randint(1,3),"C":kodukai,"F":kodukai // 2,"N":0}
if grade in result:
    print("今月のあなたの成績は"+grade+"ですね。\n従っておこづかいは"+str(result[grade])+"円です。")
else:
    print("入力エラー") 