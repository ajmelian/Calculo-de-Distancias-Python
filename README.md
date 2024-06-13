# Distance Calculation Algorithm

Este repositorio contiene un algoritmo en Python para calcular la distancia entre dos puntos geográficos dados por sus coordenadas de latitud y longitud. La distancia se puede devolver en kilómetros, millas o metros.

## Descripción

El algoritmo utiliza la fórmula del haversine para calcular la distancia entre dos puntos en la superficie de la Tierra. La fórmula del haversine toma en cuenta la curvatura de la Tierra para proporcionar una medida precisa de la distancia entre dos puntos dados sus latitudes y longitudes.

## Uso

### Función

```python
def distance(lat1, lng1, lat2, lng2, unit='km'):
    """
    Calcula la distancia entre dos puntos geográficos dados por sus coordenadas de latitud y longitud.
    La distancia se puede devolver en kilómetros, millas o metros.

    :param lat1: Latitud del primer punto.
    :param lng1: Longitud del primer punto.
    :param lat2: Latitud del segundo punto.
    :param lng2: Longitud del segundo punto.
    :param unit: Unidad de medida para la distancia ('km', 'miles', 'metro'). Por defecto es 'km'.
    :return: La distancia entre los dos puntos en la unidad especificada, redondeada a dos decimales.
    :raises ValueError: Si se proporciona una unidad no válida.
    :version: 1.0
    :author: AJ Melián <amelian@codesecureforge.com>
    :date: 2024-06-13
    :license: GNU General Public License v3.0
    :example:

    # Distancia en kilómetros
    distancia_km = distance(40.7128, -74.0060, 34.0522, -118.2437)
    print(distancia_km)  # Salida: 3935.75

    # Distancia en millas
    distancia_miles = distance(40.7128, -74.0060, 34.0522, -118.2437, 'miles')
    print(distancia_miles)  # Salida: 2445.56

    # Distancia en metros
    distancia_metros = distance(40.7128, -74.0060, 34.0522, -118.2437, 'metro')
    print(distancia_metros)  # Salida: 3935750
    """
```

### Ejemplos de uso

#### Distancia en kilómetros

```python
distancia_km = distance(40.7128, -74.0060, 34.0522, -118.2437)
print(distancia_km)  # Salida: 3935.75
```

#### Distancia en millas

```python
distancia_miles = distance(40.7128, -74.0060, 34.0522, -118.2437, 'miles')
print(distancia_miles)  # Salida: 2445.56
```

#### Distancia en metros

```python
distancia_metros = distance(40.7128, -74.0060, 34.0522, -118.2437, 'metro')
print(distancia_metros)  # Salida: 3935750
```

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/ajmelian/Calculo-de-Distancias-Python.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd Calculo-de-Distancias-Python
    ```
3. Asegúrate de tener Python instalado en tu sistema. Este script es compatible con Python 3.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, por favor, abre una solicitud de extracción (pull request) o un issue para discutir los cambios que deseas realizar.

## Licencia

Este proyecto está licenciado bajo la GNU General Public License v3.0. Para más detalles, consulta el archivo [LICENSE](LICENSE).

## Autor

- AJ Melián <amelian@codesecureforge.com>

Fecha: 2024-06-13

---

¡Gracias por usar este algoritmo! Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto.
