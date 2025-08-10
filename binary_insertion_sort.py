def binary_insertion_sort(arr):
    """
    二分插入排序：使用二分查找优化插入排序
    时间复杂度：O(n²) - 比较次数优化为O(n log n)，但移动次数仍为O(n²)
    空间复杂度：O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        # 使用二分查找找到插入位置
        left, right = 0, i
        
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > key:
                right = mid
            else:
                left = mid + 1
        
        # 将元素向右移动，为key腾出位置
        for j in range(i, left, -1):
            arr[j] = arr[j - 1]
        
        # 插入key到正确位置
        arr[left] = key
    
    return arr


def binary_search_position(arr, target, end):
    """
    辅助函数：在已排序的数组前end个元素中找到target的插入位置
    """
    left, right = 0, end
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1
    
    return left


def binary_insertion_sort_v2(arr):
    """
    二分插入排序的另一种实现
    """
    for i in range(1, len(arr)):
        key = arr[i]
        # 找到插入位置
        pos = binary_search_position(arr, key, i)
        
        # 移动元素
        arr[pos + 1:i + 1] = arr[pos:i]
        arr[pos] = key
    
    return arr


def binary_insertion_sort(arr):
    """使用二分查找优化的插入排序"""
    for i in range(1, len(arr)):
        key = arr[i]
        left, right = 0, i

        # 二分查找插入位置
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > key:
                right = mid
            else:
                left = mid + 1

        # 移动元素并插入
        for j in range(i, left, -1):
            arr[j] = arr[j - 1]
        arr[left] = key
        print(f"插入 {key} 到位置 {left}: {arr}")
        print(f"当前数组状态: {arr}")
        print("-" * 40)
        print()

    return arr


def run_test_case(test_name, arr, expected=None):
    """运行单个测试用例"""
    original = arr.copy()
    result = binary_insertion_sort(arr.copy())
    
    # 如果没有提供期望结果，则使用Python内置排序作为参考
    if expected is None:
        expected = sorted(original)
    
    # 验证结果
    is_correct = result == expected
    status = "✅ PASS" if is_correct else "❌ FAIL"
    
    print(f"{test_name}: {status}")
    print(f"  原数组: {original}")
    print(f"  结果:   {result}")
    if not is_correct:
        print(f"  期望:   {expected}")
    print()
    
    return is_correct


def comprehensive_tests():
    """全面的测试用例"""
    print("=" * 60)
    print("二分插入排序 - 全面测试")
    print("=" * 60)
    
    test_results = []
    
    # 1. 基本测试用例
    print("📋 基本测试用例")
    print("-" * 30)
    
    test_results.append(run_test_case(
        "基本排序", 
        [64, 34, 25, 12, 22, 11, 90]
    ))
    
    test_results.append(run_test_case(
        "小数组", 
        [5, 2, 4, 6, 1, 3]
    ))
    
    # 2. 边界测试用例
    print("🔍 边界测试用例")
    print("-" * 30)
    
    test_results.append(run_test_case(
        "空数组", 
        []
    ))
    
    test_results.append(run_test_case(
        "单元素", 
        [42]
    ))
    
    test_results.append(run_test_case(
        "两元素-升序", 
        [1, 2]
    ))
    
    test_results.append(run_test_case(
        "两元素-降序", 
        [2, 1]
    ))
    
    # 3. 特殊情况测试
    print("🎯 特殊情况测试")
    print("-" * 30)
    
    test_results.append(run_test_case(
        "已排序数组", 
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ))
    
    test_results.append(run_test_case(
        "逆序数组", 
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ))
    
    test_results.append(run_test_case(
        "相同元素", 
        [5, 5, 5, 5, 5]
    ))
    
    test_results.append(run_test_case(
        "部分相同", 
        [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    ))
    
    # 4. 数据类型测试
    print("🔢 数据类型测试")
    print("-" * 30)
    
    test_results.append(run_test_case(
        "负数", 
        [-5, -1, -10, 0, 3, -2]
    ))
    
    test_results.append(run_test_case(
        "浮点数", 
        [3.14, 2.71, 1.41, 0.57, 2.23]
    ))
    
    test_results.append(run_test_case(
        "大数", 
        [1000000, 999999, 1000001, 500000]
    ))
    
    # 5. 性能测试用例
    print("⚡ 性能测试用例")
    print("-" * 30)
    
    import random
    
    # 随机数组
    random_arr = [random.randint(1, 100) for _ in range(50)]
    test_results.append(run_test_case(
        "随机数组(50个)", 
        random_arr
    ))
    
    # 部分有序数组
    partially_sorted = list(range(1, 26)) + [random.randint(1, 100) for _ in range(25)]
    test_results.append(run_test_case(
        "部分有序数组", 
        partially_sorted
    ))
    
    # 6. 稳定性测试
    print("🔄 稳定性测试")
    print("-" * 30)
    
    # 使用元组来测试稳定性
    class NumberWithIndex:
        def __init__(self, value, index):
            self.value = value
            self.index = index
        
        def __lt__(self, other):
            return self.value < other.value
        
        def __eq__(self, other):
            return self.value == other.value and self.index == other.index
        
        def __repr__(self):
            return f"({self.value},{self.index})"
    
    # 创建有重复值的数组来测试稳定性
    stability_test = [NumberWithIndex(3, 1), NumberWithIndex(1, 2), 
                     NumberWithIndex(3, 3), NumberWithIndex(2, 4), 
                     NumberWithIndex(1, 5)]
    
    original_stability = stability_test.copy()
    sorted_stability = binary_insertion_sort(stability_test.copy())
    
    # 检查稳定性：相同值的元素应该保持原有顺序
    is_stable = True
    for i in range(len(sorted_stability) - 1):
        if (sorted_stability[i].value == sorted_stability[i + 1].value and 
            sorted_stability[i].index > sorted_stability[i + 1].index):
            is_stable = False
            break
    
    print(f"稳定性测试: {'✅ PASS' if is_stable else '❌ FAIL'}")
    print(f"  原数组: {original_stability}")
    print(f"  排序后: {sorted_stability}")
    print(f"  稳定性: {'保持' if is_stable else '未保持'}")
    print()
    
    test_results.append(is_stable)
    
    # 7. 算法比较测试
    print("📊 算法比较测试")
    print("-" * 30)
    
    import time
    
    sizes = [100, 500, 1000]
    
    for size in sizes:
        test_data = [random.randint(1, 1000) for _ in range(size)]
        
        # 测试二分插入排序
        data1 = test_data.copy()
        start_time = time.time()
        binary_insertion_sort(data1)
        binary_time = time.time() - start_time
        
        # 测试传统插入排序
        data2 = test_data.copy()
        start_time = time.time()
        traditional_insertion_sort(data2)
        traditional_time = time.time() - start_time
        
        # 测试Python内置排序
        data3 = test_data.copy()
        start_time = time.time()
        data3.sort()
        builtin_time = time.time() - start_time
        
        print(f"数组大小: {size}")
        print(f"  二分插入排序: {binary_time:.6f} 秒")
        print(f"  传统插入排序: {traditional_time:.6f} 秒")
        print(f"  Python内置排序: {builtin_time:.6f} 秒")
        if traditional_time > 0:
            print(f"  性能提升: {traditional_time/binary_time:.2f}x (vs 传统插入)")
        print()
    
    # 测试结果统计
    print("=" * 60)
    print("测试结果统计")
    print("=" * 60)
    
    passed = sum(test_results)
    total = len(test_results)
    
    print(f"总测试数: {total}")
    print(f"通过数: {passed}")
    print(f"失败数: {total - passed}")
    print(f"通过率: {passed/total*100:.1f}%")
    
    if passed == total:
        print("🎉 所有测试通过！")
    else:
        print("⚠️  存在测试失败，请检查代码")


def interactive_test():
    """交互式测试"""
    print("\n" + "=" * 60)
    print("交互式测试模式")
    print("=" * 60)
    print("输入数字序列（用空格分隔），输入 'quit' 退出")
    
    while True:
        try:
            user_input = input("\n请输入数组: ").strip()
            
            if user_input.lower() == 'quit':
                print("退出交互式测试")
                break
            
            if not user_input:
                continue
            
            # 解析输入
            arr = list(map(float, user_input.split()))
            
            # 转换为整数（如果可能）
            if all(x.is_integer() for x in arr):
                arr = [int(x) for x in arr]
            
            original = arr.copy()
            result = binary_insertion_sort(arr)
            
            print(f"原数组: {original}")
            print(f"排序后: {result}")
            
        except ValueError:
            print("输入格式错误，请输入数字序列（用空格分隔）")
        except KeyboardInterrupt:
            print("\n退出交互式测试")
            break


if __name__ == "__main__":
    # 运行全面测试
    comprehensive_tests()
    
    # 可选：运行交互式测试
    # interactive_test()
