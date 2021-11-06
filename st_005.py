x = input("x=")
if not x.isdigit():
    print("入力エラー　整数を入力してください")
else:
    y = input("y=")
    if not x.isdigit():
        print("入力エラー　整数を入力してください")
    else:
        print(int(x) % int(y))
