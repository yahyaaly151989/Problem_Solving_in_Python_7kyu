# ==================== Product of Largest Pair ====================
def max_product(a):
    max1 = max(a)
    a.remove(max1)
    max2 = max(a)
    return max1 * max2
 
print(max_product([2, 1, 5, 0, 4, 3]))