#obtener la populación
def get_population():
    keys = ['col', 'bol']
    values = [300, 400]
    print(keys, values)
    return keys, values
    
def population_by_contry(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result

