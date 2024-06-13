import tkinter
import urllib.request

class Analyze_All_Function:
    def __init__(self):
        self.Windows = tkinter.Tk()
        self.title = self.Windows.title("Numbers Analyze tool")
        self.Windows_height = 600
        self.Windows_width = 1000
        self.unsizeale = self.Windows.resizable(False, False)
        self.computer_info_height = self.Windows.winfo_screenheight()
        self.computer_info_width = self.Windows.winfo_screenwidth()
        self.screen_x = int((self.computer_info_width - 1000) / 2)
        self.screen_y = int((self.computer_info_height - 600) / 2)
        self.size_position_str = f"{self.Windows_width}x{self.Windows_height}+{self.screen_x}+{self.screen_y}"
        self.New_Windows = self.Windows.geometry(self.size_position_str)

    def Entry_Function(self):
        self.entry = tkinter.Entry(
            self.Windows, background="#FFFFFF", foreground="#4B0082",
            selectbackground="#FFFF00", selectforeground="#DC143C", font=("宋体", 15, "underline"),
            width=88, relief="solid", insertwidth=1)
        self.entry.place(x=50, y=10)

    def url_get(self):
        self.entry_get = self.entry.get()
        return self.entry_get

    def Windows_Button(self):
        self.button_serch = tkinter.Button(
            self.Windows, text="搜索/下载", width=8, height=1, font=("Arial", 8, "underline"))
        self.button_width = self.button_serch.winfo_width()
        self.button_height = self.button_serch.winfo_height()
        self.x = int(self.Windows_width - self.button_width)
        self.y = 10
        self.button_serch.place(x=self.x, y=self.y, anchor="ne")
        self.button_serch.bind("<Button-1>", self.bind_get_url)

    def bind_get_url(self, event):
        self.Downloader_get()

    def Downloader_get(self):
        url = self.url_get()
        if url == "" or url == ' ':
            print("URL is empty")
        else:
            try:
                self.response = urllib.request.urlopen(url)
                self.reading = self.response.read()
                print(self.reading)
            except Exception as e:
                print("Error:", e)
    def main_loop(self):
        self.Windows.mainloop()

if __name__ == "__main__":
    run = Analyze_All_Function()
    run.Entry_Function()
    run.Windows_Button()
    run.main_loop()
