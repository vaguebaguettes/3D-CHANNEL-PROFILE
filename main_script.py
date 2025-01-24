import csv
import tkinter as tk
from tkinter import messagebox, filedialog

class UserInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("User Information")

        self.name_label = tk.Label(root, text="Name")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        self.age_label = tk.Label(root, text="Age")
        self.age_label.pack()
        self.age_entry = tk.Entry(root)
        self.age_entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_info)
        self.submit_button.pack()

        self.save_button = tk.Button(root, text="Save", command=self.save_info)
        self.save_button.pack()

        self.user_info = []

    def submit_info(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        if name and age:
            try:
                age = int(age)
                self.user_info.append((name, age))
                self.name_entry.delete(0, tk.END)
                self.age_entry.delete(0, tk.END)
                messagebox.showinfo("Success", "User information added.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid age.")
        else:
            messagebox.showerror("Error", "Please enter both name and age.")

    def save_info(self):
        if not self.user_info:
            messagebox.showerror("Error", "No information to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                 filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if file_path:
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Age"])
                writer.writerows(self.user_info)
            messagebox.showinfo("Success", f"Information saved to {file_path}")
            self.user_info = []

if __name__ == "__main__":
    root = tk.Tk()
    app = UserInfoApp(root)
    root.mainloop()
