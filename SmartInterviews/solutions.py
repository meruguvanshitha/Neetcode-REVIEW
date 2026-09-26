# Smart Interviews Solutions

# --- 24/09/2026 ---
# Nth Term of GP
def nth_term_gp(a, r, n):
    return a * (r ** (n - 1))

# Compress String
def compress_string(s):
    if not s: return ""
    res = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            res.append(s[i - 1] + str(count))
            count = 1
    res.append(s[-1] + str(count))
    return "".join(res)

# --- Basic Questions ---
# Merge 2 Sorted Arrays
def merge_sorted(arr1, arr2):
    return sorted(arr1 + arr2)

# Intersection of 2 Arrays
def intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

# Reverse String
def reverse_string(s):
    return s[::-1]

# Reverse Number
def reverse_num(n):
    return int(str(n)[::-1])

# Print Array A using B
def print_a_using_b(A, B):
    return [A[i] for i in B if i < len(A)]