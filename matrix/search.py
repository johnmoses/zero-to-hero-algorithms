""" 
Search
"""
arr = [
    [0, 6, 8, 9, 11],
    [20, 22, 28, 29, 31],
    [36, 38, 50, 61, 63],
    [64, 66, 100, 122, 128]
]
x = 8

def search(arr, x):
    rows, cols = len(arr), len(arr[0])

    # Traverse each row and column
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == x:
                return True
    return False

print(search(arr, x))