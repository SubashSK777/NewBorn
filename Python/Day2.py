# from datetime import date

# print("Today's Date is: " + str(date.today()))

# print("")
# print ("=======================================================")
# print("")

# # print("Welcome to the greeter program")
# # name = input("Enter your name: ")
# # print("Greetings " + name)

# print("")
# print ("=======================================================")
# print("")

# a = 27
# b = 93
# if a < b:
#     print("a is less than b")
# elif a > b:
#     print("a is greater than b")
# else: 
#     print ("a is equal to b")
    
# print("")
# print ("=======================================================")
# print("")

# a = 27
# b = 93
# c = 380

# if a > b:
#   print("a is Greatest")
  
#   if a > c:
#     print("a is the Greatest")
    
#   else:
#     print("c is the Greatest")

# elif b > c:
#   print("b is the Greatest")
  
# else:
#   print("c is the Greatest")
  
# print("")
# print ("=======================================================")
# print("")

# fact = "The Moon has no atmosphere. "
# fact += "No sound can be heard on the Moon."
# print(fact)

# print("")
# print ("=======================================================")
# print("")

# print("temperatures and facts about the moon".title())  

# print("")
# print ("=======================================================")
# print("")

# temperatures = "Alakazambarkadabradubaididubidiadumwiaht"
# temperatures_list = temperatures.split("a")
# print(temperatures_list)

# print("")
# print ("=======================================================")
# print("")

# print("Moon" in "This text will describe facts about the Moon")

# print("")
# print ("=======================================================")
# print("")

# text = "This text will describe facts aboutMoonthe Moon"
# count = text.count("Moon")
# print(count)

# print("")
# print ("=======================================================")
# print("")

# temperatures = "Alakazambarkadabradubaididubidiadumwiaht"
# temperatures_list = temperatures.split("a")
# print(temperatures)
# print(temperatures_list[2:2:])

# print("")
# print ("=======================================================")
# print("")

# name = ["SubashKumarK", "Kennedy", "John", "Marcus", "Killer"]

# for person in name:
#   if "k" in person.lower():  
#       print(person)

# print("")
# print ("=======================================================")
# print("")

# temperatures = "Mars Average Temperature is 60 C"
# for parts in temperatures.split():
#   if parts.isnumeric():
#     print(parts)

text1 = str(input("Enter a String: "))
text2 = str(input("Enter another String: "))

char1 = sorted(list(text1.islower()))
char2 = sorted(list(text2.islower()))

if char1 == char2:
  print ("It is an Anagram")
else:
  print ("It is not an Anagram")