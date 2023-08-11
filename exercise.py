# 1
names = ["Muhangi", "susan", "Duncan", "Davis", "Everest"]
print(names[1])

# 2
names =["Muhangi", "susan", "Duncan", "Davis", "Everest"]
names[0] = "Museveni"
print(names)

# 3
names = ["Muhangi", "susan", "Duncan", "Davis", "Everest"]
names.append("Jannet")
print(names)

# 4
names = ["Muhangi", "susan", "Duncan", "Davis", "Everest"]
names.insert(2, "Bathel")
print(names)

# 5
names = ["Muhangi", "susan", "Duncan", "Davis", "Everest"]
del names[3]
print(names)

# 6
names = ["Muhangi", "susan", "Duncan", "Davis", "Everest"]
print(names[-1])

# 7
new_list = [10, 20, 30, 40, 50, 60, 70]
print(new_list[2:5])

# 8
countries = ["India", "China", "United States", "United Kingdom", "France"]

copy_of_countries = countries.copy()

print("The copy of the countries list is:", copy_of_countries)

# 9
countries = ["India", "China", "United States", "United Kingdom", "France"]
for country in countries:
    print(country)

# 10

animals = ["dog", "cat", "mouse", "bird", "fish"]

animals.sort(reverse=True)

print("The animals in descending order are:", animals)

animals.sort()

print("The animals in ascending order are:", animals)

#11
animals_with_a = []

for animal in animals:
    if "a" in animal:
        animals_with_a.append(animal)

print("The animal names with the letter ‘a’ in them are:", animals_with_a)
# 12
first_names = ["arinaitwe", "John"]
second_names = ["Eliod", "Doe"]

full_names = first_names + second_names

print("The full names are:", full_names)
# Exercise 2
# 1 
x = ("samsung", "iphone", "tecno", "redmi")
fav_phone = "iphone"
for item in x:
    if item == fav_phone:
     print(item) 

#2
x = ("samsung", "iphone", "tecno", "redmi")
print(x[-2])  

#3
x = ("samsung", "iphone", "tecno", "redmi")
x = list(x)
x[x.index("iphone")] = "itel"
x = tuple(x)
print(x) 
#alternative
x = ("samsung", "iphone", "tecno", "redmi")
updated_x = tuple("itel" if phone == "iphone" else phone for phone in x)
print(updated_x)
print("---------------------------------------")
 
#4
x = ("samsung", "iphone", "tecno", "redmi")
x = x + ("Huawei",)
print(x) 

#5
x = ("samsung", "iphone", "tecno", "redmi")
for phone in x:
    print(phone)
    
length = len(x)
i= 0
while i<length:
    print(phone)
    i+=1

#6
x = ("samsung", "iphone", "tecno", "redmi")
x = x[1:]
print(x) 
 
#7
cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara"])
print(cities)

#8
kampala, entebbe, jinja, mbra = cities
print(kampala)  
print(entebbe) 
print(jinja)  
print(mbra)

#9
cities = ("Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu")
print(cities[1:4])  

#10
first_names = ("John", "Jane", "Michael", "Emily")
last_names = ("Doe", "Smith", "Johnson", "Brown")
full_names = first_names + last_names
print(full_names)

#11
colors = ("red", "green", "blue")
new_colors = colors * 3
print(new_colors)

#12
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count = thistuple.count(8)
print(count)  

print("\n")
print("Exercise 3")
print("\n")

#Exercise 3
#1
beverages = set(["coffee", "juice", "chocolate"])
print(beverages)

#2
beverages = set(["coffee", "juice", "chocolate"])
beverages.add("water")
beverages.update(["soda", "smoothie"])
print(beverages)

#3
mySet = {"oven", "kettle", "microwave", "refrigerator"}

#4
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set.")
else:
    print("Microwave is not present in the set.")
    
    
 #alternative   
for x in mySet:
    if x == "microwave":
        print("Microwave is present in the set")

#5
mySet = {"oven", "kettle", "microwave", "refrigerator"}
for item in mySet:
    print(item)

#6
mySet = {1, 2, 3, 4}
myList = [5, 6]
mySet.update(myList)
print(mySet)


#7
ages = {25, 30, 35}
names = {"John", "Jane", "Michael"}
combined_set = ages.union(names)
print(combined_set)

#Alternative
ages = {25, 30, 35}
names = {"John", "Jane", "Michael"}
combined_set = ages | names
print(combined_set)

print("\n")
print("_____Exercisesss 4_____")
print("\n")


# 1
num = 10
text = "Hello"
concatenated = f"{num}{text}"
print(concatenated)

#2
txt = " Hello, Uganda! "
trimmed = "".join(txt.split())
print(trimmed)

#3
txt = "Hello, Uganda!"
uppercase_txt = txt.upper()
print(uppercase_txt)

#4
txt = "Hello, Uganda!"
replaced_txt = txt.replace('U', 'V')
print(replaced_txt)

#5
y = "I am proudly Ugandan"
range_of_chars = y[1:4]
print(range_of_chars)

#6
x = 'All "Data Scientists" are cool!'
print(x)

#Exercise five

#1 
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(Shoes["size"])

#2
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
Shoes["brand"] = "Adidas"
print(Shoes)

#3
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
Shoes["type"] = "sneakers"
print(Shoes)

#4
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
keys_list = list(Shoes.keys())
print(keys_list)

#5
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
values_list = list(Shoes.values())
print(values_list)

#6
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
if "size" in Shoes:
    print("The key 'size' exists in the dictionary.")
else:
    print("The key 'size' does not exist in the dictionary.")

#7
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
for key, value in Shoes.items():
    print(key, ":", value)

#8
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
Shoes.pop("color")
print(Shoes)

#9
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
Shoes.clear()
print(Shoes)

#10
my_dict = {"name": "John", "age": 30, "city": "New York"}
copy_dict = my_dict.copy()
print(copy_dict)

#11
students = {
    "John": {"age": 25, "major": "Computer Science"},
    "Jane": {"age": 23, "major": "Mathematics"},
    "Michael": {"age": 27, "major": "Physics"}
}
for student, info in students.items():
    print(student)
    for key, value in info.items():
        print(key, ":", value)
    print()

