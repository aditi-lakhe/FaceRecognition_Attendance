import tkinter as tk
import util

class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x520+350+100")

        self.login_button_main_window = util.get_button(
            self.main_window, "Login", "green", self.login
        )
        self.login_button_main_window.place(x=750, y=300)

        self.register_new_user_button_main_window = util.get_button(
            self.main_window, "Register New User", "gray", self.register_new_user, fg='black'
        )
        self.register_new_user_button_main_window.place(x=750, y=400)

        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)

        self.add_webcam(self.webcam_label)

    def start(self):
        self.main_window.mainloop()

    def login(self):
        print("Login clicked")

    def register_new_user(self):
        print("Register clicked")

    def add_webcam(self, label):
        pass
if __name__ == "__main__":
    app = App()
    app.start()

