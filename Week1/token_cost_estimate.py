print("=== AI Tokens Cost Estimator ===")
token = int(input("How Many Many Token? = "))
price_per_1000 =float(input("Price per 1000 Token (in reupees) = "))
cost = (token / 1000) * price_per_1000
print(f"Estimated Cost:{cost:.2f} Rs") 