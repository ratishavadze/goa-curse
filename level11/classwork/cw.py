
input_data = {} 

for label in ['სახელი', 'ასაკი']:
    value = input(f"{label} შეიყვანეთ: ")
    input_data[label] = value

print(f"\nმომხმარებლის მონაცემები:")
for id, name in input_data.items():
    print(f"{id}: {name}")

