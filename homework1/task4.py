def calculate_discount(price, discount):

    if not isinstance(price, (int, float)):
        raise TypeError("Invalid price")
    if not isinstance(discount, (int, float)):
        raise TypeError("Invalid discount type")
    if discount < 0 or discount > 100:
        raise ValueError("Invalid discount value")

    return price * (1 - discount / 100)