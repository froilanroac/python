from datetime import time
from data_collection.collector import get_data
import controller.config as config

def load_runners():
    data = get_data()
    config.runners = arrange_runners(data)

def arrange_runners(data):
    runners = []
    for line in data:
        d = {
            'id': line[0],
            'firstLastName':line[1],
            'secondLastName': line[2],
            'firstName': line[3],
            'initialSecondName': line[4],
            'sex': line[5],
            'age': int(line[6]),
            'time': time(int(line[7]),int(line[8]),int(line[9]))
            }
        runners.append(d)
    runners.sort(key=lambda r: r['time'])
    return runners
    
def juniors(runners):
    juniors = [x for x in runners if int(x['age']) < 25]
    juniors.sort(key=lambda r: r['time2'])
    return juniors

def seniors(runners):
    seniors = [x for x in runners if int(x['age']) >= 25 and int(x['age']) <= 40]
    seniors.sort(key=lambda r: r['time2'])
    return seniors

def masters(runners):
    masters = [x for x in runners if int(x['age']) > 40]
    masters.sort(key=lambda r: r['time2'])
    return masters

    
