echo 开始运行自动化考勤脚本

cd /d D:\auto_test

:: 创建虚拟环境（可选）

call venv\Scripts\activate

:: 安装依赖
:: pip install -r requirements.txt

:: 执行自动化测试（如 Selenium 脚本）
python test_login.py

echo 自动化脚本执行完毕