from itertools import count


string = input("Enter word: ")
char = input("Enter a character: ")
count = 0
for i in range(len(string)):
    if(string[i]==char):
        count = count+1
print("Number is: ", count)