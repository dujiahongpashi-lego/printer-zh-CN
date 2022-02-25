"""
辅助程序
这个地址可以生成点阵字符：https://www.qqxiuzi.cn/zh/dianzhenzi-zifu/
视频求赞求三连
↑↑↑↑↑↑↑↑↑↑↑↑这句话你可能都看烦了吧？
因为点赞三连什么的对视频真的很重要，所以我才这样百般讨要，抱歉抱歉，影响你的体验了。
"""
import os

from ReadBMPFile import ReadBMPFile

filePaths = [
    'C:/Users/sduwo/Desktop/019乐高打印机/25x25 BMP图像/点-微软雅黑-18字号-25x25.bmp',
    'C:/Users/sduwo/Desktop/019乐高打印机/25x25 BMP图像/赞-微软雅黑-18字号-25x25.bmp',
    'C:/Users/sduwo/Desktop/019乐高打印机/25x25 BMP图像/三-微软雅黑-18字号-25x25.bmp',
    'C:/Users/sduwo/Desktop/019乐高打印机/25x25 BMP图像/连-微软雅黑-18字号-25x25.bmp',
    'C:/Users/sduwo/Desktop/019乐高打印机/25x25 BMP图像/关-微软雅黑-18字号-25x25.bmp',
    'C:/Users/sduwo/Desktop/019乐高打印机/25x25 BMP图像/注-微软雅黑-18字号-25x25.bmp',
    'C:/Users/sduwo/Desktop/019乐高打印机/25x25 BMP图像/禁-微软雅黑-18字号-25x25.bmp',
    'C:/Users/sduwo/Desktop/019乐高打印机/25x25 BMP图像/止-微软雅黑-18字号-25x25.bmp',
    'C:/Users/sduwo/Desktop/019乐高打印机/25x25 BMP图像/吸-微软雅黑-18字号-25x25.bmp',
    'C:/Users/sduwo/Desktop/019乐高打印机/25x25 BMP图像/烟-微软雅黑-18字号-25x25.bmp',
    'C:/Users/sduwo/Desktop/019乐高打印机/25x25 BMP图像/smoke-icon-25x25.bmp',
]

legoPrinterResolution = ['025', '025']
bmpBinList = []
bmpBinStrList = []
for filePath in filePaths:
    bmpFile = ReadBMPFile(filePath)
    bmpData = bmpFile.bmp_data
    bmpBinStr = ''
    for line in bmpData:
        lineBinList = []
        for pixel in line:
            pixelBin = [0, 1][pixel[0] > 0]
            lineBinList.append(pixelBin)
            bmpBinStr += str(pixelBin)
            print([' ', '■'][pixelBin], ' ', end="")
        print()
    print()
    bmpBinStrList.append(bmpBinStr)
    bmpBinList.append([os.path.basename(filePath), bmpBinStr])

"""
for bmpBinStr in bmpBinStrList:
    print('二进制：')
    print(bmpBinStr, 2)
    print('十六进制：')
    hexStr = hex(int(bmpBinStr, 2))
    print(hexStr)
    print('乐高编程汉字字体完整字符串：')
    print(legoPrinterResolution[0] + legoPrinterResolution[1] + hexStr[2: len(hexStr) - 1])
"""

for bmpBin in bmpBinList:
    hexStr = hex(int(bmpBin[1], 2))
    print(bmpBin[0], '乐高编程汉字字体完整字符串：')
    print(legoPrinterResolution[0] + legoPrinterResolution[1] + hexStr[2: len(hexStr) - 1])
