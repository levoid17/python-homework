monthly_electricity_usage = float(input("Enter your monthly electricity usage in kWh: "))
if monthly_electricity_usage <= 0:
    print("Invalid electricity usage.")
elif monthly_electricity_usage <= 100:
    print(f"Your electricity bill is {0.08 * monthly_electricity_usage:.2f} AZN" + ' ' + f'applied rate is 0.08 AZN per kWh: {monthly_electricity_usage:.2f} kWh')
elif monthly_electricity_usage <= 300 and monthly_electricity_usage > 100:
    print(f"Your electricity bill is {0.12 * monthly_electricity_usage:.2f} AZN" + ' ' + f'applied rate is 0.12 AZN per kWh: {monthly_electricity_usage:.2f} kWh')
elif monthly_electricity_usage > 300:
    print(f"Your electricity bill is {0.15 * monthly_electricity_usage:.2f} AZN" + ' ' + f'applied rate is 0.15 AZN per kWh: {monthly_electricity_usage:.2f} kWh')