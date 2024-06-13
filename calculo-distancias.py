import math

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
    
    # Determina el radio de la Tierra según la unidad de medida especificada
    if unit == 'km':
        planet_radius = 6371
    elif unit == 'miles':
        planet_radius = 6371 * 0.6213711
    elif unit == 'metro':
        planet_radius = 6371 * 1000
    else:
        raise ValueError("Unidad no válida. Use 'km', 'miles' o 'metro'.")

    # Calcula la diferencia en radianes entre las latitudes y longitudes
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lng2 - lng1)

    # Aplicamos la fórmula del haversine para calcular la distancia
    a = math.sin(d_lat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(d_lon / 2) ** 2
    c = 2 * math.asin(math.sqrt(a))
    distance = round(planet_radius * c, 2)
    
    return distance

# Ejemplos de uso
# Distancia en kilómetros
distancia_km = distance(40.7128, -74.0060, 34.0522, -118.2437)
print(distancia_km)  # Salida: 3935.75

# Distancia en millas
distancia_miles = distance(40.7128, -74.0060, 34.0522, -118.2437, 'miles')
print(distancia_miles)  # Salida: 2445.56

# Distancia en metros
distancia_metros = distance(40.7128, -74.0060, 34.0522, -118.2437, 'metro')
print(distancia_metros)  # Salida: 3935750
