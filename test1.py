import tkinter as tk
from tkinter import messagebox

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hello Tkinter")
        self.label_text = tk.StringVar()
        self.label_text.set("Nhập chiều cao của bạn: ")
        self.name_text = tk.StringVar()
        self.label = tk.Label(self, textvar=self.label_text)
        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=10)
        self.name_entry = tk.Entry(self, textvar=self.name_text)
        self.name_entry.pack(fill=tk.BOTH, expand=1, padx=20, pady=20)
        hello_button = tk.Button(self, text="Ok",
        command=self.say_hello)
        hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))
        goodbye_button = tk.Button(self, text="Cancel",
        command=self.say_goodbye)
        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))
        
    def say_goodbye(self):
        if messagebox.askyesno("Close Window?", "Would you like to close this window?"):
            self.label_text.set("Window will close in 2 seconds")
            self.after(100, self.destroy)
        else:
            messagebox.showinfo("Not Closing", "Great! This window will stay open.")
            
    def say_hello(self):
        messagebox.showinfo("Chiều cao của bạn là", str("Chiều cao = ")+str(self.name_entry.get()))
        
        
if __name__ == "__main__":
    window = Window()
    window.mainloop()