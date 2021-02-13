class Product:
    def __init__(self, category, itemCode, description, price):
        self.category = category
        self.itemCode = itemCode
        self.description = description
        self.price = price

productList = [
    Product('Phone', 'BPCM', 'Compact', 29.99),
    Product('Phone', 'BPSH', 'Clam Shell', 49.99),
    Product('Phone', 'RPSS', 'RoboPhone – 5-inch screen and 64 GB memory', 199.99),
    Product('Phone', 'RPLL', 'RoboPhone – 6-inch screen and 256 GB memory', 499.99),
    Product('Phone', 'YPLS',
            'Y-Phone Standard – 6-inch screen and 64 GB memory', 549.99),
    Product('Phone', 'YPLL',
            'Y-Phone Deluxe – 6-inch screen and 256 GB memory', 649.99),
    Product('Tablet', 'RTMS', 'RoboTab – 8-inch screen and 64 GB memory', 149.99),
    Product('Tablet', 'RTLM', 'RoboTab – 10-inch screen and 128 GB memory', 299.99),
    Product('Tablet', 'YTLM',
            'Y-Tab Standard – 10-inch screen and 128 GB memory', 499.99),
    Product('Tablet', 'YTLL',
            'Y-Tab Deluxe – 10-inch screen and 256 GB memory', 599.99),
    Product('SIM card', 'SMNO', 'SIM Free (no SIM card purchased)', 0.00),
    Product('SIM card', 'SMPG', 'Pay As You Go (SIM card purchased)', 9.99),
    Product('Case', 'CSST', 'Standard', 0.00),
    Product('Case', 'CSLX', 'Luxury', 50.00),
    Product('Charger', 'CGCR', 'Car', 19.99),
    Product('Charger', 'CGHM', 'Home', 15.99)
]

for i in range(0, len(productList)):
    if productList[i].category == 'Phone' or productList[i].category == 'Tablet':
        print(productList[i].description + ' : $' + str(productList[i].price))
