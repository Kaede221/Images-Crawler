"""
2023.6.29 18:00
"""

import hashlib
import os
import gradio as gr


def getmd5(filename):
    """
    获取文件 md5 码
    :param filename: 文件路径
    :return: 文件 md5 码
    """
    file_txt = open(filename, 'rb').read()
    # 调用一个md5对象
    m = hashlib.md5(file_txt)
    # hexdigest()方法来获取摘要（加密结果）
    return m.hexdigest()


def delete_the_same_files(path, progress=gr.Progress()):
    # 存放文件的 md5 码
    all_md5 = []
    # 计数变量
    total_file = 0
    total_delete = 0
    # 遍历文件夹下的所有文件
    for file in progress.tqdm(os.listdir(path)):
        # 文件数量加 1
        total_file += 1
        # 文件的路径
        real_path = os.path.join(path, file)
        # 判断文件是否是文件
        if os.path.isfile(real_path) == True:
            # 获取文件的md5码
            filemd5 = getmd5(real_path)
            # 如果文件 md5 已存在，则删除此文件
            if filemd5 in all_md5:
                total_delete += 1
                os.remove(real_path)
            else:
                # 如果文件 md5 不存在，则将此文件的 md5 码添加到 all_md5 列表中
                all_md5.append(filemd5)
    return f"源文件数量:{total_file}, 删除数量:{total_delete}, 剩余数量:{total_file - total_delete}"