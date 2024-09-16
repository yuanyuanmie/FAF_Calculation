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


url = 'https://www1.hkexnews.hk/listedco/listconews/sehk/2024/0103/2024010302045.pdf'  # 替换为你要下载的PDF文件的URL
save_path = osp.join(ROOT, "data", "totalshare", "1477", "2024010302045.pdf")


# 打开PDF文件
with pdfplumber.open(r"C:\Users\shenys\FAF_Calculation\data/ir/1477/20230926.pdf") as pdf:
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
