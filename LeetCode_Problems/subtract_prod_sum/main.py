import math
def subtract_product_and_sum(n):
    int_arr = [int(i) for i in str(n)]
    product = math.prod(int_arr)
    total = sum(int_arr)
    return product - total

subtract_product_and_sum(4421)