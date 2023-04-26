from tkinter import filedialog
import tkinter as tk

class Choose_file:
    def __init__(self) -> None:
        root = tk.Tk()
        root.withdraw()
        self.arquivo = filedialog.askopenfilename(title="Selecione o arquivo",parent=root,filetypes=(("png","*.png"),("jpg","*.jpg"),("jpeg","*.jpeg")))

    def get_dir(self):
        return self.arquivo