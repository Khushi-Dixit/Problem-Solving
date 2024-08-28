#To swap two characters (ch1 and ch2) in a string (str)
str=input()
ch1=input()
ch2=input()
new_string = ""
for i in str:
    if i == ch1:
        new_string += ch2
    elif i == ch2:
        new_string += ch1
    else:
        new_string += i

print(new_string)    
