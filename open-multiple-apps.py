import tkinter as tk
import os
from tkinter import filedialog, Text

apps = []
if os.path.isfile('apps.txt'):
    with open('apps.txt', 'r') as rfp:
        temp_apps = rfp.read()
        temp_apps = temp_apps.split(',')
        apps = [x for x in temp_apps if x.strip()]

def add_app():
    for widget in frame.winfo_children():
        widget.destroy()

    file_name = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(('executables','*.exe'), ("All Files", '*.*')))
    apps.append(file_name)
    for app in apps:
        label = tk.Label(frame, text=app, fg='blue', bg="white")
        label.pack()

def run_apps():
    for app in apps:
        os.startfile(app)

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack()
 
frame = tk.Frame(root,bg= '#FFF')
frame.place(relheight=0.8, relwidth=0.8, relx = 0.1, rely=0.05)

open_file = tk.Button(root, text="Open File", padx=10, pady=5, bg="#236D42", fg="#FFF", command=add_app)
open_file.pack()

run_apps = tk.Button(root, text="Run Apps", padx=10, pady=5, bg="#236D42", fg="#FFF", command=run_apps)
run_apps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('apps.txt', 'w') as fp:
    for app in apps:
        fp.write(app + ',')

