
# Midterm Practical Exam — Pet Adoption Records Manager
#Student: Eliyah Rieluis J. De Leon #

pets = []  # starts empty — the user adds pets as the program runs


def display_menu():
    print("[Pet Adoption Records Manager]")
    print("1. Add Pets")
    print("2. View Pets")
    print("3. Available or Adopted")
    print("4. Find Pets")
    print("5. Remove Pet")
    print("6. Exit")

    choice = input("Enter number: ")
    return choice


def add_pet(pet_list):
    name = input("Enter pet name: ")
    animal_type = input("What kind of animal: ")
    status = input("Enter status (Available or Adopted): ")

    pet = f"{name} | {animal_type} | {status}"
    pet_list.append(pet)

    print("Added successfully!")


def view_pets(pet_list):
    if len(pet_list) == 0:
        print("No pets found.")
    else:
        print("\n=== Pet Records ===")

        for pet in pet_list:
            print(pet)


def count_available_adopted(pet_list):
    available = 0
    adopted = 0

    for pet in pet_list:
        if "Available" in pet:
            available += 1
        elif "Adopted" in pet:
            adopted += 1

    return available, adopted


def find_pet(pet_list):
    search_name = input("Enter pet name: ")

    found = False

    for pet in pet_list:
        if pet.lower().startswith(search_name.lower() + " |"):
            print("Pet found:", pet)
            found = True
            break

    if not found:
        print("Pet not found.")


# bons
def remove_pet(pet_list):
    search_name = input("Enter pet name to remove: ")

    for pet in pet_list:
        if pet.lower().startswith(search_name.lower() + " |"):
            pet_list.remove(pet)
            print("Pet removed successfully!")
            return

    print("Pet not found.")




main()