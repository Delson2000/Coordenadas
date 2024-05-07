# Conversor de Coordenadas

Este é um simples script em Python para converter coordenadas de formato numérico para o formato de graus, minutos e segundos. 🌍

## Como Usar

1. **Instalação do Python**: Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/). 🐍

2. **Execução**: No seu terminal, navegue até o diretório onde o arquivo `coordenadas.py` está localizado e execute o script usando o comando:

    ```bash
    python coordenadas.py
    ```

3. **Saída**: As coordenadas convertidas serão impressas no terminal. 🖨️

## Exemplo

Você pode usar este script para converter uma única coordenada ou uma lista de pares de coordenadas.

```python
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
