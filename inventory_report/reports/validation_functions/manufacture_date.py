from datetime import date


def oldest_manufacture(list):
    year, month, day = list[0].split("-")
    oldest_manufacture = date(int(year), int(month), int(day))

    for product in list:
        year, month, day = product.split("-")
        manufacture = date(int(year), int(month), int(day))

        if manufacture < oldest_manufacture:
            oldest_manufacture = manufacture

    return oldest_manufacture
