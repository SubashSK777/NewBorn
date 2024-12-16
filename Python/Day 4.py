# x = int(input("Enter a Number: "))
# y = int(input("Enter another Number: "))

# oper = int(input("""Select an Operation to Perform:
# 1. Addition
# 2. Subtraction
# 3. Exit
# Your choice: """))

# if oper == 1:
#     print(f"The Sum of the two numbers is {x + y}")
# elif oper == 2:
#     print(f"The Difference of the two numbers is {x - y}")
# elif oper == 3:
#     print("Exiting the program.")
# else:
#     print("Invalid choice. Please try again.")


n = int(input("Enter a Number: "))

for i in range(11):
  print(f"{n} x {i} = {i*n}")