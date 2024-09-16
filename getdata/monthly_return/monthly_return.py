import os
import sys
import os.path as osp
import requests
import warnings
import pdfplumber
import re

warnings.filterwarnings("ignore")

ROOT = os.path.dirname(os.path.abspath("."))
sys.path.append(ROOT)

local = "1477"

# def download_pdf(url, save_path):
#     """
#     从指定URL下载PDF文件并保存到指定路径。
#
#     :param url: PDF文件的URL地址
#     :param save_path: 保存文件的完整路径
#     """
#
#     if os.path.exists(save_path):
#         print("文件存在")
#     else:
#         # 创建一个PDF文件
#         c = canvas.Canvas(save_path)
#     # 发送GET请求
#     response = requests.get(url, stream=True)
#
#     # 检查请求是否成功
#     if response.status_code == 200:
#         # 打开文件准备写入
#         with open(save_path, 'wb') as f:
#             # 迭代响应的内容
#             for chunk in response.iter_content(chunk_size=8192):
#                 # 写入文件
#                 if chunk:  # 过滤掉keep-alive新分块
#                     f.write(chunk)
#         print(f"文件已保存到 {save_path}")
#     else:
#         print(f"下载失败，状态码：{response.status_code}")

url = 'https://www1.hkexnews.hk/listedco/listconews/sehk/2024/0103/2024010302045.pdf'  # 替换为你要下载的PDF文件的URL
save_path = osp.join(ROOT, "data", "totalshare", "1477", "2024010302045.pdf")
# 打开PDF文件
with pdfplumber.open(r"C:\Users\shenys\FAF_Calculation\data/totalshare/1477/2024010302045.pdf") as pdf:
    text = pdf.pages[0].extract_text()
    pattern = r"Total authorised/registered share capital at the end of the month: USD ([\s\S]*?)(?=\n\w+:|$)"
    if text:
        # 分割文本，以便我们可以找到字符串的位置
        lines = text.split('\n')
        result = ""
        line = lines[-2].strip()
        result += line + "\n"
        # 使用re.search来查找匹配项
        match = re.search(pattern, line, re.MULTILINE)
        # 如果找到了匹配项，就提取捕获组中的内容
        if match:
            result = match.group(1).strip()
            # 去除逗号并转换为整数
            number_int = int(result.replace(",", ""))
            # 打印结果
            print(number_int)  # 输出: 50000
        else:
            print("未找到匹配项")

    else:
        print("这个数据第一页没有信息")
