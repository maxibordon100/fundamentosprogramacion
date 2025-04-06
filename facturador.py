###Programa de facturacion###
def calculate(total,discounts,taxes):
    """

    :param total:
    :param discounts:
    :param taxes:
    """
    for tax in taxes:
         total=total + (total * (tax/100))
    print('El precio con los impuestos sin los descuentos es ',total)
    for discount in discounts:
          total=total - (total * (discount/100))
    print('El precio final es ',total)

def loadTransactionData():
    """

    """
    discounts=[]
    taxes=[]
    total=0
    article = input('Ingrese código del articulo (end para finalizar): ').strip()
    while(article!='end'):
        price = float(input('Ingrese precio del artículo: ').strip())
        cant = float(input('Ingrese cantidad adquirida: ').strip())
        total=total + (price * cant)
        article = input('Ingrese código del artículo (end para finalizar): ').strip()

    print('El total de la venta es ',total)


    questionTaxes = input('Desea agregar un impuesto ? (y/n): ').strip()
    while (questionTaxes != 'n'):
        tax = float(input('Ingrese porcentaje: ').strip())
        taxes.append(tax)
        questionTaxes = input('Desea agregar un impuesto (%)? (y/n): ').strip()


    questionDiscount = input('Desea agregar un descuento (y/n): ').strip()
    while (questionDiscount != 'n'):
        discount = float(input('Ingrese procentaje: ').strip())
        discounts.append(discount)
        questionDiscount = input('Desea agregar un descuento (y/n): ').strip()
    calculate(total, discounts, taxes)


def main():
  try:
    question=input('Desea ingresar una transacción o venta (y/n): ')
    while(question=='y'):
        loadTransactionData()
        question = input('Desea ingresar una transacción o venta (y/n): ')
  except:
         print('Se ha producido un error en la carga de datos')
if __name__ =='__main__':
       main()
