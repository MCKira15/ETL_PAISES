def transform(data):
    transform_data = []
    for pais in data:
        nombre = f'{pais['name']["common"]}'
        capital = pais["capital"][0]
        subregion = pais['subregion']
        poblacion = pais['population']
        transform_data.append((nombre,capital,subregion,poblacion))
    return transform_data