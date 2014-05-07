#!/usr/sbin/python

import sys
import os.path
import struct

def MakePixelArray(inputData, startPos, width, height):
    #Init tmp array
    tmpArray = [width * height]

    for y in range(height):
        for x in range(width):
            #Reset this dictionary
            pixel = {}

            #Read color data
            pixel['r'] = struct.unpack_from('<B', inputData, (startPos + ((y * width) + x) * 3) + 2)[0]
            pixel['g'] = struct.unpack_from('<B', inputData, (startPos + ((y * width) + x) * 3) + 1)[0]
            pixel['b'] = struct.unpack_from('<B', inputData, (startPos + ((y * width) + x) * 3) + 0)[0]

            #Add this dictionnary into array
            #tmpArray.append(pixel)
            tmpArray[y * width + x] = pixel

    return tmpArray

#User can input the path
#filePath = input('Get me the path of picture you want to blur: ')
#print('Your input is:', filePath)

filePath = './cat.bmp'

#Check if file exist
if os.path.isfile(filePath):
    print('File exist, start working!')
else:
    print('What\'s your problem?')
    sys.exit(1)

#Read from picture
with open(filePath, 'rb') as fopen:
    picData = fopen.read()

#Get width and height of picture
picWidth = struct.unpack_from("<i", picData, 0x12)[0]
picHeight = struct.unpack_from("<i", picData, 0x16)[0]

#Get the start position of color data
picStart = struct.unpack_from("<I", picData, 0x0A)[0]

#Get the depth of this picture
picDepth = struct.unpack_from("<H", picData, 0x1C)[0]

print('picWidth= ', picWidth)
print('picHeight= ', picHeight)
print('picStart= ', picStart)
print('picDepth= ', picDepth)

picArray = []
picArray = MakePixelArray(picData, picStart, picWidth, picHeight)

print('r= ', picArray[2816]['r'])
print('g= ', picArray[2816]['g'])
print('b= ', picArray[2816]['b'])

if picDepth != 24:
    print('Sorry, we only handle 24bits picture, bye')
    sys.exit(1)
