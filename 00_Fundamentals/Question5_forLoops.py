string1 = "aabbcsdw"
string2 = "abbbcsdd"

# Write your code here.
for x,y in enumerate(string1):
    if y == string2[x]:
        print(y)

for i in range(len(string1)):
    if string1[i] == string2[i]:
        print(string1[i])