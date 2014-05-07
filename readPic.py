
import sys
import os.path
import struct

def MakePixelArray(inputData, startPos, width, height):
    #Init tmp array
    tmpArray = []

    for y in range(height):
        for x in range(width):
            #Reset this dictionary
            pixel = {}

            #Read color data
            pixel['r'] = struct.unpack_from('<B', inputData, (startPos + ((y * width) + x) * 3) + 2)[0]
            pixel['g'] = struct.unpack_from('<B', inputData, (startPos + ((y * width) + x) * 3) + 1)[0]
            pixel['b'] = struct.unpack_from('<B', inputData, (startPos + ((y * width) + x) * 3) + 0)[0]

            #Add this dictionnary into array
            tmpArray.append(pixel)

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
    BMPHeader = fopen.read(14)
    picStart = struct.unpack_from("<I", BMPHeader, 0x0A)[0]
    print('Start= ', picStart)

    BMPInfo = fopen.read(picStart - 14)
    picWidth = struct.unpack_from('<i', BMPInfo, 4)[0]
    picHeight = struct.unpack_from('<i', BMPInfo, 8)[0]

    BMPColor = fopen.read(int(picWidth) * int(picHeight) * 3)
    print('Width= ')
    print(picWidth)
    print('Height= ')
    print(picHeight)

    print('r= ', struct.unpack_from('<B', BMPColor, 0 + 2)[0])
    print('g= ', struct.unpack_from('<B', BMPColor, 0 + 1)[0])
    print('b= ', struct.unpack_from('<B', BMPColor, 0 + 0)[0])

    print('')

    print('r= ', struct.unpack_from('<B', BMPColor, picWidth*3 + 2)[0])
    print('g= ', struct.unpack_from('<B', BMPColor, picWidth*3 + 1)[0])
    print('b= ', struct.unpack_from('<B', BMPColor, picWidth*3 + 0)[0])


sys.exit(1)

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
