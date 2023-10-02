import time
import matplotlib.pyplot as plt

class ArrayDinamico:
    # ... (tu código de la clase ArrayDinamico, incluyendo el método insertar)
# Definición de la clase ArrayDinamico
    # Constructor: Inicializa la instancia del objeto con un tamaño dado.
    def __init__(self, tamaño):
        # Inicializa una lista de datos con el tamaño especificado, inicialmente con valores None.
        self._datos = [None] * tamaño
        # Inicializa el tamaño actual del array como 0.
        self._tamaño = 0

    # Sobrecarga de la función len(): Devuelve el tamaño actual del array.
    def __len__(self):
        return self._tamaño

    # Sobrecarga del operador []: Permite acceder a un elemento del array por índice.
    def __getitem__(self, índice):
        return self._datos[índice]

    # Sobrecarga del operador []: Permite establecer el valor de un elemento del array por índice.
    def __setitem__(self, índice, valor):
        self._datos[índice] = valor

    # Método insertar: Inserta un valor en la posición especificada del array.
    def insertar(self, índice, valor):
        # Si el tamaño actual del array es igual al tamaño de la lista interna, se redimensiona.
        if self._tamaño == len(self._datos):
            self.redimensionar(2 * len(self._datos))

        # Mueve los elementos desde la posición de inserción hacia la derecha para hacer espacio.
        for i in range(self._tamaño - 1, índice, -1):
            self._datos[i + 1] = self._datos[i]

        # Inserta el valor en la posición especificada e incrementa el tamaño del array.
        self._datos[índice] = valor
        self._tamaño += 1

    # Método redimensionar: Cambia el tamaño del array interno a uno nuevo.
    def redimensionar(self, nuevo_tamaño):
        # Crea una nueva lista con el nuevo tamaño.
        nuevos_datos = [None] * nuevo_tamaño
        # Copia los elementos actuales del array al nuevo array.
        for i in range(self._tamaño):
            nuevos_datos[i] = self._datos[i]
        # Actualiza la referencia de datos al nuevo array.
        self._datos = nuevos_datos
# Función para calcular estadísticas del tiempo amortizado
def calcular_estadisticas_tiempo_amortizado(array, num_inserciones):
    tiempos = []
    tiempo_total = 0.0

    for i in range(num_inserciones):
        tiempo_inicio = time.time()  # Marcar el tiempo de inicio
        array.insertar(i, i)  # Realiza la inserción en el array
        tiempo_fin = time.time()  # Marcar el tiempo de finalización
        tiempo_insercion = tiempo_fin - tiempo_inicio  # Calcular tiempo de inserción
        tiempos.append(tiempo_insercion)
        tiempo_total += tiempo_insercion

    # Calcular estadísticas del tiempo amortizado
    tiempo_promedio = tiempo_total / num_inserciones
    return tiempos, tiempo_promedio

def main():
    num_inserciones = 10000000
    array = ArrayDinamico(num_inserciones)  # Crea una instancia de ArrayDinamico

    # Calcula las estadísticas del tiempo amortizado
    tiempos_insercion, tiempo_promedio = calcular_estadisticas_tiempo_amortizado(array, num_inserciones)

    # Muestra las estadísticas
    print(f"Tiempo promedio de inserción: {tiempo_promedio} segundos")

    # Graficar los tiempos de inserción
    plt.plot(range(num_inserciones), tiempos_insercion, linestyle='-', color='b')
    plt.xlabel('Número de Inserciones')
    plt.ylabel('Tiempo de Inserción (segundos)')
    plt.title('Tiempo de Inserción vs. Número de Inserciones')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
    

