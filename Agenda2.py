class Agenda:
  
  """Abstraccion de los objetos agenda."""

  def __init__(self, NOMBRE):
    self.menus(NOMBRE)  
    print('--------------------------')
    while True:
      v_Cadena=input('favor selecionar la operacion: ')
      if v_Cadena in ['A','a']: 
        self.insertar_registros(NOMBRE)
      elif v_Cadena in ['B','b']:
        self.buscar_datos(NOMBRE)     
      elif v_Cadena in ['c','C']:
        self.modificar_datos(NOMBRE)  
      else:
        break 

  def menus(self,NOMBRE): 
    print(NOMBRE,'esta es tu lista de contactos \n')
    print('para acceder a sus funciones precione: \n')
    print('A: para insertar registros')
    print('B: para buscar registros')
    print('C: para modificar un registros')
    print('Otras para salir')


  def insertar_registros(self, NOMBRE):
    header = ["NOMBRE".ljust(30), "APELLIDO".ljust(30), "EDAD".ljust(3), "TELEFONO".ljust(30), "EMAIL".ljust(60)]
    from os import path
    print("Has elegido la opcion Insertar")
    print('--------------------------')
    v_achivo ='C:\\reportes\\'+NOMBRE+'.txt'
    if path.isfile(v_achivo):
      nombre= input("Nombre: ")
      apellido= input("Apellido: ")
      edad= input("Edad: ")
      telefono= input("Telefono: ")
      email= input("Email: ")
      lista_agenda=['Nombre:'+nombre,"Apellido:"+apellido,"Edad:"+edad,"Telefono:"+telefono,"Email:"+email]
      agenda= open(v_achivo,"a+")
      agenda.write(",".join(lista_agenda) + "\n")
      agenda.close()
    else:
      nombre= input("Nombre: ")
      apellido= input("Apellido: ")
      edad= input("Edad: ")
      telefono= input("Telefono: ")
      email= input("Email: ")
      lista_agenda=['Nombre:'+nombre,"Apellido:"+apellido,"Edad:"+edad,"Telefono:"+telefono,"Email:"+email]
      agenda= open(v_achivo,"w")
      agenda.write(",".join(lista_agenda)+ "\n")
      agenda.close()  


  def buscar_datos(self, NOMBRE):
    print('has elegido la opcion de buscar datos')
    print('--------------------------')
    archiv =open('C:\\reportes\\'+NOMBRE+'.txt','r')
    diccionario={}
    num=input('search no: ') 
    for x in archiv:
      if num in x:
        diccionario={"Nombre":x.split(',')[0].split(':')[1],"Apellido":x.split(',')[1].split(':')[1],"Edad":x.split(',')[2].split(':')[1],"Telefono":x.split(',')[3].split(':')[1],"Email":x.split(',')[4].split(':')[1]}
        print('Nombre:'+diccionario['Nombre'])


  def modificar_datos(self, NOMBRE):
    print('***has elegido la opcion de modificar registos***')


def run_Agenda():
    mi_Agenda = Agenda('javier')
run_Agenda()
