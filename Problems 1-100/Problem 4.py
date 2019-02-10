# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

list1 = [a for a in range (100, 1000)]
list2 = [b for b in range (100, 1000)]
list3 = []

for a in list1:
    for b in list2:
        c = a * b
        list3.append(c)

for i in list3:
    d = list(str(i))
    if d[0] == d[-1] and d[1] == d[-2] and d[2] == d[-3] and d[0] == '9':
        e = "".join(d)
print(e)






