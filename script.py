import cv2
import os
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def create_dicts():
    d, c = {}, {}
    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)
    return d, c

def encrypt_image(img_path, msg, password):
    img = cv2.imread(img_path)
    d, _ = create_dicts()
    n, m, z = 0, 0, 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    encrypted_path = "encryptedImage.jpg"
    cv2.imwrite(encrypted_path, img)
    os.system(f"start {encrypted_path}") 
    return encrypted_path, password

def decrypt_image(img_path, msg_length, stored_password):
    img = cv2.imread(img_path)
    _, c = create_dicts()
    pas = simpledialog.askstring("Passcode", "Enter passcode for Decryption", show='*')

    if pas == stored_password:
        message, n, m, z = "", 0, 0, 0
        for i in range(msg_length):
            message += c[img[n, m, z]]
            n = (n + 1) % img.shape[0]
            m = (m + 1) % img.shape[1]
            z = (z + 1) % 3
        messagebox.showinfo("Decryption", f"Decryption message: {message}")
    else:
        messagebox.showerror("Error", "Incorrect passcode!")

def select_image():
    file_path = filedialog.askopenfilename(title="Select Image")
    return file_path

def encrypt_action():
    img_path = select_image()
    if img_path:
        msg = simpledialog.askstring("Secret Message", "Enter secret message:")
        password = simpledialog.askstring("Passcode", "Enter a passcode:", show='*')
        encrypt_image(img_path, msg, password)

def decrypt_action():
    img_path = select_image()
    if img_path:
        msg_length = simpledialog.askinteger("Message Length", "Enter the length of the hidden message:")
        stored_password = simpledialog.askstring("Passcode", "Enter the passcode you used:", show='*')
        decrypt_image(img_path, msg_length, stored_password)


root = tk.Tk()
root.title("Sanchit AICTE Intership Project-25 Stegnography")

frame = tk.Frame(root)
frame.pack(pady=20)

encrypt_btn = tk.Button(frame, text="Encrypt 'D' Image", command=encrypt_action)
decrypt_btn = tk.Button(frame, text="Decrypt 'D' Image", command=decrypt_action)

encrypt_btn.pack(side=tk.LEFT, padx=10)
decrypt_btn.pack(side=tk.RIGHT, padx=10)

root.mainloop()
