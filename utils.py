
def world_population(DATA):
  world_data = {
    item['Country']: item['World Population Percentage']  for item in DATA
  }
  labels = world_data.keys()
  values = world_data.values()
  return labels, values

if __name__ == '__main__':
  world_population(DATA)