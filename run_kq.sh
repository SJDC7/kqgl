#!/bin/sh
set -e  # 遇错立刻退出

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

echo "已安装库列表："
pip list

cd testcases

python test_login.py

echo "自动化脚本执行完毕"