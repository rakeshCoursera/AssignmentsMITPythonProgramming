def radiationExposure(start, stop, step):
    area=0
    while(start < stop):
        area = area + f(start)*step
        #print(start,area)
        start = start + step
    return area



def f(x):
    import math
    return 60*math.e**(math.log(0.5)/55.6 * x)
