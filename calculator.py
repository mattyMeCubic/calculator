import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create labels and entry fields for user input
        self.label1 = tk.Label(master, text="Enter first number:")
        self.label1.pack()
        self.entry1 = tk.Entry(master)
        self.entry1.pack()

        self.label2 = tk.Label(master, text="Enter second number:")
        self.label2.pack()
        self.entry2 = tk.Entry(master)
        self.entry2.pack()

        # Create buttons for user to select operation
        self.add_button = tk.Button(master, text="+", command=self.add)
        self.add_button.pack()

        self.subtract_button = tk.Button(master, text="-", command=self.subtract)
        self.subtract_button.pack()

        self.multiply_button = tk.Button(master, text="*", command=self.multiply)
        self.multiply_button.pack()

        self.divide_button = tk.Button(master, text="/", command=self.divide)
        self.divide_button.pack()

        # Create label to display result
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    # A method to get user inputs
    def get_inputs(self):
        x = float(self.entry1.get())
        y = float(self.entry2.get())
        return x, y

    # Methods to perform calculations based on user input
    def add(self):
        x, y = self.get_inputs()
        result = x + y
        self.display_result(result)

    def subtract(self):
        x, y = self.get_inputs()
        result = x - y
        self.display_result(result)

    def multiply(self):
        x, y = self.get_inputs()
        result = x * y
        self.display_result(result)

    def divide(self):
        x, y = self.get_inputs()
        result = x / y
        self.display_result(result)

    # A method to display the result of the calculation
    def display_result(self, result):
        self.result_label.config(text=f"Result: {result}")

# Create the Tkinter root window and the Calculator object
root = tk.Tk()
calculator = Calculator(root)

# Run the main event loop
root.mainloop()