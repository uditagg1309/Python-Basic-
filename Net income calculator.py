
print("Inputed amount should NOT be Negative and do not use commas")
BS = float(input("Enter your basic salary = "))
DA = BS * 0.10
print("Your D.A. = ", DA )
TA = BS * 0.15
if TA <= 75000:
    TA1 = TA
else:
    TA1 = 75000
print("Your Travelling allowances = ", TA1)
HRA = BS * 0.25
if HRA <= 100000:
    HRA1 = HRA
else:
    HRA1 = 100000
print("Your house rent allowance = ", HRA1)
TI = BS + DA + TA1 + HRA1
print("Your total income = ", TI)
print("Input positive value for Deduction")
DEA = float(input("Enter your Deduction under Section 80C  = "))
if DEA < 0:
    print("Deduction cannot be negative")
elif DEA <= 150000:
    DEA1 = DEA
    TAXI = TI - DEA1
    print("Your taxable income = ", TAXI)
else:
    DEA1 = 150000
    TAXI = TI - DEA1
    print("Your taxable income = ", TAXI)
if TAXI < 500000:
    IT = 0
elif TAXI < 750000:
    IT = (TAXI - 500000) * 0.10
elif TAXI < 1000000:
    IT = (250000 * 0.10) + (TAXI - 750000) * 0.15
elif TAXI < 1250000:
    IT = (250000 * 0.10) + (250000 * 0.15) + (TAXI - 1000000) * 0.20
elif TAXI < 1500000:
    IT = (250000 * 0.10) + (250000 * 0.15) + (250000 * 0.20) + (TAXI - 1250000) * 0.25
else:
    IT = IT = (250000 * 0.10) + (250000 * 0.15) + (250000 * 0.20) + (250000) * 0.25 + (TAXI - 1500000) * 0.30
print("Your income tax = ",IT)
EC = IT * 0.04
print("Your Education cess = ",EC)
NI = TAXI - IT - EC
print("Your Net income = ",NI)



