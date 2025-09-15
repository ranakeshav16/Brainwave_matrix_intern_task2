# Inventory Management System

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, quantity, price):
        if product_id in self.products:
            print("❌ Product ID already exists!")
        else:
            self.products[product_id] = {
                "name": name,
                "quantity": quantity,
                "price": price
            }
            print(f"✅ Product '{name}' added successfully.")

    def edit_product(self, product_id, name=None, quantity=None, price=None):
        if product_id in self.products:
            if name:
                self.products[product_id]["name"] = name
            if quantity is not None:
                self.products[product_id]["quantity"] = quantity
            if price is not None:
                self.products[product_id]["price"] = price
            print("✅ Product updated successfully.")
        else:
            print("❌ Product not found!")

    def delete_product(self, product_id):
        if product_id in self.products:
            deleted = self.products.pop(product_id)
            print(f"🗑️ Product '{deleted['name']}' deleted successfully.")
        else:
            print("❌ Product not found!")

    def view_inventory(self):
        if not self.products:
            print("📦 Inventory is empty.")
        else:
            print("\n--- Inventory List ---")
            for pid, details in self.products.items():
                print(f"ID: {pid}, Name: {details['name']}, "
                      f"Qty: {details['quantity']}, Price: {details['price']}")
            print("----------------------")

    def track_low_stock(self, threshold=5):
        print(f"\n⚠️ Products with stock below {threshold}:")
        low_stock = False
        for pid, details in self.products.items():
            if details["quantity"] < threshold:
                print(f"ID: {pid}, Name: {details['name']}, Qty: {details['quantity']}")
                low_stock = True
        if not low_stock:
            print("✅ No products are low in stock.")


# Menu-driven program
def main():
    inventory = Inventory()
    
    while True:
        print("\n--- Inventory Management System ---")
        print("1. Add Product")
        print("2. Edit Product")
        print("3. Delete Product")
        print("4. View Inventory")
        print("5. Track Low Stock")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            pid = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            qty = int(input("Enter Quantity: "))
            price = float(input("Enter Price: "))
            inventory.add_product(pid, name, qty, price)

        elif choice == "2":
            pid = input("Enter Product ID to edit: ")
            name = input("New Name (leave blank to keep same): ")
            qty = input("New Quantity (leave blank to keep same): ")
            price = input("New Price (leave blank to keep same): ")

            inventory.edit_product(
                pid,
                name if name else None,
                int(qty) if qty else None,
                float(price) if price else None
            )

        elif choice == "3":
            pid = input("Enter Product ID to delete: ")
            inventory.delete_product(pid)

        elif choice == "4":
            inventory.view_inventory()

        elif choice == "5":
            threshold = input("Enter stock threshold (default 5): ")
            threshold = int(threshold) if threshold else 5
            inventory.track_low_stock(threshold)

        elif choice == "6":
            print("👋 Exiting Inventory System. Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
