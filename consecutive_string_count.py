a=input("enter the string")
s=a[0]
x=[s]
for i in a[1:]:
    if i ==s:
        x[-1]+=i
    else:
        s=i
        x.append(i)
print(x)