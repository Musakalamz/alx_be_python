def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []   # required list

    while True:
        display_menu()   # required call

        choice = input("Enter your choice: ")  # input for choice

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} added.")

        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed.")
            else:
                print("Item not found.")

        elif choice == '3':
            if len(shopping_list) == 0:
                print("Shopping list is empty.")
            else:
                print("Current Shopping List:")
                for item in shopping_list:
                    print(item)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
