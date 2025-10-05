# Part II: 
#4. menu_editor.py 
from menu_item import MenuItem
from menu_manager import MenuManager
import sys

def add_item_to_menu():
    print("\n--- Add New Item ---")

    item_name = input("Enter item name: ").strip()
    if not item_name:
        print("Item name cannot be empty. Aborting.")
        return

    item_price = None
    while True:
        try:
            price_input = input("Enter item price (whole number): ").strip()
            item_price = int(price_input)
            if item_price < 0:
                print("Price must be zero or positive.")
                continue
            break
        except ValueError:
            print("Invalid input. Price must be a whole number (integer).")

    try:
        item = MenuItem(item_name, item_price)
        if item.save():
            print(f"\nSUCCESS: Item '{item_name}' was added successfully.")
        else:
            print(f"\nERROR: Failed to add item '{item_name}'.")

    except ValueError as e:
        print(f"\nERROR: Could not create item. {e}")
    except Exception as e:
        print(f"\nAN UNEXPECTED ERROR OCCURRED: {e}")


def remove_item_from_menu():
    print("\n--- Remove Item ---")
    item_name = input("Enter the name of the item to remove: ").strip()

    if not item_name:
        print("Item name cannot be empty. Aborting.")
        return

    try:
        item = MenuItem(item_name, 0)

        if item.delete():
            print(f"\nSUCCESS: Item '{item_name}' was deleted successfully.")
        else:
            print(f"\nFAILURE: Item '{item_name}' could not be deleted or was not found in the menu.")

    except ValueError:
        print("\nERROR: Invalid item name provided.")
    except Exception as e:
        print(f"\nAN UNEXPECTED ERROR OCCURRED: {e}")


def update_item_from_menu():
    print("\n--- Update Item ---")
    original_name = input("Enter the CURRENT name of the item you want to update: ").strip()

    if not original_name:
        print("Item name cannot be empty. Aborting.")
        return

    existing_item = MenuManager.get_by_name(original_name)
    if not existing_item:
        print(f"\nERROR: Item '{original_name}' not found in the menu. Cannot update.")
        return

    print(f"Current Item: {existing_item.name}, Price: {existing_item.price:.2f} DH")

    new_name = input("Enter NEW name (leave blank to keep current): ").strip() or None

    new_price = None
    while True:
        price_input = input("Enter NEW price (leave blank to keep current): ").strip()
        if not price_input:
            break
        try:
            price_int = int(price_input)
            if price_int < 0:
                print("Price must be zero or positive.")
                continue
            new_price = price_int
            break
        except ValueError:
            print("Invalid input. Price must be a whole number (integer).")

    try:
        if existing_item.update(new_name, new_price):
            print(f"\nSUCCESS: Item '{original_name}' was updated successfully.")
        else:
            print(f"\nFAILURE: Item '{original_name}' could not be updated (no changes or database error).")
    except Exception as e:
        print(f"\nAN UNEXPECTED ERROR OCCURRED during update: {e}")


def show_restaurant_menu():
    items = MenuManager.all_items()
    print("\n" + "="*40)
    print("      RESTAURANT MENU")
    print("="*40)

    if not items:
        print("The menu is currently empty or database connection failed.")
        print("="*40)
        return

    max_name_len = max(len(item.name) for item in items)

    print(f"| {'Item Name':<{max_name_len}} | {'Price':>6} |")
    print("-" * (max_name_len + 12))

    for item in items:
        price_str = f"{item.price:.2f} DH"
        print(f"| {item.name:<{max_name_len}} | {price_str:>6} |")

    print("="*40)


def show_user_menu():
    while True:
        print("\n=== Restaurant Menu Manager ===")
        print("V - View an Item")
        print("A - Add an Item")
        print("D - Delete an Item")
        print("U - Update an Item")
        print("S - Show the Full Menu")
        print("X - Exit")
        print("=============================")

        choice = input("Enter your choice: ").upper().strip()

        if choice == 'V':
            item_name = input("Enter the name of the item to view: ").strip()
            if not item_name:
                print("Item name cannot be empty.")
                continue
            item = MenuManager.get_by_name(item_name)
            if item:
                print(f"\nItem Found: {item.name}, Price: {item.price:.2f} DH")
            else:
                print(f"\nItem '{item_name}' not found.")
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'X':
            print("\nExiting program...")
            show_restaurant_menu() 
            sys.exit(0)
        else:
            print("Invalid choice. Please enter V, A, D, U, S, or X.")

if __name__ == '__main__':
    show_user_menu()