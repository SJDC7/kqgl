class IframeBase:
    def switch_to_iframe(self):
        """
        进入iframe
        :return:
        """
        return f"//iframe[@id='ifrContent']"

    def select_name(self, Condition_name):
        """
        下拉框
        :return:
        """
        return f"//td[contains(text(),'{Condition_name}')]/following-sibling::td/div/a/span"

    def input_select_xpath(self):
        """
        输入姓名
        :param input_name:
        :return:
        """
        return "//*[@id='people_name_chosen']/div/div/input"

    def start_time_select(self):
        """
        开始时间
        :param time_name:
        :return:
        """
        return "//*[@id='dtpStartTime']/input"

    def ent_time_select(self):
        """
        结束时间
        :return:
        """
        return "//*[@id='dtpEndTime']/input"

    def button_btnSearch(self):
        """
        查询按钮
        :return:
        """
        return "//*[@id='btnSearch']"

    def button_btnExport(self):
        """
        导出按钮
        :return:
        """
        return "//*[@id='btnExport']"
