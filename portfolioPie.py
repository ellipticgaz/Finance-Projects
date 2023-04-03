import tkinter as tk
import matplotlib.pyplot as plt

class AssetAllocationGUI:
    def __init__(self, master):
        self.master = master
        master.title("Asset Allocation")

        self.create_widgets()
    
    def create_widgets(self):
        # Create the main label
        self.main_label = tk.Label(self.master, text="Asset Allocation")
        self.main_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Create the asset input boxes
        self.asset_boxes = []
        for i in range(20):
            name_label = tk.Label(self.master, text=f"Asset {i+1} Name:")
            name_label.grid(row=i+1, column=0, padx=10, pady=5)
            amount_label = tk.Label(self.master, text="Amount:")
            amount_label.grid(row=i+1, column=1, padx=10, pady=5)
            name_entry = tk.Entry(self.master)
            name_entry.grid(row=i+1, column=2, padx=10, pady=5)
            amount_entry = tk.Entry(self.master)
            amount_entry.grid(row=i+1, column=3, padx=10, pady=5)
            self.asset_boxes.append((name_entry, amount_entry))

        # Create the submit button
        self.submit_button = tk.Button(self.master, text="Submit", command=self.show_pie_chart)
        self.submit_button.grid(row=21, column=0, columnspan=2, padx=10, pady=10)

    def show_pie_chart(self):
        # Get the asset names and amounts
        asset_names = []
        asset_amounts = []
        total_amount = 0
        for asset_box in self.asset_boxes:
            name = asset_box[0].get()
            amount = asset_box[1].get()
            if name and amount:
                asset_names.append(name)
                asset_amounts.append(float(amount))
                total_amount += float(amount)

        # Calculate the allocation percentages
        allocation_percentages = [amount/total_amount for amount in asset_amounts]

        # Plot the pie chart
        fig, ax = plt.subplots()
        ax.pie(allocation_percentages, labels=asset_names, autopct='%1.1f%%')
        ax.set_title("Asset Allocation")
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    asset_allocation_gui = AssetAllocationGUI(root)
    root.mainloop()