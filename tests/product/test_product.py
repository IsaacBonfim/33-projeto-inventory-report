from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        'Pão de Sal',
        'Padaria Xodó',
        '28-10-2022',
        '29-10-2022',
        '01',
        'Guardar em local fresco'
    )

    assert product.id == 1
    assert product.nome_do_produto == 'Pão de Sal'
    assert product.nome_da_empresa == 'Padaria Xodó'
    assert product.data_de_fabricacao == '28-10-2022'
    assert product.data_de_validade == '29-10-2022'
    assert product.numero_de_serie == '01'
    assert product.instrucoes_de_armazenamento == 'Guardar em local fresco'
