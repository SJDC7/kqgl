import sys
import os
import logging
from time import sleep
import traceback
from logging.handlers import TimedRotatingFileHandler

# 创建日志目录
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 日志文件格式
log_file = os.path.join(log_dir, "test_login.log")

# 设置日志格式
log_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# **文件日志**
file_handler = logging.FileHandler(log_file,encoding="utf-8")
file_handler.setFormatter(log_formatter)
file_handler.setLevel(logging.INFO)

# **控制台日志**
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
console_handler.setLevel(logging.INFO)

# **日志对象**
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)


# 将 config 目录添加到 sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

try:
    logging.info("导入模块...")
    from config.driver_config import DriverConfig
    from common.yaml_config import Getconf
    from page.LoginPage import LoginPage
    from page.IframPage import IframPage
    from common.tools import rename_file_name, readfile

    logging.info("模块导入成功...")
    

    class TestLogin:

        def __init__(self):
            logging.info("初始化 TestLogin 类...")
            self.driver = DriverConfig().driver_config()
            logging.info("驱动程序已初始化.")

        def login(self,username,password):
            logging.info(f"账户密码: {username}, {password}")
            LoginPage().login_input_value(self.driver, "请输入员工编号", username)
            LoginPage().login_input_value(self.driver, "请输入密码", password)
            LoginPage().drag_and_verify(self.driver)
            LoginPage().click_button(self.driver, "登录")
            logging.info("点击登录...")
            logging.info("登录成功.")
            sleep(2)


        def two_menu(self):
            logging.info("正在进入打卡信息页面...")
            LoginPage().click_one_menu(self.driver, "考勤管理")
            LoginPage().click_two_menu(self.driver, "打卡信息")
            IframPage().get_to_iframe(self.driver)
            logging.info("导航到iframe.")
            sleep(2)
        
        def Attendance_time(self,start_time,end_time,name_data):
            logging.info("正在选择考勤时间...")
            IframPage().input_time(self.driver, "开始时间",start_time)
            IframPage().input_time(self.driver, "结束时间",end_time)
            logging.info(f"选择时间: {start_time} - {end_time}")
            logging.info(f"获取考勤姓名...")

            for name in name_data:
                logging.info(f"选择姓名: {name}")
                IframPage().click_to_name(self.driver, "姓名")
                IframPage().input_select_name(self.driver, name)
                logging.info(f"点击查询...")
                IframPage().click_button(self.driver, "查询")
                sleep(1)
                logging.info(f"点击导出:{name}日志...")
                IframPage().click_button(self.driver, "导出")
                sleep(3)
                logging.info(f"重命名{name}日志...")
                rename = Getconf().get_rename()
                rename_file_name(Getconf().get_save_path()[0], name, rename)
                sleep(3)
                logging.info(f"重命名{name}日志完成.")
        def test_login(self):
            try:
                logging.info("正在启动 test_login ...")
                url = Getconf().get_url()
                logging.info(f"导航到 {(url)}")
                self.driver.get(url)
                username, password = Getconf().get_username_password()
                self.login(username, password)
                self.two_menu()
                name_data = Getconf().get_name()
                stm,ctm = Getconf().get_select_data()
                self.Attendance_time(stm,ctm, name_data)
                logging.info("正在合并考勤明细...")
                svae_path= Getconf().get_save_path()
                logging.info(readfile(svae_path[0],svae_path[1]))
            except Exception as e:
                logger.error(f"测试失败: {e}")
                logger.error(traceback.format_exc())
            finally:
                logging.info("测试完成，关闭驱动...")
                self.driver.quit()

except Exception as e:
    logging.error(f"程序启动失败: {e}")
    logger.error(traceback.format_exc())
    raise
if __name__ == "__main__":
    try:
        logging.info("启动测试...")
        test = TestLogin()
        test.test_login()
    except Exception as e:
        logging.error(f"测试失败: {e}")
        logger.error(traceback.format_exc())
        raise
