#exercise3
#Exercise 3: Print characters from a string that are present at an even index number

#here is code where it will ask the user a word.
input = input('Enter a word:')

#this code shows the user what they inputed.
print("the word is", input)

#this code gets the lenght of the string.
size = len(input)

#this code serves as the result.
print("printing only in odd pattern")

for i in range (0, size -1, 2):
    print("[",i,"]", input[i])