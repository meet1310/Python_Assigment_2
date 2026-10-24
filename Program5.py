import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name == "" or phone == "" or email == "":
        messagebox.showwarning("Warning", "Please enter all details")
        return

    contact = (len(contacts) + 1, name, phone, email)
    contacts.append(contact)

    messagebox.showinfo("Success", "Contact added successfully")

    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

def show_contacts():
    output.delete("1.0", tk.END)

    for contact in contacts:
        output.insert(tk.END, str(contact) + "\n")

window = tk.Tk()
window.title("Contact Manager")
window.geometry("450x400")

tk.Label(window, text="Name").pack()
name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Phone").pack()
phone_entry = tk.Entry(window)
phone_entry.pack()

tk.Label(window, text="Email").pack()
email_entry = tk.Entry(window)
email_entry.pack()

tk.Button(window, text="Add Contact", command=add_contact).pack(pady=10)
tk.Button(window, text="Show Contacts", command=show_contacts).pack()

output = tk.Text(window, height=10, width=50)
output.pack(pady=10)

window.mainloop()