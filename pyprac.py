# age = int(input("What's your age?"))

# if age >= 18:
#     print ("Access allowed")
# elif age < 18 and age > 0:
#     print("Access not allowed")
# else:
#     print("Invalid age")    

my_list = [1, 2, 3, "python", 67, [4, 5]]

for j in my_list:
    print j

    # create a dictionary
person = {
            "name": "Amos",
            "age": 23,
            "hobbies": ["Travelling", "Swimming", "Coding", "Music"]
        }

# iterate through the dict and print the keys
for key in person:
    print(key)

# iterate through the dict's keys and print their values
for key in person:
    print(person[key])