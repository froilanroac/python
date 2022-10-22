from datetime import time,timedelta
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

def participants_by_age():
    runners = {}
    runners.update({"Juniors" : len([x for x in config.runners if int(x['age']) < 25])})
    runners.update({"Seniors" : len([x for x in config.runners if int(x['age']) >= 25 and int(x['age']) <= 40])})
    runners.update({"Masters" : len([x for x in config.runners if int(x['age']) > 40])})
    return runners

def participants_by_sex():
    runners = {}
    runners.update({"Male"  : len([x for x in config.runners if x['sex'].upper() == "M"])})
    runners.update({"Female": len([x for x in config.runners if x['sex'].upper() == "F"])})
    return runners

def winners_by_age():
    runners = {}
    juniors = [x for x in config.runners if int(x['age']) < 25]
    juniors.sort(key=lambda r: r['time'])
    seniors = [x for x in config.runners if int(x['age']) >= 25 and int(x['age']) <= 40]
    seniors.sort(key=lambda r: r['time'])
    masters = [x for x in config.runners if int(x['age']) > 40]
    masters.sort(key=lambda r: r['time'])

    runners.update({"Juniors" : juniors[0]})
    runners.update({"Seniors" : seniors[0]})
    runners.update({"Masters" : masters[0]})
    
    return runners

def histogram_data():
    runners = {}
    total_runners = len(config.runners)
    juniors = len([x for x in config.runners if int(x['age']) < 25]) * 100 / total_runners
    seniors = len([x for x in config.runners if int(x['age']) >= 25 and int(x['age']) <= 40]) * 100 / total_runners
    masters = len([x for x in config.runners if int(x['age']) > 40]) * 100 / total_runners
    runners.update({"juniors" : juniors})
    runners.update({"seniors" : seniors})
    runners.update({"masters" : masters})
    return runners

def winners_by_sex():
    runners = {}
    male = [x for x in config.runners if x['sex'].upper() == 'M']
    male.sort(key=lambda r: r['time'])
    female = [x for x in config.runners if x['sex'].upper() == 'F']
    female.sort(key=lambda r: r['time'])

    runners.update({"male" : male[0]})
    runners.update({"female" : female[0]})


    return runners

def winners_by_sex_age():
    runners = {}
    juniors_m = [x for x in config.runners if int(x['age']) < 25 and x['sex'].upper() == 'M']
    juniors_m.sort(key=lambda r: r['time'])

    juniors_f = [x for x in config.runners if int(x['age']) < 25 and x['sex'].upper() == 'F']
    juniors_f.sort(key=lambda r: r['time'])

    seniors_m = [x for x in config.runners if int(x['age']) >= 25 and int(x['age']) <= 40 and x['sex'].upper() == 'M']
    seniors_m.sort(key=lambda r: r['time'])
    seniors_f = [x for x in config.runners if int(x['age']) >= 25 and int(x['age']) <= 40 and x['sex'].upper() == 'F']
    seniors_f.sort(key=lambda r: r['time'])
    masters_m = [x for x in config.runners if int(x['age']) > 40 and x['sex'].upper() == 'M']
    masters_m.sort(key=lambda r: r['time'])
    masters_f = [x for x in config.runners if int(x['age']) > 40 and x['sex'].upper() == 'F']
    masters_f.sort(key=lambda r: r['time'])

    runners.update({"Juniors_Male" : juniors_m[0]})
    runners.update({"Juniors_Female" : juniors_f[0]})
    runners.update({"Seniors_Male" : seniors_m[0]})
    runners.update({"Seniors_Female" : seniors_f[0]})
    runners.update({"Masters_Male" : masters_m[0]})
    runners.update({"Masters_Female" : masters_f[0]})

    return runners
    
def general_winner():
    runners = [x for x in config.runners]
    return runners[0]

def average_age_sex():
    runners = {}
    
    runners.update({"juniors_male": time_average([x['time'] for x in config.runners if int(x['age']) < 25 and x['sex'].upper() == 'M'])})
    runners.update({"juniors_female": time_average([x['time'] for x in config.runners if int(x['age']) < 25 and x['sex'].upper() == 'F'])})
    runners.update({"seniors_male": time_average([x['time'] for x in config.runners if int(x['age']) >= 25 and int(x['age']) <= 40 and x['sex'].upper() == 'M'])})
    runners.update({"seniors_female": time_average([x['time'] for x in config.runners if int(x['age']) >= 25 and int(x['age']) <= 40 and x['sex'].upper() == 'F'])})
    runners.update({"masters_male": time_average([x['time'] for x in config.runners if int(x['age']) > 40 and x['sex'].upper() == 'M'])})
    runners.update({"masters_female": time_average([x['time'] for x in config.runners if int(x['age']) > 40 and x['sex'].upper() == 'F'])})

    return runners

def time_average(list):
    aux = []
    for i in list:
        aux.append(i.strftime("%H:%M:%S"))
    return str(timedelta(seconds=sum(map(lambda f: int(f[0])*3600 + int(f[1])*60 + int(f[2]), map(lambda f: f.split(':'), aux)))/len(aux)))



    
