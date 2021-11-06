

y = input('変数x＝')
if not y.isdigit():
    print('入力エラー')
else:
    x = int(y)
    if x < 10:    
        print('10より少ない')
    elif x >= 10:
        print('10以上です')
    else:
        print('入力エラー')
