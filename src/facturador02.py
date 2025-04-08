import shelve

def loadProducts():
    with shelve.open('../products') as db:
        db['a1']={'stock':400,'description':'Mesa','price':55000}
        db['b2']={'stock':200,'description':'Silla','price':40000}
        db['c3']={'stock':40,'description':'radio','price':37000}
        db['d4']={'stock':10,'description':'TV','price':200500}
        db['e5']={'stock':15,'description':'zapatillas','price':60000}

cost_by_zone={'CABA':1000,
              'AMBA':2000,
              'INTERIOR':5000}

def update(code, cant):
    flag = False
    error=''
    with shelve.open('../products') as db:
        if (code in db):
            stock = db[code]['stock']
            if (stock >= cant):
                 data=db[code]
                 data['stock']=(stock-cant)
                 db[code]=data
                 flag=True
            else:
                 error='No hay stock suficiente'

    result=(flag,error)
    return result

def getData(code):
    data=None
    with shelve.open('../products') as db:
           if (code in db):
                   data=db[code]
    return data

def validateZone(zone):
     return zone in ['CABA','AMBA','INTERIOR']

def getZone():
    zone= input('Indique donde es el envío: (CABA/AMBA/INTERIOR): ').strip()
    while(not validateZone(zone)):
        print('Opción ingresada no válida - sólo se permite (CABA/AMBA/INTERIOR)')
        zone = input('Indique donde es el envío: (CABA/AMBA/INTERIOR): ').strip()
    return zone

def getResponseEnvio():
    answer= input('Confirma envío de la compra: ')
    while (not validateOption(answer)):
        print('Opción ingresada no válida - solo se permite (y/n): ')
        answer = input('Confirma envío de la compra: ').strip()
    return answer

def calculate(total,discounts):
    for discount in discounts:
          total=total - (total * (discount/100))
    return total


def loadTransaction():
    discounts = []
    total = 0
    article = input('Ingrese código del articulo (end para finalizar): ').strip()
    while (article != 'end'):
        data=getData(article)
        if (data!=None):
            cant = float(input('Ingrese cantidad adquirida: ').strip())
            result=update(article,cant)
            if (result[0]):
                total=(total + data['price']*cant)
            else:
                print(result[1])
        else:
              print('No existe el articulo cargado en el sistema')
        article = input('Ingrese código del artículo (end para finalizar): ').strip()
    print('El total adquirido fue: ',total)
    response=getResponseEnvio()
    if (response=='y'):
        zone=getZone()
        #Recuperamos el costo por zona
        total+=cost_by_zone[zone]
    print('El nuevo total fue de: ', total)
    #Chequear si fue una compra grande
    if (total > 350000):
            discounts.append(10)
    questionDiscount = input('Desea agregar un descuento (y/n): ').strip()
    while (questionDiscount != 'n'):
        discount = float(input('Ingrese procentaje: ').strip())
        discounts.append(discount)
        questionDiscount = input('Desea agregar un descuento (y/n): ').strip()
    total=calculate(total,discounts)
    print('El total a pagar con los descuentos es: ',total)

def validateOption(question):
      return question in ['y','n']
def getQuestionTransaction():
    answer = input('Desea ingresar una transacción o venta (y/n): ').strip()
    while (not validateOption(answer)):
        print('Opción ingresada no válida - solo se permite (y/n): ')
        answer = input('Desea ingresar una transacción o venta (y/n): ').strip()
    return answer
def main():
  try:
    question= getQuestionTransaction()
    while (question=='y'):
           loadTransaction()
           question = getQuestionTransaction()
  except KeyboardInterrupt:
         print('Se termina la ejecución por acción del user')
if __name__=='__main__':
      loadProducts()
      main()

