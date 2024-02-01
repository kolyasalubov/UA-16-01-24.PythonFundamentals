
# variant 1
# num = input("Entered your number: ")
# factorial = 1


# while 1 < num:
#  factorial *= num
#  num -= 1
# print(factorial)

# # variant 2
n = int(input("Entered your number: "))
f = 1
if isinstance(n,int) and 0 <=0:
 for item in range(2, n+1):
    f *= item
    print (f"{item}! {f}")

 else:
    print ("Number is not intenger")    