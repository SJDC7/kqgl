from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from config.driver_config import DriverConfig
from common.yaml_config import Getconf

from base.LoginBase import LoginBase


class LoginPage(LoginBase):

    def login_input_value(self, driver, input_placeholder, input_value):
        """
        登录页输入值
        :param driver:
        :param input_placeholder:
        :param input_value:
        :return:
        """
        input_xpath = self.login_input(input_placeholder)
        return driver.find_element(By.XPATH, input_xpath).send_keys(input_value)

    def click_button(self, driver, button_name):
        """
        点击登录
        :param driver:
        :param input_placeholder:
        :param input_value:
        :return:
        """
        button_xpath = self.login_button(button_name)
        return driver.find_element(By.XPATH, button_xpath).click()

    def drag_and_verify(self, driver):
        """
        拖拽滑块进行验证
        """
        drag_slider_xpath = self.verify()
        slider = driver.find_element(By.XPATH, drag_slider_xpath)
        # 创建模拟交互对象
        action = ActionChains(driver)
        # 点击并按住元素往右滑动350，并释放
        action.click_and_hold(slider).move_by_offset(350, 0).release().perform()

    def click_one_menu(self, driver, menu_name):
        """
        点击一级菜单
        :param driver:
        :param menu_name:
        :return:
        """
        menu_xpath = self.one_menu(menu_name)
        return driver.find_element(By.XPATH, menu_xpath).click()

    def click_two_menu(self, driver, menu_name):
        """
        点击二级菜单
        :param driver:
        :param menu_name:
        :return:
        """
        menu_xpath = self.two_menu(menu_name)
        return driver.find_element(By.XPATH, menu_xpath).click()


