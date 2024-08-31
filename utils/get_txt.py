import ast
import os

def compare_list_of_lists_unordered(list1, list2):
    # 首先比较长度
    if len(list1) != len(list2):
        return False
    
    # 对每个子列表进行排序
    sorted_list1 = [sorted(sublist) for sublist in list1]
    sorted_list2 = [sorted(sublist) for sublist in list2]
    
    # 对整个列表进行排序
    sorted_list1.sort()
    sorted_list2.sort()
    
    # 比较排序后的列表
    return sorted_list1 == sorted_list2

def get_ids_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip()  # 读取文件内容

    # 使用 ast.literal_eval 安全地将字符串解析为列表
    coordinates = ast.literal_eval(content)

    # 将嵌套列表平铺成一个单一列表
    flat_list = [item for sublist in coordinates for item in sublist]
    return flat_list

def get_groups_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip()  # 读取文件内容
    ground_truth_list = eval(content)
    return ground_truth_list

if __name__ == '__main__':
    all_file_path = 'new_result'
    for root, dirs, files in os.walk(all_file_path):
        for dir in dirs:
            images_path = os.path.join(all_file_path, dir)
            for root, dirs, files in os.walk(images_path):
                for file in files:
                    if file.endswith('.txt'):
                        file_path = os.path.join(images_path, file)
                        ids = get_groups_from_file(file_path)
                        