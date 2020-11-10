from invoice import invoice

products = {}
total_amount = 0
repeat = ''

while True:
    product = input('What is your product : ')
    unit_price = invoice.inputAnswer("Please enter unit price: ")
    qnt = invoice.inputNumber("Please enter quantity of product: ")
    discount = invoice.inputNumber("Discount percent (%) : ")
    repeat = invoice.inputAnswer("Another product? (y,n) : ")
    result = invoice.addProduct(qnt, unit_price, discount)
    products[product] = result
    if repeat == "n":
        break

total_amount = invoice.totalPurePrice(products)

print("Your total price is: ", total_amount)