import pandas as pd  # se importa la librería pandas y se le da el alias pd

class jrlibrerias:
    def leer_excel(self, path):
        """
        Me lee y me devuelve un DataFrame.
        - self: referencia a la propia instancia del objeto.
        - path: ruta del archivo a leer (string o Path).
        """
        df = pd.read_excel(path)  # lee un archivo y devuelve un DataFrame
        return df  # devuelve el DataFrame a quien lo llamó
