#!/usr/bin/env python
#coding: utf-8

import glob
import img2pdf
import sys
import os
from pdf2image import convert_from_path
from PIL import Image


class PdfConvert:
    """
    文本PDF转换成为图片PDF文件输出
    """

    def __init__(self, sourcePdf, targetPdf):
        self.__sourcePdf = sourcePdf
        self.__targetPdf = targetPdf
        self.__tmpDir = './tmpDir/'
        self.__waterMark = './water_logo/water_mark.png'

    # 加水印
    def addWaterMark(self, sourcePic):
        logo = Image.open(self.__waterMark)
        imageSrc = Image.open(sourcePic)
        logo_mask = logo.convert("L").point(lambda x: min(x, 35))
        logo.putalpha(logo_mask)

        # 循环遍历水印
        for i in range(0, 3):
            for j in range(0, 3):
                x = 33 + (374*j)
                y = 250 + (374*i)
                imageSrc.paste(logo, (x, y), mask=logo_mask)
        imageSrc.save(sourcePic, optimize=True)

    # 创建临时文件夹
    def createTmpDir(self):
        if not os.path.exists(self.__tmpDir):
            os.makedirs(self.__tmpDir)

    # 将PDF源文件转换成为图片存放于临时文件夹中
    def convertPdfToTmpDir(self):
        pages = convert_from_path(self.__sourcePdf)
        count = 0
        for page in pages:
            targetPic = self.__tmpDir + 'page-' + str(count+1) + '.jpg'
            page.save(targetPic, 'JPEG')
            # TODO: 给图片加水印
            self.addWaterMark(targetPic)
            count = count + 1

    # 输出源文件
    def ouputFile(self):
        # 获取文件夹中的图片，并按顺序压入列表中
        files = glob.glob(self.__tmpDir + '*')
        pageList = []
        for pageNum in range(1, len(files)+1):
            pageList.append(self.__tmpDir + 'page-' + str(pageNum) + '.jpg')

        # 创建目标文件
        with open(self.__targetPdf, "wb") as f:
            f.write(img2pdf.convert(pageList))

        # 删除临时文件夹中的文件
        for page in pageList:
            if os.path.exists(page):
                os.unlink(page)

    # 执行对应所有的逻辑
    def excute(self):
        self.createTmpDir()
        self.convertPdfToTmpDir()
        self.ouputFile()


def main():
    # 判断出入参数是否正确
    if len(sys.argv) != 3:
        print("python " + os.path.basename(__file__) + " PDF源文件 PDF目标文件")
        sys.exit()

    sourcePdf = sys.argv[1]
    targetPdf = sys.argv[2]

    # 检测传入文件是否存在
    if not os.path.exists(sourcePdf):
        print('PDF源文件：[' + sourcePdf + '] 不存在')

    worker = PdfConvert(sourcePdf, targetPdf)
    worker.excute()


if __name__ == "__main__":
    main()
