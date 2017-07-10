balance = 999999
annualInterestRate = 0.18
MIR = annualInterestRate/12
LB = balance/12
UB = balance*((1+MIR)**12)/12.0
MP= (LB+UB)/2
guessed = True
while guessed:
    bal = balance
    for i in range(12):
        MUBal = bal - MP
        IR = (annualInterestRate/12.0)*MUBal
        bal = MUBal + IR
        #print("Remaining balance: " + str(round(bal,2)))
    if(bal < 0 and bal > -0.01):
        guessed = False
    else:
        if (bal < 0):
            UB = MP
        else:
            LB =MP
    MP= (LB+UB)/2
print("Lowest Payment: " + str(round(MP,2)))
