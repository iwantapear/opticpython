import requests
from io import BytesIO
from PIL import Image

# Step 1: 解析文字描述并提取关键词和短语
description = "一只棕色的狗在海滩上奔跑"
keywords = ["狗", "棕色", "海滩", "奔跑"]

# Step 2: 使用Google Images API搜索相关的图片
query = " ".join(keywords)
url = "https://www.googleapis.com/customsearch/v1"
params = {
    "key": "YOUR_API_KEY",
    "cx": "YOUR_CX_ID",
    "q": query,
    "searchType": "image"
}
response = requests.get(url, params=params)
json_data = response.json()
image_links = [item["link"] for item in json_data["items"]]

# Step 3: 下载和保存图片
for i, link in enumerate(image_links):
    try:
        response = requests.get(link)
        image = Image.open(BytesIO(response.content))
        image.save(f"image_{i}.jpg")
    except:
        pass
