import sys

# Scalability and extensibility (Scale and extend with more features over time)

def parseArguments():
    arguements = {
        "price": int(sys.argv[1]),
        "quantity": sys.argv[2],
        "province": sys.argv[3]
    }
    return arguements

def taxRate(province):
    tax = {
        "ON": 1.13
    }
    return tax[province]

def mcmerchCalculator():
    arguements = parseArguments()
    tax = taxRate(arguements["province"])
    print(arguements["price"] * arguements["quantity"] * tax)
    
mcmerchCalculator()