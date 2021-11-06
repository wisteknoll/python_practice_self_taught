a = "どこで？_だれが？_いつ？"
print(a.split("_"))

a = "どこで？　だれが？　いつ？"
print(a.split("　"))

print('----------')

words = ["The", "fox", "jumped", "over", "the", "fence", "."]

ans = " ".join(words)
ans = ans.replace(" .", ".")
print(ans)

print('----------')

b = "A screaming comes across the sky."
c = b.replace("s", "$")
print(b)
print(c)

print('----------')

name = "Hemingway"
#d = name[2:]
#print(d)
d = name.index("m")
print(d)

print('----------')

e = "okite 'tatakae!'"
print(e)

print('----------')

f = "t" + "h" + "r" + "e" + "e"
print(f)
g = f * 3
print(g)

print('----------')

h = "4月の晴れた寒い日で、時計がどれも13時を打っていた。"
print(h)
i = h.index("、")
print(i)
j = h[:i+1]
print(j)






