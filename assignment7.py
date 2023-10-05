# calculate the area of square and area of rectangle
# def square(s):
#     print("area of this square=",s*s)
# def rectangle(h,w):
#     print("area of rectangle",h*w)
# s=int(input("enter the side of square"))
# square(s)
# h=int(input("enter the height:"))
# w=int(input("enter the wedth:"))
# rectangle(h,w)
#find a number is even or odd
# def checkeven(n):
#     if n%2==0:
#         print(f"{n} is even no")
#     else:
#         print(f"{n} is odd no")
# n=int(input("enter a number"))
# checkeven(n)
def factorial_with_validatio(n):
    if n<0:
        return"invalid factorial: this number is negative number"
    elif (n==0):
        return 1
    else:
        result=1
        for i in range(1,n+1):
            result *= i
        return result
user_input=int(input("enter a non negative number "))
result=factorial_with_validatio(user_input)
print(result)