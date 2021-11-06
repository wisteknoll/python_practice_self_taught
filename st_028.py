import statistics
import keyword
import math

# mean(平均値)
nums = [1, 5, 33, 12, 46, 33, 2]
a = statistics.mean(nums)
print(a)

#median(中央値)
b = statistics.median(nums)
print(b)

print(len(nums))
print(nums[3])

#mode(最頻値)
c = statistics.mode(nums)
print(c)

print("----------")

#keyword
d = keyword.iskeyword("mean")
e = keyword.iskeyword("median")
f = keyword.iskeyword("mode")
print(d, e, f)

print("----------")

#pstdev
g = statistics.pstdev(nums)
print(g)

#pvariance
h = statistics.pvariance(nums)
print(h)
i = math.sqrt(h)
print(i)
