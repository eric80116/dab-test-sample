import sys

BUNDLE_SRC_PATH = "/Workspace/Users/eric.liou@databricks.com/.bundle/dab_test_sample/dev/files/src"
if BUNDLE_SRC_PATH not in sys.path:
    sys.path.insert(0, BUNDLE_SRC_PATH)


from my_package.pipeline import transform_numbers

def main():
    data = [0, 5, -3]
    result = transform_numbers(data)
    assert result == [0, 10], f"Unexpected result: {result}"
    print("Integration test passed.")

if __name__ == "__main__":
    main()
