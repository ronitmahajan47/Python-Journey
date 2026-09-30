#Removal of dublication from a List

myList = ["a","b","a","c","b"]

newList = list(dict.fromkeys(myList))

print(newList)