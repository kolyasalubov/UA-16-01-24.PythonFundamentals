# 3 Interchanging the values of two variables without using the third one

first_var = input("Enter the 1st variable: ")
second_var = input("Enter the 2nd variable: ")
print("=====================================")
print(f"Before interchange: \nFirst variable is: {first_var}.\nSecond variable is: {second_var}")
first_var, second_var = second_var, first_var
print("====== INTERCHANGING ======")
print(f"After interchange: \nFirst variable is: {first_var}.\nSecond variable is: {second_var}")
print("=====================================")
