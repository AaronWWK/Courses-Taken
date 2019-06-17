vowels = ['a','e','i','o','u']
lists = []
s = "This is great!"
s2= ''
for letter in str(s):
    if letter not in vowels:
        lists.append(letter)
if len(lists) == 0:
    print(' ')
else:
    for items in lists:
        s2 = s2+ items
    print(s2)
