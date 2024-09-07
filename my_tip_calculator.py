def main():
    to_pay = float(input("Enter pay: "))
    percentage = float(input("Enter percentage: "))
    tip = compute_tip_of(to_pay,percentage)
    print(f"Tip: ksh.{tip:.2f}")
    
def compute_tip_of(to_pay,percentage):
    percentage = percentage / 100
    tip = to_pay * percentage
    return tip


main() 
