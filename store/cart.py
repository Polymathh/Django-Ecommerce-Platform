class Cart:
    def __init__(self, request):
        self.session = request.session
        cart=self.session.get('cart')
        if not cart:
            cart=self.session['cart'] = {}
            self.cart = cart

    def add(self, product, quanlity=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity' : 0, 'price' : str(product.price)}
        self.cart[product_id]['quantity'] += quantity
        self.save() 

    def save(self):
        self.session.modified = True
