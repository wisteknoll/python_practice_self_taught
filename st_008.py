
def nijyo(x):
        x = int(x)
        y = x ** 2
        return y

value = input('x=')

if not value.isdigit():
    print("入力エラー　整数を入力してください")
else:
    print(nijyo(value))
