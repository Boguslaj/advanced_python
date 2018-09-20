class Money(object):
    exchange = {
        'USD': 1,
        'BYN': 2.12,
        'EUR': 0.86,
        'JPY': 112.28,
        'GBP': 0.76}

    def __init__(self, summ, currency='USD'):
        try:
            Money.exchange[currency]
        except KeyError:
            print('This currency is not supported! USD will be used enstead.')
            currency = 'USD'
        self.currency = currency
        self.value = summ  # * exchange[currency]  # stored in USD

    def __str__(self):
        return ('{:.2f}'.format(self.value)) + " " + self.currency

    def __add__(self, other):
        if self.currency == other.currency:
            new_value = self.value + other.value
        else:
            added = other.value / Money.exchange[other.currency]
            new_value = self.value + (added * Money.exchange[self.currency])
        return Money(new_value, self.currency)

    def __radd__(self, other):
        universal = self.value / Money.exchange[self.currency]
        new_value = (universal + other) * Money.exchange[self.currency]
        return Money(new_value, self.currency)

    def __sub__(self, other):
        if self.currency == other.currency:
            new_value = self.value - other.value
        else:
            added = other.value / Money.exchange[other.currency]
            new_value = self.value - (added * Money.exchange[self.currency])
        return Money(new_value, self.currency)

    def __rsub__(self, other):
        universal = self.value / Money.exchange[self.currency]
        new_value = (universal - other) * Money.exchange[self.currency]
        return Money(new_value, self.currency)

    def __mul__(self, mult):
        new_val = self.value * mult
        return Money(new_val, self.currency)

    def __rmul__(self, mult):
        new_val = self.value * mult
        return Money(new_val, self.currency)


if __name__ == '__main__':
    b = Money(10, 'BYN')
    j = Money(1000, 'JPY')
    e = Money(10, 'EUR')
    g = Money(10, 'GBP')
    u = Money(100, 'UUU')

    check = [j, b, e, g, u]
    summ = b + j + e + g + u
    print(summ)
    s = sum(check)
    print(s)
    print(e + (j * 4.5) + (0.5 * b))

    x = Money(10, "BYN")
    y = Money(11)  # define your own default value, e.g. “USD”
    z = Money(12.34, "EUR")
    print(z + (3.11 * x) + (y * 0.8))  # result in “EUR”

    lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]
    s = sum(lst)
    print(s)  # result in “BYN”
