def shop_from_grocery_list(budget, grocery_list, *args):
    purchased_products = []
    for info in args:
        product_name = info[0]
        price = info[1]
        if budget < price:
            break
        if product_name in purchased_products:
            continue
        if product_name not in grocery_list:
            continue
        purchased_products.append(product_name)
        grocery_list.remove(product_name)
        budget -= price

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))


