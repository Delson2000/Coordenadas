def converter_para_coordenadas(latitude, longitude):
    """
    Converte um par de coordenadas em formato numérico para o formato de graus, minutos e segundos.
    
    Args:
        latitude (int): Latitude em formato numérico.
        longitude (int): Longitude em formato numérico.
        
    Returns:
        str: Coordenadas no formato de graus, minutos e segundos.
    """
    lat_graus = int(latitude) // 1000000
    lat_minutos = (int(latitude) % 1000000) // 10000
    lat_segundos = (int(latitude) % 10000) / 100

    long_graus = int(longitude) // 1000000
    long_minutos = (int(longitude) % 1000000) // 10000
    long_segundos = (int(longitude) % 10000) / 100

    coordenadas = f"{lat_graus}°{lat_minutos}'{lat_segundos:.2f}\"S {long_graus}°{long_minutos}'{long_segundos:.2f}\"O"
    return coordenadas


def converter_pares_para_coordenadas(pares):
    """
    Converte uma lista de pares de coordenadas em formato numérico para o formato de graus, minutos e segundos.
    
    Args:
        pares (list): Lista de pares de coordenadas em formato numérico.
        
    Returns:
        list: Lista de coordenadas no formato de graus, minutos e segundos.
    """
    coordenadas = []
    for par in pares:
        latitude, longitude = par
        lat_graus = int(latitude) // 1000000
        lat_minutos = (int(latitude) % 1000000) // 10000
        lat_segundos = (int(latitude) % 10000) / 100

        long_graus = int(longitude) // 1000000
        long_minutos = (int(longitude) % 1000000) // 10000
        long_segundos = (int(longitude) % 10000) / 100

        coordenada = f"{lat_graus}°{lat_minutos}'{lat_segundos:.2f}\"S {long_graus}°{long_minutos}'{long_segundos:.2f}\"O"
        coordenadas.append(coordenada)
    return coordenadas


# Exemplo de uso
if __name__ == "__main__":
    numero_latitude = 22291344
    numero_longitude = 42394883

    coordenadas = converter_para_coordenadas(numero_latitude, numero_longitude)
    print(coordenadas)

    pares = [
        (22091344, 42394883), (22180074, 42311718), (22152252, 42314480),
        (22274479, 43285764), (22280859, 43292083), (22225547, 42560872),
        (22150724, 42322055), (22152760, 42321843), (21494019, 41163951),
        (21501539, 41153936), (21504872, 41144400), (21393046, 42202401),
        (22372892, 43532535), (22433225, 44074211), (21421093, 41240984),
        (22061074, 41510033)
    ]

    coordenadas = converter_pares_para_coordenadas(pares)
    for coordenada in coordenadas:
        print(coordenada)
