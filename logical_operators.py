hasHighIncome = True
hasGoodCredit = True
hasCriminalRecord = True

if hasHighIncome or hasGoodCredit:
    print("Eligible for loan")

if hasHighIncome and hasGoodCredit:
    print("Eligible for loan")

if hasHighIncome and not hasCriminalRecord:
    print("Eligible for loan")