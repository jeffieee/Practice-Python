def calculate_average_sales(sales):
    if len(sales) == 0:
        return 0
    else:
        return sum(sales) / len(sales)
    
sales = [2500, 3000, 3200, 2800, 2600, 2900, 3100, 3300, 2700, 2900, 3500, 3800]
print(calculate_average_sales(sales))
