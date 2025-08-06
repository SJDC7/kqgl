import datetime
import os
import pandas as pd

def get_now_time():
    return datetime.datetime.now()


def get_now_date_time_str():
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S")


def get_project_path():
    """
    获取项目绝对路径
    :return:
    """
    # project_name = ("CwaTool\CwaTool")
    # file_path = os.path.dirname(__file__)
    # return file_path[:file_path.find(project_name) + len(project_name)]
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def sep(path, add_sep_before=False, add_sep_after=False):
    all_path = os.sep.join(path)
    if add_sep_before:
        all_path = os.sep + all_path
    if add_sep_after:
        all_path = all_path + os.sep
    return all_path


def rename_file_name(directory, new_filename, date):
    """
    获取文件下目录更改为.xlsx文件
    :param directory:
    :param new_filename:
    :param date:
    :return:
    """
    for filename in os.listdir(directory):
        if filename.endswith('.crdownload'):
            old_name = os.path.join(directory, filename)
            # 替换为 .xlsx 后缀
            new_name = os.path.join(directory, date + new_filename + '.xls')

            try:
                # 重命名文件
                os.rename(old_name, new_name)
                print(f"{old_name} 已重命名为 {new_name}")
            except Exception as e:
                print(f"重命名文件时发生错误: {e}")


def readfile(folder_path,excel_file_name):
    excel_files = [f for f in os.listdir(folder_path) if f.endswith('.xls')]
    all_data = pd.DataFrame()

    for file in excel_files:
        file_path = os.path.join(folder_path, file)
        # 读取 Excel 文件
        df = pd.read_excel(file_path, skiprows=2)
        all_data = pd.concat([all_data, df], ignore_index=True)
        # 去掉含有任何空值的行
    df_clean = all_data.dropna(how='any')
    excel_file = os.path.join(excel_file_name, "农业灌区事业部考勤汇总.xlsx")

    try:
        df_clean.to_excel(excel_file,index=False)
        print(f"导出Excel文件成功！，路径为：{excel_file}")
    except Exception as e:
        print(f"保存文件出错：{e}")


if __name__ == '__main__':
    print("项目根目录：", get_project_path())

    readfile(r"D:\Elitel\9_考勤统计\202505月考勤\考勤明细",r"D:\Elitel\9_考勤统计\202505月考勤")