from .validation_functions.expiration_date import next_expiration
from .validation_functions.manufacture_date import oldest_manufacture
from .validation_functions.most_products import most_products


class SimpleReport:

    @staticmethod
    def generate(list):
        lista_de_validades = [product["data_de_validade"] for product in list]
        manufacture_list = [product["data_de_fabricacao"] for product in list]
        company_dict = {product["nome_da_empresa"]: 0 for product in list}

        for product in list:
            company_dict[product["nome_da_empresa"]] += 1

        validade = next_expiration(lista_de_validades)
        manufacture = oldest_manufacture(manufacture_list)
        company = most_products(company_dict)

        return (
          f"Data de fabricação mais antiga: {str(manufacture)}\n"
          f"Data de validade mais próxima: {str(validade)}\n"
          f"Empresa com mais produtos: {company}"
        )
