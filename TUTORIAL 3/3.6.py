import tkinter as tk
def bhs():
    result_label.config(text=entry.get().upper())
root = tk.Tk()
root.title("Uppercase Converter")
root.geometry("300x150")
tk.Label(root, text="Enter text:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)
tk.Button(root, text="Convert", command=bhs).pack(pady=5)
result_label = tk.Label(root, font=("Papyrus", 12, "bold"))
result_label.pack(pady=5)
root.bhsloop()
