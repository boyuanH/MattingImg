from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def main():
    img = np.array(Image.open('D:/Temp/205.jpg'))  # 打开图像并转化为数字矩阵
    rects = [];
    rows, cols, div = img.shape
    for i in range(rows):
        lst_point = [0,255,0]
        for j in range(cols):
            current_point = [img[i, j][0], img[i, j][1], img[i, j][2]]
            if __is_new_img_point(lst_point,current_point) is True:
                if __is_point_in_exist_rect__(current_point,rects) is False:
                    rects.append(__find_rect_by_point__(current_point))
            lst_point = current_point



    plt.figure("dog")
    plt.imshow(img)

    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    main()


def __is_point_in_exist_rect__(point, rects):
    # 判断该点是否是在一个已知的矩形list里 矩形为一个turple,前两个为坐标点，后两个为width height
    pass


def __find_rect_by_point__(i, j):
    # 当确定了i,j是左上角点后，求出该矩形的长宽各占多少像素点
    pass


def __is_new_img_point(last_point,next_point):
    if __is_green_point__(last_point) is True and __is_green_point__(next_point) is False:
        return True
    else:
        return False


def __is_green_point__(point):
    if point[0] == 0 and point[1] == 255 and point[2] == 0:
        return True
    else:
        return False
