from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def __is_point_in_exist_rect__(point, rects):
    # 判断该点是否是在一个已知的矩形list里 矩形为一个turple,前两个为坐标点，后两个为width height
    for rect in rects:
        x1 = rect[1]
        x2 = x1 + rect[2] - 1
        y1 = rect[0]
        y2 = y1 + rect[3] - 1
        if x1 <= point[3][1] <= x2 and y1 <= point[3][0] <= y2:
            return True
    return False


def __find_rect_by_point__(curr_point, img_array):
    i = curr_point[3][0]
    j = curr_point[3][1]
    # 当确定了i,j是左上角点后，求出该矩形的长宽各占多少像素点
    rect_width = 1
    rect_height = 1
    rows, cols, div = img_array.shape
    last_point = [img_array[i, j][0], img_array[i, j][1], img_array[i, j][2]]
    for row in range(i+1, rows):
        current_point = img_array[row, j]
        if __is_green_point__(last_point) is False and __is_green_point__(current_point) is True:
            break
        else:
            rect_height = rect_height + 1
    last_point = [img_array[i, j][0], img_array[i, j][1], img_array[i, j][2]]
    for col in range(j+1, cols):
        current_point = img_array[i, col]
        if __is_green_point__(last_point) is False and __is_green_point__(current_point) is True:
            break
        else:
            rect_width = rect_width + 1
    rect = (i, j, rect_width, rect_height)
    return rect


def __is_new_img_point(last_point, next_point):
    if __is_green_point__(last_point) is True and __is_green_point__(next_point) is False:
        return True
    else:
        return False


def __is_green_point__(point):
    if point[0] == 0 and point[1] == 255 and point[2] == 0:
        return True
    else:
        return False


def main():
    img = np.array(Image.open('testImg.bmp'))  # 打开图像并转化为数字矩阵
    rects = []
    rows, cols, div = img.shape
    for i in range(rows):
        lst_point = [0, 255, 0, [i, -1]]
        for j in range(cols):
            current_point = [img[i, j][0], img[i, j][1], img[i, j][2], [i, j]]
            if __is_new_img_point(lst_point, current_point) is True:
                if __is_point_in_exist_rect__(current_point, rects) is False:
                    rects.append(__find_rect_by_point__(current_point, img))
            lst_point = current_point
    plt.figure("dog")
    plt.imshow(img)

    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    main()


