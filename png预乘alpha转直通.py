from PIL import Image
import os
from sys import argv
import numpy as np


def StraightAlpha(img):
    matrix = np.array(img)
    for row in matrix:
        for pixel in row:
            rgb = pixel[:-1]
            alpha = pixel[-1]
            if alpha != 0 and alpha != 255:
                maxrgb = max(rgb)
                if maxrgb > alpha:
                    for i in range(3):
                        pixel[i] = rgb[i] * 255 // maxrgb
                else:
                    for i in range(3):
                        pixel[i] = rgb[i] * 255 // alpha
    return Image.fromarray(matrix)

def main():
    args = argv

    print("Creat by Satan-23333\nGithub：https://github.com/Satan-23333/PMA-Converter\n")

    try:
        png_path_list = args
        # print(png_path_list)
        if len(png_path_list) < 2:
            print("请把需要修改的png拖放到本程序上捏。\n")
            os.system("pause")
            return

        for i, png_path in enumerate(png_path_list[1:]):
            img = Image.open(png_path)

            print(f"\n第{i+1}张处理中:\t" + png_path + "\n")
            final = StraightAlpha(img)
            result_path, filename = os.path.split(png_path)
            newname = result_path + "\\" + filename.split(".png")[0] + "_bak.png"
            # print(png_path,result_path + newname)

            if os.path.exists(newname):
                os.remove(newname)

            os.rename(png_path, newname)
            result_path = os.path.join(result_path, filename)
            final.save(result_path)

            print("文件修改成功！结果文件保存至:\n" + result_path)
            print("原文件备份至:\n" + newname)
        print("\n完成!\n转换后的png可以用PS修改,修改完用另一个脚本转回直通即可\n")
        os.system("pause")
    except:
        print("请把需要修改的png拖放到本程序上捏。\n")
        os.system("pause")

if __name__ == "__main__":
    main()
