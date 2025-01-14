"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import re

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """

    def load_data(input_file):
        with open(input_file, "r") as file:
          data = file.read()
        return data

    def dataB(data):
        #Extraer registos por cluster, cant de palabras claves, % de palabras clave y principales palabras claves
        datab = re.compile(
            r"([0-9]+)(?:\s+)([0-9]+)(?:\s+)([0-9|\,]+)(?:[\s|\%]+)([a-z|\s|\,|\-|\/|\n|(|)]+)(?:\.*\n*)"
        )
        return datab.findall(data)  #devuelve una lista de tuplas con los registros encontrados


###PROCESAR INFORMACIÓN

    def keys(data):
       
          def Format_key(key_words):
              #
              key_words = key_words.replace("\n", " ").split(",")                       #elimina saltos de línea (\n), las separa por comas
              return ", ".join([" ".join(word.strip().split()) for word in key_words])  #elimina los espacios extra y concatena con una coma y un espacio

          data = [
              (
                  int(record[0]),                      #cluster
                  float(record[1]),                    #Cant de palabras clave
                  float(record[2].replace(",", ".")),  #% de palabras
                  Format_key(record[3]),               #palabras clave
              )
              for record in data
          ]

          return data

### CREAR DATA FRAME
       
    def create_df(data):
      columns = [
                "cluster",
                "cantidad_de_palabras_clave",
                "porcentaje_de_palabras_clave",
                "principales_palabras_clave",
            ]
      df = pd.DataFrame(data, columns=columns)

      return df        


### ORQUESTADOR

    def main():
       data= load_data("files/input/clusters_report.txt")
       data= dataB(data)
       data = keys(data)
       data = create_df(data)

       print(data)
       return data
    
    
    return main()
    
 ### Llamar a la función main
if __name__ == "__main__":
  print(pregunta_01())
