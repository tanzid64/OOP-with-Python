class User:
    def __init__(self,name, phone, email, username, password, role) -> None:
        self.email = email
        self.password = password
        self.name = name
        self.phone = phone
        self.username = username
        self.wallet = 0
        self.role = role

class Product:
    def __init__(self, name, unit, price, quantity,seller) -> None:
        self.name = name
        self.unit = unit
        self.price = price
        self.quantity = quantity
        self.seller = seller

class Eshop(User,Product):
    def __init__(self) -> None:
        self.user = []
        self.products = []
        self.cart = []
        self.login = {}
        self.cart_dict = {}
        self.current_user = None
    
    def signUpUser(self,name, phone, email, username, password, role):
        user = User(name, phone, email, username, password, role)
        self.login[email] = password
        self.login[username] = password
        self.user.append(user)
        if role == 'customer':
            print('\nSignUp Successfull as customer.')
            print(f'\nUser info:\n\nUsername:{username}\nName:{name}\nPhone:{phone}\nEmail:{email}\nBalance:{user.wallet} Tk')
        else:
            print('\nSignUp Successfull as seller.')
            print(f'\nUser info:\n\nUsername:{username}\nName:{name}\nPhone:{phone}\nEmail:{email}\nBalance:{user.wallet} Tk')

    def logIn(self, email_or_username, password):
        if self.login[email_or_username] == password:
            for id in self.user:
                if id.email == email_or_username or id.username == email_or_username:
                    self.current_user = id
                    break
            return True
        else:
            return False
    
    def deposit(self,amount): #For Customer
        if amount > 0:
            self.current_user.wallet += amount
            print(f'\nBalance has been updated to {self.current_user.wallet} Tk')
        else:
            print('Invalid amount type, please enter a valid amount of Tk')

    def withdraw(self,amount): #For Seller
        if amount <= self.current_user.wallet:
            self.current_user.wallet -= amount
            print(f'\n{amount}Tk Cashout successfull\nRemaining Balance {self.current_user.wallet} Tk')
        else:
            print(f'Insufficient balance, your current balance is {self.current_user.wallet}Tk')

    def createProduct(self, name, unit, price, quantity): #Seller
            product = Product(name, unit, price, quantity,self.current_user)
            self.products.append(product)
            print('Product Successfully added into store')

    def viewAvailableProducts(self): #Everyone
        for product in self.products:
            print(f'Name: {product.name}, Price per {product.unit}: {product.price} Tk, Stock: {product.quantity} {product.unit}')

    def addToCart(self, product_name, quantity): #Customer
        for product in self.products:
            if product_name == product.name:
                if quantity <= product.quantity:
                    product.quantity -= quantity
                    self.cart_dict[product.name] = quantity
                    self.cart.append(self.cart_dict)
                    print('\nSuccessfully added to the cart')
                else:
                    print('\nInsufficient Quantity. This item details is:')
                    print(f'Name: {product.name}, Price per {product.unit}: {product.price} Tk, Stock: {product.quantity} {product.unit}')
            else:
                print('Sorry, not available in the Shop')
    
    def viewCart(self): #Customer
        if not self.cart:
            print('Your list is empty')
        else:
            for cart_item in self.cart:
                for key,value in cart_item.items():
                    print(f'Name: {key}, Quantity: {value}')

    def removeFromCart(self, product_name, quantity): #Customer
        for object in self.cart:
            for key in object:
                if product_name == key:
                    object[key] -= quantity
                    for product in self.products:
                        if product_name == product.name:
                            product.quantity += quantity
                else:
                    print('\nThis product is not in your cart')

    def placeOrder(self):  # Customer
        if not self.cart:
            print("Your cart is empty. Please add items to your cart first.")
            return

        total_price = 0
        for cart_item in self.cart:
            for product_name, quantity in cart_item.items():
                for product in self.products:
                    if product_name == product.name:
                        item_price = product.price * quantity
                        total_price += item_price

        if total_price > self.current_user.wallet:
            print(f"Insufficient balance. Please deposit minimum {total_price - self.current_user.wallet} Tk before placing the order.")
            return

        # Calculate the seller's earnings and update their wallet
        seller_earnings = 0
        for cart_item in self.cart:
            for product_name, quantity in cart_item.items():
                for product in self.products:
                    if product_name == product.name:
                        seller_earnings += product.price * quantity
                        product.seller.wallet += seller_earnings

        # Deduct the total price from the customer's wallet
        self.current_user.wallet -= total_price

        # Clear the cart after the order is placed
        self.cart.clear()

        print(f"Order placed successfully! Total price: {total_price} Tk")
        print(f"Customer's remaining balance: {self.current_user.wallet} Tk")

