from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 自动下载并管理 ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 打开测试页面
driver.get("https://www.google.com")

# 关闭浏览器
driver.quit()