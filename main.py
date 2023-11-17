from customtkinter import *


class App():
    def __init__(self) -> None:
        self.app =CTk()
        self.app.geometry('700x906')
        self.app.resizable(width=False, height=False)

        self.frame_up = CTkFrame(master=self.app, width=700, height=100, fg_color="#2C2828", border_color="#373333", border_width=2)
        self.frame_center = CTkFrame(master=self.app,  width=700, height=700, fg_color="#1B2021", border_color="#373333", border_width=2)
        self.frame_down = CTkFrame(master=self.app,  width=700, height=100, fg_color="#2C2828", border_color="#373333", border_width=2)

        self.frame_up.pack(pady=1, padx=1, anchor="n")
        self.frame_center.pack(pady=1, padx=1, anchor="center")       
        self.frame_down.pack(pady=1, padx=1, anchor="e")

        btn = CTkButton(master=self.frame_up, text='Click', corner_radius=32, command=self.click)
        btn.place(relx=0.5, rely=0.5, anchor='s')

        self.entry = CTkEntry(master=self.frame_center, placeholder_text='Start...')
        self.entry.place(relx=0.5, rely=0.5, anchor='n')
        self.entry.bind("<Return>", self.enter)
        self.app.mainloop()

    def click(self):
        print('asdasd')

    def enter(self, event):
        self.entry.configure(placeholder_text='')
        value = self.entry.get()
        self.entry.delete(0, 'end')
        print(value)


if __name__ == "__main__":
    run = App()
