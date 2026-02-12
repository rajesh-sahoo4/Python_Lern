# pratice  qustion of string , list and dictanary
lst = [10, 20, 30, 20, 40]
# Add value 50 at the end of the list.
lst.append(50)
print(lst)

# 2️⃣ Insert 15 at index 1.
lst.insert(1,15)
print(lst)

# 3️⃣ Remove the first occurrence of 20.
lst.remove(20)
print(lst)

# 4️⃣ Count how many times 20 appears.
print(lst.count(20))


# 5️⃣ Find index of value 30.
print(lst.index(30))

# 6️⃣ Reverse the list.
lst.reverse()
print(lst)

# 7️⃣ Sort the list in ascending order.
lst.sort()
print(lst)

tup = (5, 10, 15, 10, 20)
# 8. Count how many times 10 appears in the tuple.
print(tup.count(10))

# 9. Find index of value 15.
print(tup.index(15))
# 10.  Convert tuple into a list.
l=list(tup)
print(l)
# 11. Find length of tuple.
print(len(tup))
dct = {"name": "Ram", "age": 25, "city": "Delhi"}
# 12. Get the value of key "name".
print(dct.get("name"))
# 13.  Add a new key "country" with value "India".
dct['country']='India'
print(dct)
# 14.  Update "age" to 26.
dct["age"]="26"
print(dct)
# 15. Remove key "city".
dct.pop('city')
print(dct)
# 16. Get all keys from dictionary.
print(dct.keys())
# 17. Get all values from dictionary.
print(dct.values())
s = " python is very easy "
# 18. Remove extra spaces from both ends.
print(s.strip(" "))
# 19.  Convert string to uppercase.
print(s.upper())
# 20. Count how many times "is" appears.
print(s.count('is'))
# 21. Replace "easy" with "simple".
print(s.replace("easy","simple"))
# 22.Split the string into words.
print(s.split())


