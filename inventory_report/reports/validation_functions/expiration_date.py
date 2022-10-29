from datetime import date


def proxima_validade(list):
    year, month, day = list[0].split("-")
    proxima_validade = date(int(year), int(month), int(day))

    for product in list:
        year, month, day = product.split("-")
        expiration = date(int(year), int(month), int(day))

        if expiration < proxima_validade and expiration >= date.today():
            proxima_validade = expiration

    return proxima_validade
