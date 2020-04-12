my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    }
}

for (relationship, info) in my_family.items():
    print(f'{my_family[relationship]["name"]} is my {relationship} and is {my_family[relationship]["age"]} years old.')
