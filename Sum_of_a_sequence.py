# ======================= Sum of a Sequence =======================
def sequence_sum(begin_number, end_number, step):
    return sum( range(begin_number, end_number + 1, step) )


print(sequence_sum(4, 2, 2))   # Output: 0
print(sequence_sum(2, 2, 2))   # Output: 2
print(sequence_sum(2, 6, 2))   # Output: 12
print(sequence_sum(1, 5, 1))   # Output: 15
print(sequence_sum(1, 5, 3))   # Output: 5
