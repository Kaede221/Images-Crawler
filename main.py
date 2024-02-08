import gradio as gr
from utils.delete_the_same_files import delete_the_same_files
from utils.get_images import get_images

with gr.Blocks() as ROOT:
    with gr.Tab("爬取"):
        gr.Markdown("使用这个很简单，只是你应当拥有一个API可以调用")
        gr.Markdown(
            "填入的数量就是获取的次数，链接就是API链接了，返回内容必须是一张图片，如果不是也会保存，但是请自己去除错误文件，防止数据污染。")
        number = gr.Number(label="获取的次数")
        url_input = gr.Textbox(label="目标链接")
        save_type = gr.Dropdown(["jpg", "png", "jpeg"],
                                label="保存文件类型",
                                value="jpg")
        pro = gr.TextArea(lines=3, label="下载进度")
        button = gr.Button("开始下载").click(get_images,
                                         [number, url_input, save_type], pro)
    with gr.Tab("去重"):
        gr.Markdown("录入需要的目录即可，比如 `C:/Users/`，会自动遍历目标下面的**所有文件**，去除所有重复的文件。")
        TARGET_FLODER = gr.Textbox(label="目标目录", lines=1)
        PRO1 = gr.TextArea(label="进度", lines=3)
        gr.Button("开始去重").click(delete_the_same_files, TARGET_FLODER, PRO1)
        gr.Examples(["images"],
                    TARGET_FLODER,
                    PRO1,
                    delete_the_same_files,
                    run_on_click=True)
if __name__ == "__main__":
    ROOT.queue(20).launch()