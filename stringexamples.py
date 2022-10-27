import tkinter as tk
i = 0
s1 = ''
s2 = "text"
block = """123"""
print(s2 * 3) #Prints s2 3 times
print(s2+s1)  #Prints s2 + s1
print(len(s2))#Prints lenght of string s2
print(s2[i])  #Prints number i in s2 (in this case, since i = 0, it prints 't')
for x in s2:i+=1 #Runs through string and increases i by 1
print("there is: ",i," numbers in i")
print(block)
"k" in s2 #Returns false, no K in s2

print(s2[-2]) #Slices 2 steps from the back of the string ex) outputs "x") 
print(s2[1:3])#Slices from 1 and 3 characters forward ex) outputs "ex" (first character is cut out)
print(s2[1:]) #Outputs all characters past the first one (character 0)
