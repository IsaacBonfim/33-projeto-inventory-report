from datetime import date


def next_expiration(list):
    year, month, day = list[0].split("-")
    next_expiration = date(int(year), int(month), int(day))

    for product in list:
        year, month, day = product.split("-")
        expiration = date(int(year), int(month), int(day))

        if expiration < next_expiration and expiration >= date.today():
            next_expiration = expiration

    return next_expiration
