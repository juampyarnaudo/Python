import utils

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

def run():
    keys, values = utils.get_population()
    #print(keys, values)



    country = input('Tipe Country => ')

    result = utils.population_by_contry(data, 'Colombia')
    print(result)

# Se le llama: Entry point
# este if le dice al archivo main.py que si se esta ejecutando desde una terminal, lo haga al metodo run(), pero si se ejecuta desde otro archivo, no lo haga.
    if __name__ == '__main__':
        run()