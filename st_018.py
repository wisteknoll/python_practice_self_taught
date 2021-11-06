name = 'camus'
for i in range(5):
    print(name[i])

print('------------')

#answer1 = input("What did you write yesterday ?")
#answer2 = input("Where did you go yesterday ?")

#new_string = "Yesterday i wrote a {}. I sent it to {}.".format(answer1, answer2)

#print(new_string)
    
print('------------')

x = "aldous Hexley was born in 1894. he was born in the United Kingdom.".title()
print(x)

y = "aldous Hexley was born in 1894. he was born in the United Kingdom.".capitalize()
print(y)

print('------------')

lst = "Where now? Who now? When now? ".split("?")
print(lst)

print('------------')


fox = ["The", "fox", "jumped", "over", "the", "fence", "."]
fox = " ".join(fox)
print(fox)
fox = fox[0:-2] + "."
print(fox)

print('------------')

sentence = "A screaming comes across the sky."
sentence = sentence.replace("s", "$")
print(sentence)

print('------------')

first_index = "Hemingway".index("H")
print(first_index)

print('------------')

quote1 = "'Drink up,' said Ford, 'you've got three pints to get through.'"
quote2 = "'I forgot,' Lennie said softly. 'I tried not to forget. Honest to God I did, George.'"
quote3 = "'Yes,' I said, 'I have a reason,' and added very softly, 'My God.'"

print(quote1)
print(quote2)
print(quote3)

print('------------')

contact = "three" + "three" + "three"
mult = "three" * 3

print(contact)
print(mult)

print('------------')

sentence2 = "It was a bright cold day in April, and the clocks were striking  thirteen."
slce = sentence2[0:33]
print(slce)

slce_i = sentence2.index(",")
print(slce_i)
slce2 = slce[:slce_i+1]
print(slce2)









