""" 辅助程序 """
import os

from ReadBMPFile import ReadBMPFile

filePaths = [
    'C:/Users/sduwo/Desktop/019乐高打印机/25x25 BMP图像/点-微软雅黑-18字号-25x25.bmp',
    'C:/Users/sduwo/Desktop/019乐高打印机/25x25 BMP图像/赞-微软雅黑-18字号-25x25.bmp',
    'C:/Users/sduwo/Desktop/019乐高打印机/25x25 BMP图像/三-微软雅黑-18字号-25x25.bmp',
    'C:/Users/sduwo/Desktop/019乐高打印机/25x25 BMP图像/连-微软雅黑-18字号-25x25.bmp'
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
