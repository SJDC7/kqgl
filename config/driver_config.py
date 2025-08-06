import getpass
import logging
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
from common.yaml_config import Getconf

# 配置日志记录
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("当前用户：", getpass.getuser())
class DriverConfig:
    """
    用于配置 WebDriver 实例的实用方法
    """

    @staticmethod
    def _configure_preferences():
        svae_path = Getconf().get_rename()
        return {
            "download.default_directory": "D:\\Elitel\\9_考勤统计\\" +svae_path+"考勤\\考勤明细",
            "profile.default_content_settings.popups": 0,
            "download.prompt_for_download": False,
            "safebrowsing.enabled": False,
            "safebrowsing.disable_download_protection": False
        }

    @staticmethod
    def driver_config():
        logging.info("正在初始化WebDriver配置...")

        try:
            # 创建 ChromeOptions 对象，用于配置 Chrome 浏览器选项
            options = Options()
            
            user_data_dir = tempfile.mkdtemp()
            options.add_argument(f"--user-data-dir={user_data_dir}")

            # 设置浏览器窗口大小
            options.add_argument("window-size=1920,1080")

            # 忽略 SSL 证书错误
            options.add_argument("--ignore-certificate-errors")

            # 配置浏览器首选项
            prefs = DriverConfig._configure_preferences()
            # options.add_experimental_option("prefs", prefs)

            # 允许访问不安全的本地主机
            options.add_argument("--allow-insecure-localhost")

            # 允许加载不安全内容
            options.add_argument("--allow-running-insecure-content")

            # 禁用 GPU 加速
            options.add_argument("--disable-gpu")

            # 禁用沙盒模式
            options.add_argument("--no-sandbox")

            # 禁用开发者模式下的共享内存使用
            options.add_argument("--disable-dev-shm-usage")

            # 返回 WebDriver 实例
            logging.info("设置ChromeDriver...")
            return webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )

        except WebDriverException as e:
            logging.error(f"Failed to initialize WebDriver: {e}")
            raise
if __name__ == "__main__":
    try:
        # 初始化 WebDriver
        driver = DriverConfig.driver_config()
        
        # 测试打开一个网页
        driver.get("https://www.google.com")
        print("Successfully opened the webpage.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # 确保浏览器关闭
        if 'driver' in locals():
            driver.quit()