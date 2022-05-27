print("Love Calculator")

name1 = input(" What is your name: \n").lower()
name2 = input("What is their name: \n").lower()

combined_string = name1 + name2

convert_to_characters = list(combined_string)

t = convert_to_characters.count('t')
r = convert_to_characters.count('r')
u = convert_to_characters.count('u')
e = convert_to_characters.count('e')
total1 = int(t + r + u + e)
print(total1)

l = convert_to_characters.count('l')
o = convert_to_characters.count('o')
v = convert_to_characters.count('v')
e = convert_to_characters.count('e')
total2 = int(l + o + v + e)
print(total2)
combined_total = str(total1) + str(total2)
love_score = int(combined_total)

if love_score > 40:
    print("Compatible")
else:
    print("Sorry not compatible")
