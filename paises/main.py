from funciones import population_by_country
paises = [
    {
    'Pais': 'Colombia',
    'Poblacion': 51609474
    },
    {
    'Pais': 'Bolivia',
    'Poblacion': 11673021
    },
    {
    'Pais': 'Brasil',
    'Poblacion': 212559417
    },
    {
    'Pais': 'Perú',
    'Poblacion': 33050325
    },
    {
    'Pais': 'Uruguay',
    'Poblacion': 3473730
    },
    {
    'Pais': 'Argentina',
    'Poblacion': 47327407
    },
    {
    'Pais': 'Ecuador',
    'Poblacion': 17643054
    },
    {
    'Pais': 'Paraguay',
    'Poblacion': 7132538
    },
]

pais = str(input('Introduce el pais del cual quieres saber su población: '))
pais = pais.title()
result = population_by_country(paises, pais)
print(f'La población del pais {pais} es {result} millones de personas')
