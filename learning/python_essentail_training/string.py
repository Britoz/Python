
name = "The Vinh Ly"
age = 26
isMale = True


print("hello \"" + name + "\" and your age is ")

#using lower() to Lower the string
print("using lower case: " + name.lower())
#using upper() to Upper the string
print("using upper case: " + name.upper())
#using isupper() and islower() to checking upper or lower case with output is true or false
#checking the length of the string by using len(string)
#__str__() is used to convert object to string
print("Your name size is: " + len(name).__str__())
#get 1 character
print(name[0])
#so, by using name[0] we are calling character 0 in the string name
#replace one string to another string
print(name.replace("Ly", "Lee"))