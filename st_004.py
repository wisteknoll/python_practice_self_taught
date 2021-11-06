

y = input('変数x＝')
if not y.isdigit():
    print('入力エラー')
else:
    x = int(y)
    if x <= 10:    
        print('10以下です')
    elif x > 10 and x <= 25:
        print('10より大きく、25以下です')
    else:
        print('25より大きいです')
