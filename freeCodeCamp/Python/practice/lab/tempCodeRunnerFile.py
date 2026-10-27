# Building an Apply Discount Function

def apply_discount (price, discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"