import tkinter as tk
import keyboard  # 引入 keyboard 库
from translate import translator

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("快捷键唤起界面示例")
        # 界面宽高
        self.width = 300
        self.height = 50
        self.geometry(f"{self.width}x{self.height}")
        self.overrideredirect(True)  # 隐藏标题栏和边框
        self.center_window()
        self.entry = tk.Entry(self, justify='center', font=('Times New Roman', 20))
        self.entry.bind("<Return>", self.trans_en2zn)
        self.bind("<Escape>", self.hide_window)
        self.entry.pack(fill=tk.BOTH, expand=True)

        # 监听全局快捷键
        keyboard.add_hotkey('Ctrl+q', self.on_key_press)

    def hide_window(self, event):
        self.withdraw()  # 隐藏窗口

    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.width) // 2
        y = (screen_height - self.height) // 4
        self.geometry(f"{self.width}x{self.height}+{x}+{y}")

    def on_key_press(self):
        self.deiconify()  # 唤起窗口

    def trans_en2zn(self, event):
        text = self.entry.get()
        translation = translator.translate_text(text)
        self.entry.delete(0, tk.END)  # 清空输入框
        self.entry.insert(0, translation)  # 插入新文本


app = MyApp()
app.mainloop()

