import tkinter as tk
import qrcode
import qrcode.image.svg
import os

# QR code generator
def generate_qr_codes():
    names = name_entry.get().split(',')
    urls = url_entry.get().split(',')
    
    if len(names) != len(urls):
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: Number of names and URLs must match.")
        return
    
    for name, url in zip(names, urls):
        img = qrcode.make(url, image_factory=qrcode.image.svg.SvgImage)
        filename = name.strip() + ".svg"
        img.save(filename)

        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"QR code generated for {name.strip()}")

# main window
root = tk.Tk()
root.title("QR Code Generator")

# Labels and Entries for names and URLs
name_label = tk.Label(root, text="Enter Names (comma-separated):")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

url_label = tk.Label(root, text="Enter URLs (comma-separated):")
url_label.pack()
url_entry = tk.Entry(root)
url_entry.pack()

# Execution button
generate_button = tk.Button(root, text="Generate QR Codes", command=generate_qr_codes)
generate_button.pack()

# display results or errors
result_text = tk.Text(root, height=4, width=50)
result_text.pack()

root.mainloop()

