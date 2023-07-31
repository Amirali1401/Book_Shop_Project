from books.models import Book


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart



    def save(self):
        self.session.modified = True



    def add(self, book , quantity=0, replace_current_quantity=False):
        book_id = str(book.id)

        if book_id not in self.cart:
            self.cart[book_id] = {
                'quantity': 0,
            }


        if replace_current_quantity:
            self.cart[book_id] = {
                'quantity': quantity,
            }

        else:
            self.cart[book_id]['quantity'] += quantity

        self.save()

    def remove(self, book):
        book_id = str(book.id)

        if book_id in self.cart:
            del self.cart[book_id]

        self.save()


    def __iter__(self):
        books_id = self.cart.keys()
        books = Book.objects.filter(id__in = books_id)

        for book in books:
            self.cart[str(book.id)]['book_obj'] = book

        for item in self.cart.values():
            yield  item

    def get_total_price(self):

        sum_price =  sum(item['book_obj'].price * item['quantity'] for item in self)
        return sum_price

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session['cart']

        self.save()
