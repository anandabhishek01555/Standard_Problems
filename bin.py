# A simple way to convert a number from decimal to binary.

x=int(input())
x=bin(x)
print(x[2:])

# n= int(input())
# li=list()
# while n>0:
#     r = n%2
#     li.append(r)
#     n=n//2 
# li.reverse()
# print("".join(list(map(str,li))))
