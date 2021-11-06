#age


age = input("age=")
if not age.isdigit():
    print("入力エラー　ageに整数を入力してください")
else:
    age = int(age)
    if age < 6:
        print("未就学年齢です。")
    elif age < 13:
        print("義務教育年齢です。")
    elif age < 19:
        print("高校生か、就労しています。")
    elif age < 23:
        print("大学生か、就労しています。")        
    elif age < 27:
        print("おそらく大学院生か、就労しています。")
    elif age < 66:
        print("就労しています。")
    else:
        print("定年を迎えています。")
        
        
