

#variable = x

#x = input('変数x＝')
#x = int(input('変数x＝'))

y = input('変数x＝')
if not y.isdigit():
    print('入力エラー')
else:
    x = int(y)

#x = x
#if int(x) < 10:
    if x < 10:    
        print('10より少ない')
#elif int(x) >= 10:
    elif x >= 10:
        print('10以上です')
    else:
        print('入力エラー')
