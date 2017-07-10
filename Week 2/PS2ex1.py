balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
TP = 0
for i in range(12):
    print("Month: " + str(i+1))
    MMP = balance * monthlyPaymentRate
    print("Minimum monthly payment: " + str(round(MMP,2)))
    TP += MMP
    UBal = balance - MMP
    IR = (annualInterestRate/12.0)*UBal
    balance = UBal + IR
    print("Remaining balance: " + str(round(balance,2)))
print("Total paid: " + str(round(TP,2)))
print("Remaining balance: " + str(round(balance,2)))
    
    
