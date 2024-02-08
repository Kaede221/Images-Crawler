import gradio as gr
import warnings
import requests
import math
from utils.get_random_str import get_random_str
# 取消所有警告
warnings.simplefilter("ignore")


# 下载图片的功能函数
def get_images(times, url: str, save_type: str, progress=gr.Progress()) -> str:
    """下载/获取图片

    Args:
        times (int): 下载的次数
        url (str): 目标链接，建议用某一个图片API地址
        save_type (str): 保存文件类型

    Returns:
        str: 这次下载的结果
    """
    # 默认，字符串长度
    length = 10
    # 转换类型
    try:
        times = int(times)
    except:
        times = math.ceil(times)
        print(f"请输入正确的次数，已修正为{times}")
    download_successfully_total = 0
    download_fail_total = 0
    for i in progress.tqdm(range(times)):
        try:
            r = requests.get(url)
            with open(f"images/{get_random_str(length=length)}.{save_type}",
                      "wb") as f:
                f.write(r.content)
            download_successfully_total = download_successfully_total + 1
        except:
            download_fail_total = download_fail_total + 1
    return f"成功/失败/目标 : {download_successfully_total}/{download_fail_total}/{times}"