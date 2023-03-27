person = {"name": " Anik", "age": 23, "profession": "Data Engineer"}
for key in person:
    p = f"Key of the dictionary is {key} and the value of dictionary is {person[key]}"
    print(p)
for value in person.values():
    print(f"the actual values of the dictionary is {value}")

for key_value_pair in person.items():
    print(key_value_pair)