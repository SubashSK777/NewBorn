 # txt = "wert ydfgh tyui erty fghj"
 # up_txt = txt.title()
 # print(up_txt)

# ================================================================================

# txt = "tuaascd iawoqc hsuirg sozdjn iu c"
# split_txt = txt.split('s')
# print(split_txt)

# ================================================================================

# print("Moon" not in "whatcha cha whacho cho moon ah moon")

# ================================================================================

# txt = "lorem ipsumu anyd quaapr tiwns"
# print(txt.find("Quaapr"))

# ================================================================================

# txt = "qwkdi wije oiqjp apqo qpl cnoi biout zwmomx vthi"
# print(txt.count('t'))
# print(txt.count('i'))

# ================================================================================

# print("ueg OQNS ideho josQUIH ocdjA Ocno".lower())

# print("ueg OQNS ideho josQUIH ocdjA Ocno".upper())

# print("ueg OQNS ideho josQUIH ocdjA Ocno".title())

# ================================================================================

# txt = "Today temperature at Coimbatore is : 80F"
# print(txt.split(":"))

# ================================================================================

txt = "lorem is not null its 7.0 but also 10 while all thinks its 0"
for num in txt.split():
  if num.isdecimal():
    print (num)
