print("<Using .append() method to add new element in the end of the list >\n""< For example, create an emmpty list and build it dynamically. >")

cart = []
print(f"\nNow the cart is empty: {cart}")
print("\n[PA that \t<cart[0].append() = 'books'>\tis the wrong way!]")
cart.append('books')
cart.append('milk')
print("[The right way like this \tcart.append('milk')\t\t!]")
print(f"\nNow we add sth in the cart: {cart}")

print("\n[PA that \tcart[0].append('cursion')\tis the wrong way too!]")
print(
    "<So how to insert?>\n[The answer is using \t.insret(index,object)\t !]")
cart.insert(0, 'cushion')
print(f"\nNow we insert sth in the cart: {cart}")

print("\n[But it seems that \tcart.insert(-1, 'Keyboard cover')\t dosen't work there!]")
cart.insert(-1, 'Keyboard cover')
print(
    f"As you can see, my new added thing in {cart} is not on the last position")
