from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

from base.IframeBase import IframeBase


class IframPage(IframeBase):

    def get_to_iframe(self, driver):
        """
        进入iframe
        :param driver:
        :return:
        """
        iframe_xpath = self.switch_to_iframe()
        iframe_element = driver.find_element(By.XPATH, iframe_xpath)
        return driver.switch_to.frame(iframe_element)

    def click_to_name(self, driver, Condition_name):
        """
        点击姓名下拉框
        :param driver:
        :return:
        """
        select_xpath = self.select_name(Condition_name)
        return driver.find_element(By.XPATH, select_xpath).click()

    def input_select_name(self, driver, input_name):
        """
        输入姓名
        :param driver:
        :param input_name:
        :return:
        """
        input_xpath = self.input_select_xpath()
        input_element = driver.find_element(By.XPATH, input_xpath)
        return input_element.send_keys(input_name, Keys.RETURN)

    def input_time(self, driver, time_name, input_value):
        """
        输入时间值
        :param driver:
        :param input_value:
        :return:
        """
        if time_name == "开始时间":
            input_xpath = self.start_time_select()
            input_element = driver.find_element(By.XPATH, input_xpath)
            input_element.clear()
            return input_element.send_keys(input_value)
        elif time_name == "结束时间":
            input_xpath = self.ent_time_select()
            input_element = driver.find_element(By.XPATH, input_xpath)
            input_element.clear()
            return input_element.send_keys(input_value)
        else:
            raise ValueError(r"无效的时间名称:{time_name}")

    def click_button(self, driver, button_name):
        """
        点击查询/导入按钮
        :param driver:
        :param button_name:
        :return:
        """
        if button_name == "查询":
            button_xpath = self.button_btnSearch()
            return driver.find_element(By.XPATH, button_xpath).click()
        elif button_name == "导出":
            button_xpath = self.button_btnExport()
            return driver.find_element(By.XPATH, button_xpath).click()
        else:
            raise ValueError(r"无效的按钮名称:{button_name}")
