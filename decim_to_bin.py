def bina(num):
    x=[]
    if num == 0:
        print(0)
    while num>0:
        a=num%2
        x.append(a)
        num=num//2
    x.reverse()
    x1="".join(map(str,x))
    print(x1)
bina(255)

# def decimal_to_binary_recursive(num):
#     if num > 0:
#         return decimal_to_binary_recursive(num // 2) + str(num % 2)
#     else:
#         return ""
#
# # Test the function
# decimal_number = 255
# binary_result = decimal_to_binary_recursive(decimal_number)
# print(f"The binary representation of {decimal_number} is: {binary_result}")