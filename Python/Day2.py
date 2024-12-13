from datetime import date

print("Today's Date is: " + str(date.today()))

print("")
print ("=======================================================")
print("")

# print("Welcome to the greeter program")
# name = input("Enter your name: ")
# print("Greetings " + name)

print("")
print ("=======================================================")
print("")

a = 27
b = 93
if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else: 
    print ("a is equal to b")
    
print("")
print ("=======================================================")
print("")

a = 27
b = 93
c = 380

if a > b:
  print("a is Greatest")
  
  if a > c:
    print("a is the Greatest")
    
  else:
    print("c is the Greatest")

elif b > c:
  print("b is the Greatest")
  
else:
  print("c is the Greatest")