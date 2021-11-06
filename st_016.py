musicans_dict = {
    'bump of chicken':['gungnir','only lonely glory', 'laugh maker'],
    'Judy and Mary':['DayDream', 'sobakasu', 'kujira 12 gou', 'radio'],
    'superfly':['ai wo komete nhanatabawo', 'beautiful', 'tamashii revolution'],
    "B'z":["Zero","Lair, Lair!", "mienai chikara", "brown'"]
    }

musican = input('musican_name=')
if musican in musicans_dict:
    result = musicans_dict[musican]
    print(result)
else:
    print("there are no musican you inputed.")
