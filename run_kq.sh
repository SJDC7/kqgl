#!/bin/sh

echo "开始运行自动化考勤脚本"

# 删除旧的虚拟环境（如果有）
rm -rf venv  

# 创建新的 Linux 虚拟环境
python3 -m venv venv  

# 激活并安装依赖
. venv/bin/activate  
pip install -r requirements.txt  

# 运行测试
python test_login.py  

echo "自动化脚本执行完毕"