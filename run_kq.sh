#!/bin/sh

echo "开始运行自动化考勤脚本"

# 删除旧的虚拟环境（如果有）
rm -rf venv  

# 创建新的 Linux 虚拟环境
python3 -m venv venv  

# 激活虚拟环境
. venv/bin/activate  

# 升级pip，避免旧版本pip安装失败
pip install --upgrade pip

# 安装依赖
pip install -r requirements.txt  
cd testcases

# 运行测试脚本
python test_login.py  

echo "自动化脚本执行完毕"