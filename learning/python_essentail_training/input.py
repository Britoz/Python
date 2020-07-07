#store input to variable
name = input("Enter your name: ")

print("hello " + name)
#about list in python
friends = ["vinh", "the", "lee"]
ages = [11,12,13]
friends.extend(ages)
#append one more item
friends.append("heel")
#insert by index
friends.insert(2,"hello")
#remove item in list
friends.remove("hello")
#clear() is used to clear all item
#pop() is used to get rip of last element
#sort list

ages.sort()
ages.reverse()
friends.extend(ages)
friends_copy = friends.copy()
print(friends[3])
print(friends[-1])
print(friends[1:])
print(friends[1:3])
print(friends.index("heel"))
print(friends.count("heel"))