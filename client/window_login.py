from tkinter import Tk, Label, Frame, Entry, Button, LEFT, END


class WindowLogin(Tk):
    """登录窗口"""

    def __init__(self):
        """初始化登录窗口"""

        super(WindowLogin, self).__init__()

        # 设置窗口属性
        self.window_init()
        # 填充控件
        self.add_widgets()

        # self.on_login_button_click(lambda: print(self.get_username()))

    def window_init(self):
        """初始化窗口属性"""
        # 设置窗口标题
        self.title('登录窗口')

        # 设置窗口不能拉伸
        self.resizable(False, False)

        # 获取窗口位置变量
        window_width = 270
        window_height = 100

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        pos_x = (screen_width - window_width) / 2
        pos_y = (screen_height - window_height) / 2

        # 设置窗口大小和位置
        self.geometry('%dx%d+%d+%d' % (window_width, window_height, pos_x, pos_y))  # 宽x高+X坐标+Y坐标

    def add_widgets(self):
        """添加控件到窗口里"""
        # 用户名
        username_label = Label(self)
        username_label['text'] = '用户名：'
        username_label.grid(row=0, column=0, padx=10, pady=5)

        username_entry = Entry(self, name='username_entry')
        username_entry['width'] = 25
        username_entry.grid(row=0, column=1)

        # 密码
        password_label = Label(self)
        password_label['text'] = '密 码：'
        password_label.grid(row=1, column=0)

        password_entry = Entry(self, name='password_entry')
        password_entry['width'] = 25
        password_entry['show'] = '*'
        password_entry.grid(row=1, column=1)

        # 按钮区
        button_frame = Frame(self, name='button_frame')

        # 重置按钮
        reset_button = Button(button_frame, name='reset_button')
        reset_button['text'] = ' 重置 '
        reset_button.pack(side=LEFT, padx=20)

        # 登录按钮
        login_button = Button(button_frame, name='login_button')
        login_button['text'] = ' 登录 '
        login_button.pack(side=LEFT)

        button_frame.grid(row=2, columnspan=2, pady=5)

    def get_username(self):
        """获取用户名"""
        return self.children['username_entry'].get()

    def get_password(self):
        """获取密码"""
        return self.children['password_entry'].get()

    def clear_username(self):
        """清空用户名输入框"""
        self.children['username_entry'].delete(0, END)

    def clear_password(self):
        """清空用户名输入框"""
        self.children['password_entry'].delete(0, END)

    def on_reset_button_click(self, command):
        """登录按钮的响应注册"""
        reset_button = self.children['button_frame'].children['reset_button']
        reset_button['command'] = command

    def on_login_button_click(self, command):
        """登录按钮的响应注册"""
        login_button = self.children['button_frame'].children['login_button']
        login_button['command'] = command

    def on_window_closed(self, command):
        """关闭窗口的响应注册"""
        self.protocol('WM_DELETE_WINDOW', command)


if __name__ == '__main__':
    window = WindowLogin()
    window.mainloop()
