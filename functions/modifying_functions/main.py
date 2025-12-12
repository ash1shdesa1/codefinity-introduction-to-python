def apply_discount(price, discount=0.05):
    cost = price * (1-discount)
    return cost

def apply_tax(price, tax=0.07):
    tax_price = price * (1 + tax)
    return tax_price

def calculate_total(price, discount=0.05, tax=0.07):
    total_price = price * (1 + tax) * (1 - discount)
    return total_price

total_price = calculate_total(120)
total_price_custom = calculate_total(100,discount=0.10,tax=0.08)

print(f"Total cost with default discount and tax: ${total_price}")

print(f"Total cost with custom discount and tax: ${total_price_custom}")