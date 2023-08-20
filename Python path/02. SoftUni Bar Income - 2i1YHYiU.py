import re

command = input()

sample = r'%(?P<customer>[A-Z][a-z]+)%([^\|\$\%\.]+)?<(?P<product>\w+)>([^\|\$\%\.]+)?\|(?P<count>\d+)\|([^\|\$\%\.0-9]+)?(?P<price>[\d+\.?]+)\$'

total_sales = 0
while command != 'end of shift':
    matches = re.finditer(sample, command)
    for match in matches:
        customerName = match.group('customer')
        product = match.group('product')
        sales = match.group('count')
        price = match.group('price')
        sales_value = int(sales) * float(price)
        total_sales += sales_value

        print(f'{customerName}: {product} - {sales_value:.2f}')

    command = input()

print(f'Total income: {total_sales:.2f}')