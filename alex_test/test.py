list_of_names = ["Gosho", "Tosho", "Pesho", "Stamat"]

print("====================================================")
print(list_of_names)

print(f"{', '.join(list_of_names)}") # Gosho, Tosho, Pesho, Stamat

print(f"{'\n'.join(list_of_names)}")


current_names = "Pesho Gosho Stamat"
print(', '.join(current_names.split()))  # Pesho, Gosho, Stamat
print(type(current_names.split()))