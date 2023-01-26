str1 = ['kriti', 'Kumari']

lstr = str1[0]
for i in range(0, len(str1)):
    if(len(str1[i]) > len(lstr)):
        lstr = str1[i]
print(lstr)