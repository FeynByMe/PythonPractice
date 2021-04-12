def shipping_costs(num_items):
    
    if num_items == 1:
        return float(10.95)
    else:
        return float(10.95) + (num_items - 1) * 2.95
