def population_by_country(data, country):
    result = list(filter(lambda x: x['Pais'] == country, data))
    for i in result:
        for value in i.values():
            x = value
    return x
