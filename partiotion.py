import numpy as np

np.random.seed(42)           # To freeze randomness so we both get same result
arr = np.random.randint(1,100,15)    # 15 random values between 1-100
k = 5

print("Original array:", arr)

idx = np.argpartition(arr, k)
part = arr[idx]

print("\nAfter partition(k=5):", part)
print("Smallest 5:", part[:k])         # NOT sorted inside
print("Remaining (includes largest):", part[k:])  # NOT sorted inside
