# from utils.gpt4v import handle as gpt_handle
from utils.gemini import handle as gemini_handle
import os
import cv2
from utils.get_txt import get_ids_from_file, get_groups_from_file, compare_list_of_lists_unordered

if __name__ == '__main__':
    all_file_path = 'new_result/'
    total_cnt = 0
    success_cnt = 0

    for root, dirs, files in os.walk(all_file_path):
        for dir in dirs:    # 遍历场景文件夹
            images_path = os.path.join(all_file_path, dir)
            for root, dirs, files in os.walk(images_path):  # 遍历图片文件夹
                for file in files:
                    if file.endswith('.txt'):
                        continue
                    if file.endswith('.jpg'):
                        total_cnt += 1
                        image_path = os.path.join(images_path, file)
                        image = cv2.imread(image_path)
                        ground_truth_file_path = image_path.replace('.jpg', '.txt')
                        ground_truth_ids = get_ids_from_file(ground_truth_file_path)
                        ground_truth_groups = get_groups_from_file(ground_truth_file_path)

                        # group_list = gpt_handle(image,ground_truth_ids)
                        group_list = gemini_handle(image)
                        print(f"GPT Group List in {image_path}: {group_list}")
                        print(f"G.T Group List in {ground_truth_file_path}: {ground_truth_groups}") 
                        if compare_list_of_lists_unordered(group_list, ground_truth_groups):
                            print("GPT4V Grouping is correct")
                            success_cnt += 1
                        else:
                            print("GPT4V Grouping is incorrect")

    print(f"success rate: {success_cnt}/{total_cnt}")