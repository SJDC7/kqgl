#!/bin/sh
#set -e  # 遇错立刻退出

echo "开始运行自动化考勤脚本"

rm -rf venv
python3 -m venv venv

. venv/bin/activate

echo "Python 版本："
python --version

echo "pip 版本："
pip --version

pip install --upgrade pip
pip install -r requirements.txt

cd testcases

python test_login.py

echo "自动化脚本执行完毕"

# 测试2025-08-04 15:56:47