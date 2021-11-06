import re

l = "Beautiful is better than ugly."
matches = re.findall("Beautiful", l)

print(matches)

matches_2 = re.findall("beautiful", l, re.IGNORECASE)

print(matches_2)


 
zen = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

m = re.findall("^If", zen, re.MULTILINE)
print(m)


string = "Two too."

m2 = re.findall("t[ow]o", string, re.IGNORECASE)
print(m2)


line = "123 hi 34 hello."
m3 = re.findall("\d", line, re.IGNORECASE)
print(m3)

line_2 = "824reg84fd;s31."
m4 = re.findall("\d", line_2, re.IGNORECASE)
print(m4)


t = "__one__two__three__"
found = re.findall("__.*?__", t)
for match_x in found:
    print(match_x)

t2 = "__one____two__three__"
found2 = re.findall("__.*?__", t2)
for match_xx in found2:
    print(match_xx)

t3 = "__one____two____three__"
found3 = re.findall("__.*?__", t3)
for match_xxX in found3:
    print(match_xxX)


line_3 = "I love $"
m5 = re.findall("\\$", line_3, re.IGNORECASE)
print(m5)



