import charts
import read_csv
import utils

DATA = read_csv.read_csv('./dataset.csv')

def run():
  labels, values = utils.world_population(DATA)
  charts.generate_pie_chart(labels, values)

if __name__ == '__main__':
  run()