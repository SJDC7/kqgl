#!/bin/sh

echo "开始运行自动化考勤脚本"

# 激活虚拟环境
. venv/bin/activate

# 安装依赖（如果需要）
# pip install -r requirements.txt

# 执行自动化测试
python test_login.py

echo "自动化脚本执行完毕"