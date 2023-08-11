#importing the tinker library for displaying the window
import tkinter as tk

# Define the abstract class Receipt
class Receipt:
    def __init__(self, item, price, quantity):
        self.item = item
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity

# Define the  class Receipt
class Receipt(Receipt):
    def __init__(self, item, price, quantity, tax_rate):
        super().__init__(item, price, quantity)
        self.tax_rate = tax_rate

    def get_total(self):
        total = super().get_total()
        tax = total * self.tax_rate
        return total + tax

# Define the main window
root = tk.Tk()
root.title("Receipt Printer")
root.geometry("400x400")

# Define the add_item() function
def add_item():
    item = item_entry.get()
    price = float(price_entry.get())  # Convert to float
    quantity = int(quantity_entry.get())  # Convert to int
    tax_rate = float(tax_rate_entry.get())  # Convert to float

    receipt = Receipt(item, price, quantity, tax_rate)
    total = receipt.get_total()

    total_entry.delete(0, tk.END)
    total_entry.insert(0, str(total))

# Define the print_receipt() function
def print_receipt():
    item = item_entry.get()
    price = float(price_entry.get())  # Convert to float
    quantity = int(quantity_entry.get())  # Convert to int
    tax_rate = float(tax_rate_entry.get())  # Convert to float

    receipt = Receipt(item, price, quantity, tax_rate)
    total = receipt.get_total()

    receipt_string = f"Receipt\n"
    receipt_string += f"Item\tPrice\tQuantity\tTotal\n"
    receipt_string += f"{item}\t{price}\t{quantity}\t{total}\n"

    print(receipt_string)

# Create the labels
item_label = tk.Label(root, text="Item")
price_label = tk.Label(root, text="Price")
quantity_label = tk.Label(root, text="Quantity")
tax_rate_label = tk.Label(root, text="Tax Rate")
total_label = tk.Label(root, text="Total")

# Create the entry boxes
item_entry = tk.Entry(root)
price_entry = tk.Entry(root)
quantity_entry = tk.Entry(root)
tax_rate_entry = tk.Entry(root)
total_entry = tk.Entry(root)

# Create the buttons
add_button = tk.Button(root, text="Add Item", command=add_item)
print_button = tk.Button(root, text="Print Receipt", command=print_receipt)

   # Add the widgets to the window
item_label.grid(row=0, column=0)
price_label.grid(row=1, column=0)
quantity_label.grid(row=2, column=0)
tax_rate_label.grid(row=3, column=0)
total_label.grid(row=4, column=0)

item_entry.grid(row=0, column=1)
price_entry.grid(row=1, column=1)
quantity_entry.grid(row=2, column=1)
tax_rate_entry.grid(row=3, column=1)
total_entry.grid(row=4, column=1)

add_button.grid(row=5, column=0)
print_button.grid(row=5, column=1)

# Start the main loop
root.mainloop()
