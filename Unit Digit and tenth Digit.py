#Unit digit
#This is mostly used for strings
a=input()
print (a[len(a)-1])

#For Integer Unit digit
num=int(input("enter a number:"))
print(num%10)

#Tenth Digit
num=int(input("enter a number:"))
num = num//10
print(num%10)

#Hundreth Digit#Tenth Digit
num=int(input("enter a number:"))
num = num//100
print(num%10)
