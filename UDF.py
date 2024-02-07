import sqlite3  # importamos las librerias sqlite3 y pandas
import pandas as pd
square = lambda n: n*n  # square va aser igual a una funcion que va a tomar como dato n y lo vamos elevaral cuadrado 
conn = sqlite3.connect("northwind.db")  # lo que hace estoe s crear una variable comm y se conecte a la bas ede datos  y solo entre las comillas poner el nombre de  la base de datos 
conn.create_function("square",1,square)  # ahora lo registramos a sqlite el primer parametro es como quiero llamar a la funcion , despues cuantos parametros va a tener y lo ultimo es cual es la funcion de python que vas a usar para crear esta funcion 
# cursores
cursor = conn.cursor()  # creamos un cursor va con .cursor por que es un metodo 
# el cursor . execute lo que etsa diciendo es ejecutame una consulta
cursor.execute('''  
    SELECT * FROM Products
    ''')
# como lo miramos la  informacion que tra el cursor 
results = cursor.fetchall()  # el fetchall lo que hara sera el cursor tiene esa informacion y con fetchall lo obtenemos 
results_df = pd.DataFrame(results) # creamos un dataframe primero traemos a pd que es la libreria de pandas , DataFrame que es un metodo y dentro de ello el parametro results
conn.commit()
cursor.close()
conn.close()
print(results_df)
with sqlite3.connect("northwind.db") as conn:
    conn.create_function("square",1,square)
    cursor = conn.cursor()
    cursor.execute('''
                   SELECT *,square(Price) FROM Products WHERE Price > 0
                   ''')
    results = cursor.fetchall()
    results_df = pd.DataFrame(results)
print(results_df)
