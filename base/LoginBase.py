class LoginBase:

    def login_input(self, input_placeholder):
        """
        登录用户名，密码输入框
        :param input_placeholder:
        :return:
        """
        return f"//input[@placeholder = '{input_placeholder}']"

    def login_button(self, button_name):
        """
        登录按钮
        :param button_name:
        :return:
        """
        return f"//button[text()='{button_name}']"

    def verify(self):
        """
        滑块验证
        :return:
        """
        return "//span[text()='请按住滑块，拖动到最右边']/preceding-sibling::span"

    def one_menu(self, menu_name):
        """
        左侧菜单
        :return:
        """
        return f"//span[text()='{menu_name}']/parent::span"

    def two_menu(self, menu_name):
        """
        二级菜单
        :param menu_name:
        :return:
        """
        return f"//span[text()='{menu_name}']/parent::a"


if __name__ == '__main__':
    print(LoginBase().select_name("姓名"))
