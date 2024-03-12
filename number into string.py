a={1:"one ",2:"two ",3:"three ",4:"four ",5:"five ",6:"six ",7:"seven ",8:"eight ",9:"nine "}
b={2:"",3:"hundered ",4:"thousand ",5:"",6:"lakh "}
d=input("enter the number")
x=[]
count=0
d1=int(d)
for i in range(len(d)):
    h=d1%10
    d1=d1//10
    count+=1
    if count>2:
        x.extend([b[count],a[h]])
    else:
        x.append(a[h])
print("".join(reversed(x)))