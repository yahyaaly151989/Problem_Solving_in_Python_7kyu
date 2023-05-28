# =================== Calculate Julie's Age ===================
def age(x, y):
    brother_age = x / (y -1)
    her_age = brother_age + x
    return round(her_age)
    
# her_age / her_age = (brother_age + x ) / (brother_age * y)

# 1 = (brother_age + x ) / (brother_age * y)

# 1 * (brother_age * y) = (brother_age + x )

# (brother_age * y) - brother_age = x

# brother_age(y - 1) = x

# brother_age = x / (y -1)


print(age(6, 3)) # 9
print(age(-15, 0.25)) # 5

