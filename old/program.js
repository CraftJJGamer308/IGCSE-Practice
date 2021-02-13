class Product {
    constructor(category, itemCode, description, price) {
        this.category = category;
        this.itemCode = itemCode;
        this.description = description;
        this.price = price;
    }
}

var productList = [
    new Product('Phone', 'BPCM', 'Compact', 29.99),
    new Product('Phone', 'BPSH', 'Clam Shell', 49.99),
    new Product('Phone', 'RPSS', 'RoboPhone – 5-inch screen and 64 GB memory', 199.99),
    new Product('Phone', 'RPLL', 'RoboPhone – 6-inch screen and 256 GB memory', 499.99),
    new Product('Phone', 'YPLS', 'Y-Phone Standard – 6-inch screen and 64 GB memory', 549.99),
    new Product('Phone', 'YPLL', 'Y-Phone Deluxe – 6-inch screen and 256 GB memory', 649.99),

    new Product('Tablet', 'RTMS', 'RoboTab – 8-inch screen and 64 GB memory', 149.99),
    new Product('Tablet', 'RTLM', 'RoboTab – 10-inch screen and 128 GB memory', 299.99),
    new Product('Tablet', 'YTLM', 'Y-Tab Standard – 10-inch screen and 128 GB memory', 499.99),
    new Product('Tablet', 'YTLL', 'Y-Tab Deluxe – 10-inch screen and 256 GB memory', 599.99),

    new Product('SIM card', 'SMNO', 'SIM Free (no SIM card purchased)', 0.00),
    new Product('SIM card', 'SMPG', 'Pay As You Go (SIM card purchased)', 9.99),

    new Product('Case', 'CSST', 'Standard', 0.00),
    new Product('Case', 'CSLX', 'Luxury', 50.00),

    new Product('Charger', 'CGCR', 'Car', 19.99),
    new Product('Charger', 'CGHM', 'Home', 15.99)
];

function buyRequest() {
    var output = document.getElementById('list');
    for (let i = 0; i < productList.length; i++) {
        if (productList[i].category == 'Phone' || productList[i].category == 'Tablet'){
            output.append(`${productList[i].description} | Price: $${productList[i].price}`);
            output.appendChild(document.createElement("br"));
        }
            
    }
}

buyRequest();