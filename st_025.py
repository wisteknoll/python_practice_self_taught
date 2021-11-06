ans = [13, 26, 39, 52]

while True:
    b = input("入力値＝")
    if str(b) == "q":
        break
    elif b.isdigit() == False:
        print("数字を入力するか、qで終了します。")
    elif int(b) in ans:
        print(str(b) + ":正解です。" )
    elif int(b) not in ans:
        print(str(b) + ":不正解です。" )


if b == "q" :
    print("q:終了します。")
 

    
