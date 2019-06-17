s = 'azcbobobegghakl'

# print('a'<'b')   True

strings_longest = ''
strings_tem = ''
for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        strings_tem += s[i+1]
        if len(strings_tem) > len(strings_longest):
            strings_longest = strings_tem
    #else:



print('Longest substring in alphabetical order is:',strings_longest)
