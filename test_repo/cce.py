import pandas as pd

def binary_sort(arr):
    """二分排序函数（基于二分插入排序原理）"""
    sorted_arr = []
    for item in arr:
        left, right = 0, len(sorted_arr)
        while left < right:
            mid = (left + right) // 2
            if item < sorted_arr[mid]:
                right = mid
            else:
                left = mid + 1
        sorted_arr.insert(left, item)
    return sorted_arr

# 读取数据
a = pd.read_csv('data.csv')

# 对某一列进行二分排序（例如 'value' 列）
if 'value' in a.columns:
    a['value'] = binary_sort(a['value'].tolist())

# 保存修改后的数据
a.to_csv('data.csv', index=False)

# 打印形状
print(a.shape)