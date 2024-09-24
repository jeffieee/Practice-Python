def filter_high_sales(sales_data, threshold):
    for i in sales_data:
        result = []
        
        for i in sales_data:
            if i["sales"] >= threshold:
                result.append(i)
        
        return result
        
sales_data = [
    {'month': 'January', 'sales': 2500},
    {'month': 'February', 'sales': 3000},
    {'month': 'March', 'sales': 2200},
    {'month': 'April', 'sales': 4000},
    {'month': 'May', 'sales': 1500},
]

threshold = 3000

print(filter_high_sales(sales_data, threshold))
        