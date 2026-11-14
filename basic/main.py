
def display_list(items):
    print("- YOUR LIST -")

    if len(items) == 0:
        print("Your list is empty.")
    else:
        for index in range(len(items)):
            print(f"{index}: {items[index]}")


def main():
    items = []
    previous_list = None

    while True:
        print("= LIST MAKING APP =")
        print("1. Add an Item")
        print("2. Remove an Item")
        print("3. Display the List")
        print("4. Undo Previous Change")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            new_item = input("Enter the item you want to add: ").strip()

            if new_item == "":
                print("You cannot add an empty item.")
            else:
                previous_list = items.copy()
                items.append(new_item)
                print(f"'{new_item}' has been added.")

        elif choice == "2":
            display_list(items)

            if len(items) > 0:
                try:
                    index = int(input("Enter the index of the item to remove: "))

                    if 0 <= index < len(items):
                        previous_list = items.copy()
                        removed_item = items.pop(index)
                        print(f"'{removed_item}' has been removed.")
                    else:
                        print("Invalid index. Please try again.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "3":
            display_list(items)

        elif choice == "4":
            if previous_list is not None:
                items = previous_list.copy()
                previous_list = None
                print("Your previous change has been undone.")
            else:
                print("There is no change to undo.")

        elif choice == "5":
            print("Thank you for using the aura kings List Making App!")
            break

        else:
            print("Invalid menu choice. Please select 1-5.")


if __name__ == "__main__":
    main()
