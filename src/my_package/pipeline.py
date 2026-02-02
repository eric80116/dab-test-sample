# src/my_package/pipeline.py

def transform_numbers(nums):
    # 簡單邏輯：去除負數，每個數乘以 2
    return [n * 2 for n in nums if n >= 0]
