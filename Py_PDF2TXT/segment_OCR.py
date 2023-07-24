# @time     :2023/7/24 12:11
# @Author   :XZQ
import datetime
import os
import pytesseract
import fitz 

# @pdf_zoom:         pdf图像缩放
# @pdf_startpage:    指定pdf起始页
def tesseractOCR_pdf(pdf_Path,txt_Path = './txt', pdf_zoom = 2.0, pdf_startpage = 0):
    startTime = datetime.datetime.now() 
    if not os.path.exists(txt_Path):  # 判断txt文件夹是否存在
        os.makedirs(txt_Path) 

    pdfDoc = fitz.open(pdf_Path)
    for i in range(pdf_startpage,pdfDoc.page_count):
        page = pdfDoc[i]
        rotate = int(0)
        # 每个尺寸的缩放系数
        mat = fitz.Matrix(pdf_zoom, pdf_zoom).prerotate(rotate)
        pix = page.get_pixmap(matrix=mat, alpha=False)
        pix.save("IMG_buffer.png") 

        result = pytesseract.image_to_string(image="./IMG_buffer.png",lang="chi_sim",config="--psm 1")   #路径；语言；配置
        print(result)

        output_path = (f"{txt_Path}/txt_{i}.TXT")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result)
    
    endTime = datetime.datetime.now() 
    print('process_time =', (endTime - startTime).seconds,'s')

# @img_start:    指定生成的img起始
# @img_end:      指定生成的img结束
def tesseractOCR_img(image_Path = './imgs',txt_Path = './txt', img_start = 0, img_end = 0):
    startTime = datetime.datetime.now()  

    if os.path.exists(image_Path):  # 判断存放图片的文件夹是否存在
        if not os.path.exists(txt_Path):  # 判断txt文件夹是否存在
            os.makedirs(txt_Path) 

        for i in range(img_start,img_end):
            img_path = (f"{image_Path}/page_{i}.PNG")
            result = pytesseract.image_to_string(image=img_path,lang="chi_sim",config="--psm 1")   #路径；语言；配置
            print(result)

            output_path = (f"{txt_Path}/txt_{i}.TXT")
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result)
    
    endTime = datetime.datetime.now()  
    print('process_time =', (endTime - startTime).seconds,'s')

if __name__ == "__main__":

    pdfPath = '../jgsh.pdf'
    # 图片的目录,可默认
    imagePath = '../imgs'
    # txt的目录,可默认
    txtPath = '../txt'

    tesseractOCR_img(imagePath,txtPath,4,238)
    #tesseractOCR_pdf(pdfPath, txtPath, 4.5, 4)

