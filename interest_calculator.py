import pandas as pd
import numpy as np

# -----------------------------
# 1️⃣ Input Loan Details
# -----------------------------
principal = float(input("Enter loan amount ($): "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan term (years): "))

monthly_rate = annual_rate / 100 / 12
num_payments = years * 12

# -----------------------------
# 2️⃣ Calculate Monthly Payment
# -----------------------------
monthly_payment = principal * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)

print(f"\n💳 Monthly Payment: ${monthly_payment:.2f}")

# -----------------------------
# 3️⃣ Generate Amortization Schedule
# -----------------------------
balance = principal
schedule = []

for month in range(1, num_payments + 1):
    interest = balance * monthly_rate
    principal_payment = monthly_payment - interest
    balance -= principal_payment
    schedule.append([month, monthly_payment, principal_payment, interest, max(balance, 0)])

df = pd.DataFrame(schedule, columns=["Month", "Payment", "Principal", "Interest", "Remaining Balance"])

# -----------------------------
# 4️⃣ Export to Excel
# -----------------------------
file_name = "loan_amortization.xlsx"
with pd.ExcelWriter(file_name, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Amortization Schedule", index=False)
    pd.DataFrame({
        "Loan Amount": [principal],
        "Annual Rate (%)": [annual_rate],
        "Term (Years)": [years],
        "Monthly Payment": [monthly_payment],
        "Total Payment": [monthly_payment*num_payments],
        "Total Interest": [monthly_payment*num_payments - principal]
    }).to_excel(writer, sheet_name="Summary", index=False)

print(f"\n✅ Excel report saved as {file_name}")
