import cv2
import numpy as np
import os
import sys
import time

all_image_path = "new_result"

for root, dirs, files in os.walk(all_image_path):
    for dir in dirs:
        images_path = os.path.join(all_image_path, dir)
        for root, dirs, files in os.walk(images_path):
            for file in files:
                if file.endswith('.jpg'):
                    file_path = os.path.join(images_path, file)
                    txt_file_path = file_path.replace('.jpg', '.txt')
                    
                    if os.path.exists(txt_file_path):
                        print(f"已存在坐标文件：{txt_file_path}")
                        continue
                    img = cv2.imread(file_path)
                    cv2.imshow(f'file_path', img)
                    cv2.waitKey(50)
                    # 获取用户输入
                    print(f"Loading image: {file_path}")
                    user_input = input("请输入坐标，用逗号分隔，然后按回车键: (例如输入: 58 59,60)\n")  
                    # 解析输入，转换成列表形式
                    coordinates = user_input.strip().split(",")
                    coordinate_list = [list(map(int, coord.strip().split())) for coord in coordinates]
                    
                    # 保存到同路径下的同名txt文件
                    with open(txt_file_path, 'w') as txt_file:
                        txt_file.write(str(coordinate_list))

                    print(f"坐标已保存到：{txt_file_path}")
                    
cv2.destroyAllWindows()  # 确保所有窗口关闭
