# tests/unit/my_package/test_pipeline.py
from my_package.pipeline import transform_numbers

def test_transform_numbers_basic():
    assert transform_numbers([1, 2, 3]) == [2, 4, 6]

def test_transform_numbers_filter_negative():
    assert transform_numbers([-1, 0, 5]) == [0, 10]
