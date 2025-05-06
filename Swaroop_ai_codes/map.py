def make_even(num):
    if num%2!=0:
        return num+1
    return num
arr=[234,57,93,247,891,45]
y= map(make_even,arr)
print(list(y))