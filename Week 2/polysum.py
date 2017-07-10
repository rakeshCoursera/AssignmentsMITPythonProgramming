import math
def polysum(n,s):
    area=(0.25*n*s*s )/ (math.tan((math.pi)/n))
    perimeter = n*s
    SUM = area + perimeter**2
    return round(SUM,4)
