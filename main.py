nombre=input('Nombre => ')

precio=float(input('Valor de tu factura => $'))


if precio<20 :
    porcentaje=0.1
elif precio>=20 and precio<=50:
    porcentaje=0.15
else:
    porcentaje=0.2

propina=precio*porcentaje

total=  precio+propina


print(f'{nombre}, de acuerdo al monto de tu factura, debes pagar una propina del {int(porcentaje*100)}%, tu total a pagar es de ${total}')



