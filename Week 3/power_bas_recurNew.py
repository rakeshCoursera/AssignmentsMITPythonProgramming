def recurPowerNew(base, exp):
    if exp==0:
        return 1;
    else:
        if exp%2==0:
            return recurPowerNew(base*base, exp/2)
        else:
            return base * recurPowerNew(base, exp-1)
