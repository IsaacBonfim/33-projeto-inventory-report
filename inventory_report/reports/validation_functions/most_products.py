def most_products(list):
    company = ""
    quant = 0

    for comp, qnt in list.items():
        if qnt >= quant and company is not None:
            quant = qnt
            company = comp

    return company
