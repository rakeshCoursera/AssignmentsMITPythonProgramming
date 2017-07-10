balance = 3926
annualInterestRate = 0.2
SS=10
MFMP=0
guessed = True
while guessed:
    bal = balance
    for i in range(12):
        MUBal = bal - MFMP
        IR = (annualInterestRate/12.0)*MUBal
        bal = MUBal + IR
        #print("Remaining balance: " + str(round(bal,2)))
    if(bal <= 0):
        guessed = False
    else:
        MFMP += SS
    #print ("Minimum fixed monthly payment: " + str(MFMP))
print("Lowest Payment: " + str(MFMP))
