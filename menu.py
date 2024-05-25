import tkinter as tk
from tkinter import messagebox
import sys; sys.path.append("Ciphers")
from shift_cipher import *
from substitution_cipher import *
from affine_cipher import *
from vigenere_cipher import *
from one_time_pad import *

#########################################################################################
# Implements a GUI menu allowing the user to encrypt a message with a random or custom  #
# key using the four crypto implementations in the Ciphers directory.                   #
#                                                                                       #
# 
#
#
#
#
#
#
#########################################################################################
class CryptoGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.grid(padx=20, pady=20)

        self.cipher_options = {"Shift cipher":0, "Substitution cipher":1, "Affine cipher":2, "One-time-pad":3}

        self.create_widgets()
        self.key = 0



    def create_widgets(self):
        self.var_cipher = tk.StringVar(self)
        self.var_cipher.set("Choose a cipher")

        self.message_label = tk.Label(self, text="Message to encrypt/decrypt:")
        self.message_label.grid(row=0, column=0, sticky=tk.W)
        self.message_entry = tk.Entry(self)
        self.message_entry.grid(row=0, column=1, columnspan=2, sticky=tk.W+tk.E)

        self.key_label = tk.Label(self, text=("Key to use (or \"random\" for random):"))
        self.key_label.grid(row=1, column=0, sticky=tk.W)
        self.key_entry = tk.Entry(self)
        self.key_entry.grid(row=1, column=1, columnspan=2, sticky=tk.W+tk.E)

        self.cipher_label = tk.Label(self, text="Cipher to use: ")
        self.cipher_label.grid(row=2, column=0, sticky=tk.W)
        self.dropdown_menu = tk.OptionMenu(self, self.var_cipher, *self.cipher_options.keys())
        self.dropdown_menu.grid(row=2, column=1, columnspan=2, sticky=tk.W+tk.E)

        self.encrypt_button = tk.Button(self)
        self.encrypt_button["text"] = "Encrypt"
        self.encrypt_button["command"] = self.encrypt_message
        self.encrypt_button.grid(row=3, column=0, sticky=tk.W)

        self.decrypt_button = tk.Button(self)
        self.decrypt_button["text"] = "Decrypt"
        self.decrypt_button["command"] = self.decrypt_message
        self.decrypt_button.grid(row=3, column=1, sticky=tk.W)

        self.result_label = tk.Label(self, text="Result:")
        self.result_label.grid(row=4, column=0, sticky=tk.W)
        self.result_text = tk.Text(self, height=10, width=50)
        self.result_text.grid(row=5, column=0, columnspan=3, sticky=tk.W+tk.E)

    def encrypt_message(self):
        message = self.message_entry.get()
        cipher = self.cipher_options[self.var_cipher.get()]
        key = self.key_entry.get()
        if cipher == 0:
            if key == "random":
                key = rand.randint(1, 127)
            encrypted_message = apply_shift_cipher(message, key)
        elif cipher == 1:
            if key == "random":
                key = rand.randint(1, 127)
            encrypted_message = apply_substitution_cipher(message, key)
        elif cipher == 2:
            if key == "random":
                a = rand.randint(1, 127)
                while is_coprime(a, 128) == False:
                    a = rand.randint(1, 127)
                b = rand.randint(1, 127)
                key = (a, b)
            encrypted_message = apply_affine_cipher(message, key)
        elif cipher == 3:
            msg_binary = convert_str_to_bin(message)
            length = len(msg_binary)
            if key == "random":
                key = gen_key(length)
            encrypted_message = one_time_pad(msg_binary, key)
        self.key = key

        self.key_entry.delete(0, tk.END)
        self.key_entry.insert(0, key)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, encrypted_message)

    def decrypt_message(self):
        ciphertext = self.message_entry.get()
        cipher = self.cipher_options[self.var_cipher.get()]
        key = self.key_entry.get()
        if cipher == 0:
            message = reverse_shift_cipher(ciphertext, int(key))
        elif cipher == 1:
            message = reverse_substitution_cipher(ciphertext, int(key))
        elif cipher == 2:
            message = reverse_affine_cipher(ciphertext, key)
        elif cipher == 3:
            msg_binary = convert_str_to_bin(ciphertext)
            n = 0
            for ch in ciphertext:
                if not ch in ['0', '1']:
                    n+=1
            if n == 0:
                msg_binary=ciphertext
            length = len(msg_binary)
            message = one_time_pad(msg_binary, key)
            message = convert_bin_to_str(message)
        self.key = key

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, message)

root = tk.Tk()
root.title("Crypto GUI")
CGUI = CryptoGUI(master=root)
CGUI.mainloop()

