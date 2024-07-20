import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift if mode == 'encrypt' else ord(char) - shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

def encrypt_decrypt():
    text = input_text.get("1.0", "end-1c")
    shift = int(shift_entry.get())
    mode = mode_var.get()

    if mode not in ['encrypt', 'decrypt']:
        messagebox.showerror("Error", "Invalid mode! Please enter 'encrypt' or 'decrypt'.")
        return

    result = caesar_cipher(text, shift, mode)
    output_text.delete("1.0", "end")
    output_text.insert("end", result)

def on_enter(event=None):
    encrypt_button.configure(bg="#4863a0")

def on_leave(event=None):
    encrypt_button.configure(bg="#368bc1")

root = tk.Tk()
root.title("Caesar Cipher")
root.configure(background="#f8f8ff")

main_frame = ttk.Frame(root, padding="30", style="My.TFrame")
main_frame.grid(row=0, column=0, sticky="nsew")

style = ttk.Style()
style.configure("My.TFrame", background="#c0c0c0")
style.configure("My.TLabel", background="#e3e4f4", font=("Allegro", 12))
style.configure("My.TButton", background="#3a3b3c", foreground="magic mint", font=("Amazone BT", 12, "bold"))

ttk.Label(main_frame, text="Enter the message:", style="My.TLabel").grid(row=0, column=0, sticky="w")
input_text = tk.Text(main_frame, height=5, width=40)
input_text.grid(row=1, column=0, columnspan=3, padx=(0, 10), pady=5, sticky="w")

ttk.Label(main_frame, text="Enter the shift value:", style="My.TLabel").grid(row=2, column=0, sticky="w")
shift_entry = ttk.Entry(main_frame, width=10)
shift_entry.grid(row=2, column=1, pady=5, sticky="w")

ttk.Label(main_frame, text="Select 'encrypt' or 'decrypt':", style="My.TLabel").grid(row=3, column=0, sticky="w")
mode_var = tk.StringVar(value="encrypt")
mode_combobox = ttk.Combobox(main_frame, textvariable=mode_var, values=["encrypt", "decrypt"], width=10)
mode_combobox.grid(row=3, column=1, pady=5, sticky="w")

encrypt_button = tk.Button(main_frame, text="Encrypt/Decrypt", command=encrypt_decrypt, bg="#4caf50", fg="white", font=("Arial", 12, "bold"))
encrypt_button.grid(row=4, column=0, columnspan=2, pady=10)
encrypt_button.bind("<Enter>", on_enter)
encrypt_button.bind("<Leave>", on_leave)

ttk.Label(main_frame, text="Result:", style="My.TLabel").grid(row=5, column=0, sticky="w")
output_text = tk.Text(main_frame, height=5, width=40)
output_text.grid(row=6, column=0, columnspan=3, padx=(0, 10), pady=5, sticky="w")

root.mainloop()