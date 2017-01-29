from sklearn import svm
import numpy as np
from PIL import Image

clf = svm.SVC()
X = np.array([[140, 102, 25], [116, 89, 34], [117, 96, 60], [132, 107, 56], [147, 117, 54], [141, 107, 44], [112, 88, 45], [114, 97, 56], [101, 84, 48], [154, 119, 48], [124, 101, 53], [136, 113, 65], [140, 107, 52], [152, 127, 73], [120, 95, 49], [111, 89, 47], [119, 94, 54], [159, 129, 62], [141, 105, 32], [104, 86, 43], [105, 83, 43], [114, 87, 45], [182, 172, 145], [86, 66, 36], [104, 88, 53], [112, 95, 57], [235, 224, 170], [228, 208, 147], [216, 197, 163], [146, 111, 41], [230, 212, 160], [214, 194, 134], [194, 184, 146], [202, 185, 132], [234, 223, 157], [192, 177, 129], [144, 109, 35], [225, 210, 159], [218, 200, 129], [148, 104, 24], [140, 100, 31], [233, 216, 161], [228, 213, 155], [116, 83, 38], [216, 195, 146], [227, 204, 143], [207, 192, 139], [209, 193, 140], [206, 193, 148], [191, 177, 134], [218, 192, 132], [196, 181, 130], [242, 218, 132], [200, 186, 128], [187, 176, 117], [220, 196, 136], [69, 49, 39], [76, 57, 49], [103, 70, 55], [97, 87, 83], [104, 69, 29], [144, 109, 82], [112, 109, 110], [129, 89, 66], [153, 128, 88], [121, 99, 92], [124, 104, 99], [145, 92, 31], [119, 101, 98], [61, 43, 35], [110, 101, 101], [165, 137, 118], [121, 112, 112], [133, 113, 102], [116, 76, 40], [97, 90, 91], [114, 106, 102], [184, 147, 114], [122, 109, 105], [128, 116, 114], [128, 113, 105], [120, 111, 110], [111, 101, 102], [113, 97, 94], [111, 103, 102], [137, 121, 110], [99, 87, 84], [126, 103, 92], [84, 60, 37], [130, 115, 109], [167, 130, 99], [115, 104, 102], [138, 113, 95], [163, 120, 93], [119, 109, 106], [169, 135, 107], [121, 107, 102], [133, 109, 99], [92, 84, 84], [114, 102, 97], [141, 123, 108], [108, 93, 88], [126, 117, 115], [122, 104, 101], [103, 95, 96], [102, 95, 94], [119, 115, 117], [122, 113, 106], [159, 127, 104], [120, 116, 116], [128, 109, 98], [128, 109, 93], [109, 100, 99], [136, 119, 112], [99, 92, 92], [96, 89, 87], [182, 142, 108], [115, 101, 98], [134, 118, 110], [143, 123, 110], [156, 118, 91], [164, 119, 92], [147, 114, 92], [146, 123, 107], [165, 114, 74], [128, 107, 91], [111, 98, 98], [151, 126, 110], [93, 84, 84], [114, 94, 85], [108, 88, 80], [142, 116, 96], [115, 108, 109], [123, 113, 114], [162, 127, 104], [143, 128, 120], [126, 110, 100], [125, 116, 114], [95, 90, 92], [152, 137, 128], [132, 119, 114], [124, 113, 110], [111, 108, 112], [110, 77, 53], [154, 117, 92], [113, 99, 95], [129, 118, 114], [139, 110, 92], [122, 109, 103], [112, 99, 96], [103, 98, 99], [179, 136, 106], [129, 115, 108], [142, 113, 88], [132, 109, 98], [149, 121, 108], [102, 93, 92], [159, 124, 98], [177, 134, 99], [180, 134, 100], [118, 112, 112], [143, 123, 111], [140, 117, 102], [141, 128, 122], [115, 102, 101], [83, 72, 71], [107, 106, 103], [53, 42, 39], [103, 107, 104], [65, 61, 61], [42, 35, 32], [51, 40, 36], [45, 36, 32], [64, 52, 48], [40, 30, 24], [44, 38, 34], [69, 59, 56], [46, 38, 33], [58, 48, 44], [44, 37, 35], [44, 37, 35], [59, 50, 48], [43, 36, 34], [52, 45, 42], [54, 46, 43], [57, 51, 49], [54, 41, 36], [72, 64, 62], [52, 46, 44], [44, 38, 35], [50, 39, 34], [51, 42, 40], [161, 122, 109], [48, 40, 36], [64, 57, 55], [173, 130, 116], [50, 46, 46], [141, 99, 80], [152, 111, 93], [171, 120, 101], [47, 37, 33], [176, 130, 108], [44, 40, 41], [48, 40, 37], [167, 124, 108], [162, 119, 105], [139, 101, 88], [173, 124, 106], [173, 126, 108], [106, 77, 56], [38, 30, 27], [164, 116, 96], [178, 132, 116], [168, 121, 104], [162, 118, 101], [169, 126, 107], [43, 32, 27], [162, 120, 102], [162, 121, 111], [42, 39, 39], [155, 108, 92], [107, 82, 78], [40, 27, 22], [85, 43, 40], [32, 22, 18], [91, 54, 32], [39, 25, 20], [43, 29, 25], [35, 24, 20], [76, 46, 30], [79, 53, 36], [64, 43, 32], [87, 63, 44], [38, 24, 18], [76, 40, 29], [37, 26, 20], [36, 23, 18], [87, 51, 34], [96, 61, 33], [72, 45, 33], [130, 82, 35], [84, 54, 45], [105, 67, 39], [78, 50, 41], [38, 27, 21], [96, 62, 44], [41, 23, 19], [54, 30, 22], [91, 61, 40], [39, 24, 20], [37, 23, 19], [73, 47, 39], [141, 112, 62], [88, 56, 40], [134, 109, 68]])
    #[138, 92, 32], [45, 26, 22], [39, 25, 23], [83, 59, 46], [94, 75, 69], [184, 127, 31], [153, 133, 98], [65, 47, 37], [56, 33, 21], [172, 121, 27], [78, 59, 41], [58, 37, 23], [67, 50, 39], [58, 36, 22], [69, 49, 35], [59, 43, 32], [50, 30, 18], [159, 104, 56], [147, 97, 50], [149, 102, 63], [66, 50, 41], [148, 102, 67], [144, 94, 58], [157, 106, 65], [168, 113, 54], [159, 104, 53], [71, 46, 31], [167, 110, 59], [162, 116, 81], [69, 53, 42], [164, 106, 55], [44, 27, 16], [130, 84, 49], [170, 118, 72], [158, 113, 81], [175, 115, 57], [58, 38, 24], [151, 97, 52], [134, 92, 57], [52, 31, 18], [146, 98, 64], [129, 104, 68], [30, 17, 10], [81, 66, 56], [155, 98, 40], [135, 92, 57], [52, 32, 17], [138, 87, 49], [132, 87, 54], [53, 44, 39], [28, 14, 9], [132, 96, 63], [153, 121, 78], [111, 73, 50], [149, 117, 81], [119, 77, 47], [197, 181, 137], [190, 176, 154], [190, 167, 112], [191, 178, 147], [185, 158, 106], [190, 162, 97], [117, 77, 45], [196, 183, 159], [198, 176, 128], [189, 174, 142], [167, 151, 129], [187, 174, 145], [197, 183, 141], [187, 172, 144], [194, 179, 147], [180, 151, 89], [197, 185, 150], [196, 183, 155], [192, 179, 148], [183, 166, 132], [218, 208, 171], [215, 206, 164], [180, 165, 128], [148, 115, 76], [157, 127, 85], [148, 110, 67], [138, 103, 67], [135, 91, 57], [112, 69, 46], [132, 82, 42], [143, 110, 71], [150, 118, 78], [140, 106, 70], [139, 111, 74], [133, 99, 64], [145, 109, 74], [126, 98, 60], [97, 57, 33], [154, 124, 80], [99, 58, 32], [210, 172, 81], [206, 173, 90], [137, 99, 61], [168, 128, 58], [141, 111, 58], [109, 65, 32], [120, 82, 45], [150, 115, 66], [202, 162, 75], [130, 101, 58], [109, 81, 49], [77, 59, 39], [162, 107, 37], [91, 55, 37], [182, 130, 62], [115, 72, 48], [226, 183, 133], [204, 153, 108], [116, 78, 49], [108, 70, 51], [113, 68, 41], [225, 171, 101], [121, 78, 52], [150, 115, 80], [90, 56, 38], [80, 47, 29], [225, 174, 104], [105, 68, 47], [224, 162, 95], [108, 67, 43], [129, 85, 54], [103, 67, 42], [150, 96, 48], [126, 83, 50], [93, 58, 40], [111, 72, 50], [230, 172, 105], [215, 150, 93], [117, 74, 46], [102, 66, 45], [79, 46, 30], [106, 68, 44], [223, 164, 99], [229, 171, 100], [93, 55, 34], [106, 67, 44], [101, 64, 43], [222, 163, 99], [88, 52, 34], [93, 60, 41], [226, 167, 105], [115, 74, 47], [103, 67, 42], [239, 179, 106], [221, 164, 101], [235, 183, 109], [201, 142, 70], [102, 64, 41], [227, 171, 105], [229, 171, 103], [222, 162, 100], [104, 68, 47], [107, 70, 46], [96, 60, 39], [228, 175, 105], [85, 51, 33], [217, 156, 94], [233, 179, 107], [227, 166, 102], [222, 168, 101], [240, 179, 104], [218, 161, 95], [230, 168, 95], [230, 171, 100], [236, 172, 100], [227, 171, 103], [224, 169, 98], [224, 167, 103], [213, 164, 100], [227, 160, 96], [216, 159, 96], [226, 173, 100], [98, 61, 42], [220, 158, 95], [214, 149, 93], [227, 175, 105], [88, 58, 42], [230, 170, 100], [227, 166, 97], [83, 57, 45], [127, 73, 43], [235, 182, 107], [86, 57, 41], [217, 160, 96], [234, 183, 108], [222, 157, 98], [100, 67, 47], [79, 49, 32], [234, 178, 108], [85, 59, 45], [226, 166, 98], [220, 165, 100], [80, 46, 30], [243, 193, 114], [214, 152, 91], [225, 161, 98], [208, 160, 107], [69, 46, 39], [193, 143, 96], [186, 134, 93], [172, 121, 88], [173, 126, 90], [186, 137, 94], [196, 146, 97], [176, 128, 92], [205, 158, 111], [177, 120, 57], [108, 72, 51], [161, 132, 102], [104, 72, 48], [172, 115, 49], [162, 115, 50], [113, 79, 51], [189, 135, 65], [95, 62, 44], [101, 62, 40], [160, 105, 55], [153, 99, 44], [181, 121, 64], [106, 72, 52], [110, 74, 50], [93, 57, 39], [112, 74, 50], [108, 71, 48], [114, 71, 47], [149, 94, 46], [176, 126, 91], [188, 137, 93], [167, 116, 85], [174, 127, 90], [174, 126, 90], [173, 123, 92], [175, 126, 92], [208, 174, 125], [215, 178, 119], [181, 135, 94], [181, 131, 92], [172, 122, 88], [186, 136, 95], [170, 124, 89], [162, 119, 90], [159, 112, 85], [187, 148, 108], [188, 137, 94], [168, 115, 84], [172, 119, 85], [174, 128, 93], [21, 16, 15], [180, 125, 88], [168, 117, 85], [180, 131, 89], [158, 109, 85], [163, 115, 89], [204, 155, 100], [166, 115, 86], [105, 64, 40], [136, 82, 49], [102, 61, 41], [227, 164, 102], [87, 54, 34], [104, 68, 44], [97, 58, 38], [102, 64, 41], [180, 123, 61], [104, 65, 44], [105, 67, 46], [226, 163, 99], [83, 48, 29], [107, 69, 49], [158, 101, 54], [91, 56, 38], [233, 177, 108], [105, 65, 43], [98, 59, 39], [231, 172, 103], [230, 172, 105], [103, 69, 50], [231, 172, 106], [100, 63, 43], [232, 175, 106], [175, 116, 61], [130, 76, 45], [193, 169, 139], [233, 177, 108], [237, 181, 111], [235, 179, 107], [109, 73, 46], [94, 58, 39], [112, 72, 50], [107, 69, 49], [230, 171, 103], [93, 61, 43], [103, 65, 44], [99, 65, 43], [205, 147, 73], [109, 74, 49], [105, 67, 46], [191, 156, 120], [79, 45, 27], [102, 65, 44], [132, 78, 46], [159, 102, 54], [236, 183, 114], [83, 48, 32], [99, 62, 40], [219, 156, 98], [233, 175, 108], [175, 116, 61], [80, 47, 31], [99, 60, 39], [107, 67, 44], [92, 55, 33], [232, 175, 106], [228, 169, 104], [231, 173, 106], [223, 165, 99], [100, 63, 43], [103, 65, 42], [85, 51, 34], [101, 65, 44], [109, 75, 52], [119, 82, 56], [241, 182, 105], [194, 169, 138], [233, 172, 105], [223, 170, 101], [232, 174, 105], [103, 67, 48], [238, 181, 111], [95, 64, 49], [113, 77, 49], [232, 176, 107], [168, 130, 95], [196, 152, 78], [233, 174, 102], [230, 178, 108], [75, 55, 48], [106, 67, 44], [103, 70, 49], [112, 67, 42], [106, 67, 44], [219, 161, 98], [94, 58, 40], [90, 52, 34], [93, 61, 43], [112, 72, 50], [99, 65, 44], [76, 44, 28], [109, 74, 49], [102, 65, 44], [187, 152, 119], [99, 62, 40], [205, 147, 73], [83, 48, 32], [80, 47, 31], [219, 156, 98], [92, 55, 34], [227, 169, 104], [103, 65, 43], [85, 51, 34], [223, 165, 99], [101, 65, 44], [109, 75, 52], [119, 82, 57], [240, 182, 105], [233, 172, 105], [223, 170, 101], [102, 67, 48], [95, 64, 49], [230, 171, 101], [231, 177, 106], [75, 55, 48], [107, 92, 64], [88, 69, 59], [92, 74, 56], [128, 105, 74], [101, 80, 69], [91, 72, 59], [95, 78, 68], [124, 98, 62], [88, 76, 58], [112, 93, 67], [86, 74, 54], [123, 101, 71], [78, 62, 41], [113, 96, 70], [121, 97, 71], [100, 79, 58], [95, 84, 83], [114, 87, 60], [105, 81, 55], [106, 90, 67], [88, 60, 23], [105, 86, 54], [124, 106, 74], [128, 105, 73], [130, 103, 70], [115, 94, 62], [111, 92, 65], [163, 127, 92], [217, 178, 100], [65, 54, 47], [172, 106, 51], [217, 186, 107], [136, 120, 96], [158, 96, 34], [207, 139, 54], [132, 104, 74], [202, 172, 113], [143, 123, 100], [120, 103, 89], [116, 90, 67])
y = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,9,1,1,1,9,9,9,1,9,9,9,9,9,9,1,9,9,1,1,9,9,1,9,9,9,9,9,9,9,9,9,9,9,9,2,2,2,8,11,8,8,8,12,8,8,11,8,2,8,8,8,8,11,8,8,8,8,8,8,8,8,8,8,8,8,8,2,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,2,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,12,2,12,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,5,2,2,5,2,5,5,5,2,5,2,2,5,5,5,5,5,12,2,5,5,5,5,5,2,5,5,2,5,5,1,4,1,4,1,1,1,2,2,2,2,1,2,1,1,2,2,2,2,2,2,2,1,2,2,2,2,1,1,2,11,2,11])
X.reshape(1,-1)
y.reshape(1,-1)
clf.fit(X, y)	



def rgb(path):
    pic = Image.open(path)
    imgData = pic.load()

    r, g, b = 0, 0, 0
    count = 0
    for x in xrange(pic.size[0]):
        for y in xrange(pic.size[1]):
            tempr,tempg,tempb = imgData[x,y]
            r += tempr
            g += tempg
            b += tempb
            count = count +1

    c = (r, g, b)
    return [r/count, g/count, b/count]

def identify(path):	
    print(clf.predict(rgb(path)))
    
for x in range(0,38):
    print(identify('cell-re'+ str(x) +'.jpg'))   