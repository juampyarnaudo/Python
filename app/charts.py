import matplotlib.pyplot as plt

#con el as plt, es como poner un sinonimo para cuando ponga esa libreria sea con un nombre mas acotado.


#generar la grafica
def generate_bar_chart(labels, values):

  #2 variables, fig es la figura y ax son las coordenadas.
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()


def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()


if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [100, 20, 400]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)
