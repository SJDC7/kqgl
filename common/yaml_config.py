import sys
import os
import yaml

# 将项目根目录添加到 sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from common.tools import get_project_path, sep

class Getconf:
    def __init__(self):
        try:
            # 构建配置文件路径
            config_path = os.path.join(get_project_path(), "config", "environment.yaml")
            
            
            # 打开并加载 YAML 文件
            with open(config_path, encoding="utf-8") as file:
                self.env = yaml.load(file, Loader=yaml.FullLoader)
            
            if not self.env:
                raise ValueError("配置文件为空或格式不正确")
        except Exception as e:
            print(f"加载配置文件失败: {e}")
            raise

    def get_username_password(self):
        try:
            return self.env["user"]["username"], self.env["user"]["password"]
        except KeyError:
            print("配置文件中缺少 'user' 或其子项")
            raise

    def get_url(self):
        try:
            return self.env["url"]
        except KeyError:
            print("配置文件中缺少 'url'")
            raise

    def get_name(self):
        try:
            return self.env["name"]
        except KeyError:
            print("配置文件中缺少 'name'")
            raise

    def get_select_data(self):
        try:
            return self.env["select_data"]["stm"], self.env["select_data"]["etm"]
        except KeyError:
            print("配置文件中缺少 'select_data'")
            raise
        
    def get_save_path(self):
        try:
            return self.env["save_path"]["save_path1"], self.env["save_path"]["save_path2"]
        except KeyError:
            print("配置文件中缺少 'save_path'")
            raise
    def get_rename(self):
        try:
            return self.env["rename"]
        except KeyError:
            print("配置文件中缺少 'rename'")
            raise


if __name__ == '__main__':
    try:
        config = Getconf()
        print("用户名和密码:", config.get_username_password())
        print("URL:", config.get_url())
        print("姓名列表:", config.get_name())
        print("查询时间:", config.get_select_data())
        print("保存路径:", config.get_save_path())
        print("重命名规则:", config.get_rename())

    except Exception as e:
        print(f"测试失败: {e}")
        