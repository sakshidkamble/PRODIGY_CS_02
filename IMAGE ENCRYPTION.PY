from tkinter import Tk, Label, Button, Entry, filedialog, messagebox
from PIL import Image
import os

def encrypt_image(input_path, output_path, key):
    try:
        image = Image.open(input_path)
        pixels = image.load()
        width, height = image.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256
                pixels[x, y] = (r, g, b)

        image.save(output_path)
        messagebox.showinfo("Success", f"Image encrypted successfully:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Encryption failed: {e}")

def decrypt_image(input_path, output_path, key):
    try:
        image = Image.open(input_path)
        pixels = image.load()
        width, height = image.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256
                pixels[x, y] = (r, g, b)

        image.save(output_path)
        messagebox.showinfo("Success", f"Image decrypted successfully:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {e}")

def browse_image():
    filename = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
    entry_path.delete(0, 'end')
    entry_path.insert(0, filename)

def encrypt_action():
    path = entry_path.get()
    key = entry_key.get()
    if not path or not key:
        messagebox.showwarning("Input Missing", "Please provide both image and key.")
        return
    output_path = os.path.splitext(path)[0] + "_encrypted.png"
    encrypt_image(path, output_path, int(key))

def decrypt_action():
    path = entry_path.get()
    key = entry_key.get()
    if not path or not key:
        messagebox.showwarning("Input Missing", "Please provide both image and key.")
        return
    output_path = os.path.splitext(path)[0] + "_decrypted.png"
    decrypt_image(path, output_path, int(key))

# GUI Window
window = Tk()
window.title("Image Pixel Encryptor")
window.geometry("400x250")
window.resizable(False, False)

# Widgets
Label(window, text="Select Image:").pack(pady=5)
entry_path = Entry(window, width=40)
entry_path.pack(pady=5)
Button(window, text="Browse", command=browse_image).pack(pady=5)

Label(window, text="Enter Key (integer):").pack(pady=5)
entry_key = Entry(window, width=20)
entry_key.pack(pady=5)

Button(window, text="Encrypt Image", width=20, command=encrypt_action).pack(pady=10)
Button(window, text="Decrypt Image", width=20, command=decrypt_action).pack(pady=5)

# Run the GUI
window.mainloop()

