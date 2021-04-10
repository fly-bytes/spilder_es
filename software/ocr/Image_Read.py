'''
用Python提取图片中的文字，用到的工具包有PIL,pytesseract,tesseract-ocr
1. pip install pytesseract
2. pip install PIL
3. https://digi.bib.uni-mannheim.de/tesseract/ 下载tesseract，配置环境变量
4. 配置语言包，下载的中文库放在 Tesseract-OCR 安装目录下的 tessdata 文件夹中
5. 设置pytesseract的tessdata路径，tesseract_cmd = 'E:\\Program Files\\Tesseract-OCR'
'''

from PIL import Image
import pytesseract

img_path = 'C:\\Users\\liusai\\Pictures\\下载.jpg'
pytesseract.pytesseract.tesseract_cmd = r'E:\\Program Files\\Tesseract-OCR\\Tesseract.exe'

images = Image.open(img_path)
text = pytesseract.image_to_string(images, lang='chi_sim')
print(text)
