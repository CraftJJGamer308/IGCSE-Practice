class Product:
    def __init__(self, category, itemCode, description, price):
        self.category = category
        self.itemCode = itemCode
        self.description = description
        self.price = price

cart = []

productList = [
    Product('Phone', 'BPCM', 'Compact', 29.99),
    Product('Phone', 'BPSH', 'Clam Shell', 49.99),
    Product('Phone', 'RPSS', 'RoboPhone - 5-inch screen and 64 GB memory', 199.99),
    Product('Phone', 'RPLL', 'RoboPhone - 6-inch screen and 256 GB memory', 499.99),
    Product('Phone', 'YPLS',
            'Y-Phone Standard - 6-inch screen and 64 GB memory', 549.99),
    Product('Phone', 'YPLL',
            'Y-Phone Deluxe - 6-inch screen and 256 GB memory', 649.99),
    Product('Tablet', 'RTMS', 'RoboTab - 8-inch screen and 64 GB memory', 149.99),
    Product('Tablet', 'RTLM', 'RoboTab - 10-inch screen and 128 GB memory', 299.99),
    Product('Tablet', 'YTLM',
            'Y-Tab Standard - 10-inch screen and 128 GB memory', 499.99),
    Product('Tablet', 'YTLL',
            'Y-Tab Deluxe - 10-inch screen and 256 GB memory', 599.99),
    Product('SIM card', 'SMNO', 'SIM Free (no SIM card purchased)', 0.00),
    Product('SIM card', 'SMPG', 'Pay As You Go (SIM card purchased)', 9.99),
    Product('Case', 'CSST', 'Standard', 0.00),
    Product('Case', 'CSLX', 'Luxury', 50.00),
    Product('Charger', 'CGCR', 'Car', 19.99),
    Product('Charger', 'CGHM', 'Home', 15.99)
]

deviceCount = 0

while True:
    for i in range(0, len(productList)):
        if productList[i].category == 'Phone' or productList[i].category == 'Tablet':
            print(str(i + 1) + '. (' + productList[i].itemCode+') ' +
                productList[i].description + ' : $' + str(productList[i].price))

    choice = input('Enter the item code(s) that you want to buy. Enter 0 to finish: ')
    
    for i in range(0, len(productList)):
        if choice == productList[i].itemCode:
            cart.append(productList[i])
            break
    
    deviceCount += 1
    SIM = input('SIM Free(1) or Pay as you go(2)?: ')
    if SIM == '1':
        cart.append(productList[10])
    else:
        cart.append(productList[11])

    case = input('Standard(1) or Luxury? (2): ')
    if case == '1':
        cart.append(productList[12])
    else:
        cart.append(productList[13])

    buyAnother = input('add another device? 1 for yes, 0 for no: ')
    if buyAnother == '0':
        break

sum = 0
for i in range(0,len(cart)):
    sum += cart[i].price
    
print(sum)