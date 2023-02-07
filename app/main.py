import utils
import read_csv
import charts
'''
data = [
        {
            'Country': 'Colombia',
            'Population': 300
        },
        {
            'Country': 'Bolivia',
            'Population': 350
        }
    ]
'''
def run():
    data = read_csv.read_csv('./app/data.csv')
    country = input('Type Country => ')

    #filtro para guardar los paises que son de South America
    data = list(filter(lambda item:item['Continent' == 'South America', data]))


    #selecciono toda la columna de paises:
    countries = list(map(lambda x: x['Country'], data))
    #selecciono toda la columnna de los porcentajes
    percengaes = list(map(lambda x:x['World Population Percentage', data])) 
    #genero un grafico de torta
    charts.generate_pie_chart(countries, percengaes)



    result = utils.population_by_contry(data, country)
    if len(result)>0:
        country = result[0]
        keys, values = utils.get_population(country)
        #charts.generate_bar_chart(labels, values)
        print(result)
        
# Se le llama: Entry point
# este if le dice al archivo main.py que si se esta ejecutando desde una terminal, lo haga al metodo run(), pero si se ejecuta desde otro archivo, no lo haga.
    if __name__ == '__main__':
        run()