linea = "------------------"
rios = {'Nilo':'Egipto','Amazonas':'Brasil','Sena':'Francia','Ebro':'España','Volga':'Rusia'}

num = rios.keys()

for num in reversed(rios):
    print('El ', str(num) , ' corre a través de ' , str(rios[num]))

print (linea)

for num in reversed(rios):
        print('Rio ', str(num))

print (linea)

for num in reversed(rios):
    print('Pais ', str(rios[num]))