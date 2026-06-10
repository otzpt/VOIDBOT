import tkinter as tk

# 1. Corrigido para tk.Tk()
root = tk.Tk()

root.title("voidtune system optimizer - test")
root.geometry("400x200")

label = tk.Text(root, height=2, width=40)
label.pack(pady=20)
label.insert(tk.END, "voidtune engine: online\nwaiting for performance commands")

# 2. Corrigido de rooot para root
button = tk.Button(root, text="trigger optimization", command=lambda: print("debloat executed successfully!"))
button.pack(pady=10)

root.mainloop()
