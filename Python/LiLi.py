listy = []

for i in range(21):
  listy.append(i**2)
  

misty = [i**2 for i in range(21)]
  
# print(listy)
# print(misty)

s = "osamaIQbudn wiwBUBus"

vow_isty = set()
vowwa_sml = {i for i in s if i in "aeiouAEIOU"}

for i in s:
  if i in "aeiouAEIOU":
    vow_isty.add(i)
    
# print(vow_isty)
# print(vowwa_sml)

s = "muah wuah cuis iormun aowi kfjg"
dicti = {}

s = s.split()

for i in s:
  dicti[i] = len(i)
  
sml_dict = {}

  
print(dicti)