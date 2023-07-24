import fitz  # fitz就是pip install PyMuPDF
import datetime
import os


# @pdf_zoom:         pdf图像缩放
# @pdf_startpage:    指定pdf起始页
def pyMuPDF_fitz(pdf_Path, image_Path, pdf_zoom = 2.0, pdf_startpage = 0):
    startTime_pdf2img = datetime.datetime.now()  # 开始时间

    pdfDoc = fitz.open(pdf_Path)
    for i in range(pdf_startpage,pdfDoc.page_count):
        page = pdfDoc[i]
        rotate = int(0)
        # 每个尺寸的缩放系数
        mat = fitz.Matrix(pdf_zoom, pdf_zoom).prerotate(rotate)
        pix = page.get_pixmap(matrix=mat, alpha=False)

        if not os.path.exists(image_Path):  # 判断存放图片的文件夹是否存在
            os.makedirs(image_Path)  # 若图片文件夹不存在就创建
        
        pix.save(f"{image_Path}/page_{i}.png",'png')  # 将图片写入指定的文件夹内
        print('page: '+ str(i) +' done')

    endTime_pdf2img = datetime.datetime.now()  # 结束时间
    print('process_time =', (endTime_pdf2img - startTime_pdf2img).seconds,'s')


if __name__ == "__main__":
    # 1、PDF地址
    pdfPath = '../jgsh.pdf'
    # 2、需要储存图片的目录
    imagePath = '../imgs'
    pyMuPDF_fitz(pdfPath, imagePath, 4.5, 4)

