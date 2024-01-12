from PIL import Image
import os
from sys import argv
import numpy as np


def premultiplyAlpha(img):
    matrix = np.array(img, dtype=int)
    for row in matrix:
        for pixel in row:
            if pixel[3] == 255:
                continue
            elif pixel[3] == 0:
                pixel[0] = pixel[1] = pixel[2] = 0
            else:
                for i in range(3):
                    pixel[i] = pixel[i] * pixel[3] / 255

    matrix = matrix.astype("uint8")
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
            final = premultiplyAlpha(img)
            result_path, filename = os.path.split(png_path)
            newname = result_path + "\\" + filename.split(".png")[0] + "_bak.png"
            # print(png_path,result_path + newname)

            if os.path.exists(newname):
                os.remove(newname)

            os.rename(png_path, newname)
            result_path = os.path.join(result_path, filename)  # 生成的结果文件放在脚本目录下
            final.save(result_path)

            print("文件修改成功！结果文件保存至:\n" + result_path)
            print("原文件备份至:\n" + newname)
        print("\n完成!\n转换后的png在软件和游戏内能正常显示\n")
        os.system("pause")
    except:
        print("请把需要修改的png拖放到本程序上捏。\n")
        os.system("pause")


if __name__ == "__main__":
    main()
