#!/bin/bash

echo "开始运行自动化考勤脚本"

# 激活虚拟环境（如果有的话，路径示例）
source venv/bin/activate

# 安装依赖（如果需要）
# pip install -r requirements.txt

# 执行自动化测试
python3 test_login.py

echo "自动化脚本执行完毕"