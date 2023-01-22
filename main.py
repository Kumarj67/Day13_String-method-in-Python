#String Methods
a="Jeetesh"
print(len(a))
#strings are Immutable it means original string doesnot change if we apply any string methos
print(a.upper())
print(a)
print(a.lower())
print(a)

#strip method only strip tail path not head path
b="harry!!!!!"
print(b.rstrip("!"))
c="!!!harry"
print(c.rstrip("!"))

print(a.replace("Jeetesh","Harry"))
print(a)

#split method split the given string at the specified instances and returns the seperated string as a list item

d="!Harry!!! !!!!! Harry"
print(d.split())

#Capitalize() method
#this method change the first character to capital and rest all to lower 
blogHeading="introduction to Python"
print(blogHeading.capitalize()) 

#center method
str="welcometotheconsoleto"
print(len(str))
print(str.center(50))

#count Method
print(d.count("Harry"))

#endwith method

print(str.endswith("console"))

print(str.endswith("to",3,10))

#find method-find first occurance of the given condition and return index of ist occurance

print(str.find("top"))
print(str.index("to"))

#index method also search the ist occurance of given string if it is absent then it throws an exception



print(str.index("to"))

#isalnum() method return is a string alphanumeric or not
#consist of A-Z a-z and 0-9
str1="45abc"
print(str1.isalnum())
print(str.isalnum())

#isalpha() method return true is string contans A-Z and a-z other than that if it contains 0-9 it returnb False
print(str1.isalpha())
print(str.isalpha())

#islower method

print(str.islower())
print(a.islower())

#isprintable() method return true if all the given values in string are printable and if it is not then returns false.not printable character are "\n"
e="harry\n"
print(str.isprintable())
print(e.isprintable())
#isspace() m ethod
print(str.isspace())
f=" "
print(f.isspace())

#istitle() method returns true onlu if first letter is capital in a string and it returns false if it doesnot contains capital ist letter in a string

print(a.istitle())
print(e.istitle())

#stratswith() method
print(blogHeading.startswith("introduction"))

#swapcase() method changes caseing upper case to lower and lower case to upper
print(blogHeading.swapcase())

#title() method makes each word first letter in capital of a given string

print(blogHeading.title())















































