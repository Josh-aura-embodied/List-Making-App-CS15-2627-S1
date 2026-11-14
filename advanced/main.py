
def display_list(items, title):
    print(f"--- {title} ---")

    if len(items) == 0:
        print("This list is empty.")
    else:
        for index in range(len(items)):
            print(f"{index}: {items[index]}")


def display_both_lists(todo_list, completed_list):
    display_list(todo_list, "TO-DO LIST")
    display_list(completed_list, "COMPLETED LIST")


def main():
    todo_list = []
    completed_list = []
    previous_state = None

    while True:
        print("= IMPROVED TO-DO LIST =")
        print("1. Add an Item")
        print("2. Remove an Item")
        print("3. Display the Lists")
        print("4. Undo Previous Change")
        print("5. Replace an Item")
        print("6. Check an Item Off")
        print("7. View a Specific List")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            new_item = input("Enter the item you want to add: ").strip()

            if new_item == "":
                print("You cannot add an empty item.")
            else:
                previous_state = (
                    todo_list.copy(),
                    completed_list.copy()
                )

                todo_list.append(new_item)
                print(f"'{new_item}' has been added.")

        elif choice == "2":
            display_list(todo_list, "TO-DO LIST")

            if len(todo_list) > 0:
                try:
                    index = int(input("Enter the index of the item to remove: "))

                    if 0 <= index < len(todo_list):
                        previous_state = (
                            todo_list.copy(),
                            completed_list.copy()
                        )

                        removed_item = todo_list.pop(index)
                        print(f"'{removed_item}' has been removed.")
                    else:
                        print("Invalid index. Please try again.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "3":
            display_both_lists(todo_list, completed_list)

        elif choice == "4":
            if previous_state is not None:
                todo_list = previous_state[0].copy()
                completed_list = previous_state[1].copy()
                previous_state = None

                print("Your previous change has been undone.")
            else:
                print("There is no change to undo.")

        elif choice == "5":
            display_list(todo_list, "TO-DO LIST")

            if len(todo_list) > 0:
                try:
                    index = int(input("Enter the index of the item to replace: "))

                    if 0 <= index < len(todo_list):
                        new_item = input("Enter the replacement item: ").strip()

                        if new_item == "":
                            print("The replacement cannot be empty.")
                        else:
                            previous_state = (
                                todo_list.copy(),
                                completed_list.copy()
                            )

                            old_item = todo_list[index]
                            todo_list[index] = new_item

                            print(f"'{old_item}' has been replaced with '{new_item}'.")

                    else:
                        print("Invalid index. Please try again.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "6":
            display_list(todo_list, "TO-DO LIST")

            if len(todo_list) > 0:
                try:
                    index = int(input("Enter the index of the completed item: "))

                    if 0 <= index < len(todo_list):
                        previous_state = (
                            todo_list.copy(),
                            completed_list.copy()
                        )

                        completed_item = todo_list.pop(index)
                        completed_list.append(completed_item)

                        print(f"'{completed_item}' has been marked as completed.")

                    else:
                        print("Invalid index. Please try again.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "7":
            print("Which list would you like to view?")
            print("1. To-Do List")
            print("2. Completed List")

            view_choice = input("Enter your choice: ").strip()

            if view_choice == "1":
                display_list(todo_list, "TO-DO LIST")
            elif view_choice == "2":
                display_list(completed_list, "COMPLETED LIST")
            else:
                print("Invalid choice. Please select 1 or 2.")

        elif choice == "8":
            print("Thank you for using the aura kings improved To-Do List!")
            break

        else:
            print("Invalid menu choice. Please select 1-8.")


if __name__ == "__main__":
    main()
