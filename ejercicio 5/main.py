import csv

def read_csv(path):
   sum = 0
   with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile)
      for data_set in reader:
         sum += int(data_set[1])
   return sum
   
sum_csv = read_csv('./ejercicio 5/data.csv')
print(sum_csv)