# ? map() applies a function to each item in iterable (list, tuple, etc)
# map(function, iterable)

store = [("shirt", 15.00),
         ("pants", 27.00),
         ("jacket", 50.00),
         ("socks", 8.00)]

AUD_to_Real = lambda data: ((data[0], ((data[1] * 3.6) * 1.15)*1.40))  # Converting to price of products to Real + taxes + IOF
# function, iterable
store_real_price = list(map(AUD_to_Real, store))

for i in store_real_price:
    print("The {} cost(s) {:.2f} in Reals.".format(i[0], i[1]))
