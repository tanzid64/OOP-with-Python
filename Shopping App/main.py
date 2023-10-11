from shopping import Eshop
def main():
    eshop = Eshop()
    
    while True:
        print('\nWelcome to Eshop.com')
        print('\nPress 1 for sign Up')
        print('Press 2 for Login')
        op = input('\nEnter your key: ')
        if op == '1':
            print('\nPress 1 for signUp as customer')
            print('Press 2 for signUp as seller')
            temp_op = input('\nEnter your option: ')
            name = input('Enter your full name: ')
            phone = input('Enter your phone number: ')
            email = input('Enter your email: ')
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            if temp_op == '1':
                eshop.signUpUser(name, phone, email,username, password, 'customer')
            else: 
                eshop.signUpUser(name, phone, email,username, password, 'seller')

        elif op == '2':
            print('Press 1 for Customer')
            print('Press 2 for Seller')
            x = input('\nEnter your option: ')
            email = input('Enter your username or email: ')
            password = input('Enter your password: ')
            if x == '1':
                if eshop.logIn(email,password):
                    print('Successfully Logged In')
                    print('\nPress 1 for buy product')
                    print('Press 2 for deposit Money')
                    print('Press 3 for back to main page')
                    temp_op = input('\nEnter your option: ')
                    if temp_op == '1':
                        eshop.viewAvailableProducts()
                        product = input('\nEnter product name: ')
                        quantity = int(input('Enter quantity: '))
                        eshop.addToCart(product, quantity)
                        eshop.viewCart()
                        print('Press 1 to remove from cart')
                        print('Press 2 to place order')
                        x = input('\nEnter your option: ')
                        if x == '1':
                            product = input('Enter product name: ')
                            quantity = int(input('Enter quantity: '))
                            eshop.removeFromCart(product,quantity)
                        else:
                            eshop.placeOrder()
                    elif temp_op == '2':
                        amount = int(input('\nEnter amount of money: '))
                        eshop.deposit(amount)
            elif x == '2':
                if eshop.logIn(email,password):
                    print('\nSuccessfully Logged In')
                    print('\nPress 1 for add product')
                    print('Press 2 for withdraw Money')
                    print('Press 3 for back to Main Page')
                    temp_op = input('\nEnter your option: ')
                    if temp_op == '1':
                        name = input('\nEnter Product Name: ')
                        price = int(input('Enter Product Price: '))
                        quantity = int(input('Enter Product Quantity: '))
                        unit = input('Enter product unit: ')
                        eshop.createProduct(name, unit, price, quantity)
                    elif temp_op == '2':
                        amount = int(input('\nEnter amount of money: '))
                        eshop.withdraw(amount)
        
        elif op == '3':
            break
    
if __name__ == '__main__':
    main()