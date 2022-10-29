from .simple_report import (
    SimpleReport,
    next_expiration,
    oldest_manufacture,
    most_products
)


class CompleteReport(SimpleReport):

    @staticmethod
    def generate(list):
        validity_list = [product["data_de_validade"] for product in list]
        manufacture_list = [product["data_de_fabricacao"] for product in list]
        company_dict = {product["nome_da_empresa"]: 0 for product in list}

        for product in list:
            company_dict[product["nome_da_empresa"]] += 1

        validity = next_expiration(validity_list)
        manufacture = oldest_manufacture(manufacture_list)
        company = most_products(company_dict)

        products_by_company = [
          f"- {company}: {qnt}\n"
          for company, qnt in company_dict.items()
        ]

        result = "".join(products_by_company)

        return (
          f"Data de fabricação mais antiga: {str(manufacture)}\n"
          f"Data de validade mais próxima: {str(validity)}\n"
          f"Empresa com mais produtos: {company}\n"
          f"Produtos estocados por empresa:\n"
          f"{result}"
        )
