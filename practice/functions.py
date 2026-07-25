def calculate_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 400)
    return price - discount_amount


def apply_tax(price, tax_percent):
    return price + (price * (tax_percent / 100))


price_after_discount = calculate_discount(1240, 0)
final_price = apply_tax(price_after_discount, 20)
print(f"итоговая цена: {final_price}")