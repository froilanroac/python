from datetime import time,timedelta
from data_collection.collector import get_data
import controller.config as config
from controller.tools import clear_screen

def data():
    if len(config.runners) > 0:
        return True
    else:
        return False

def load_runners():
    clear_screen()
    f_name = input('Please, type the filename with extension:\n(if it is empty, the system will take the default name competencia.txt):\n')
    if f_name:
        data = get_data(file_name=f_name)
    else:
        print('Taking default filename...')
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

    if len(juniors) > 0:
        runners.update({"Juniors" : juniors[0]})
    if len(seniors) > 0:   
        runners.update({"Seniors" : seniors[0]})
    if len(masters) > 0:
        runners.update({"Masters" : masters[0]})
    
    return runners

def histogram_data():
    runners = {}
    total_runners = len(config.runners)
    if total_runners > 0:
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

    if len(male) > 0:
        runners.update({"male" : male[0]})
    if len(female) > 0:
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

    if len(juniors_m) > 0:
        runners.update({"Juniors_Male" : juniors_m[0]})
    if len(juniors_f) > 0:
        runners.update({"Juniors_Female" : juniors_f[0]})
    if len(seniors_m) > 0:
        runners.update({"Seniors_Male" : seniors_m[0]})
    if len(seniors_f) > 0:
        runners.update({"Seniors_Female" : seniors_f[0]})
    if len(masters_m) > 0:
        runners.update({"Masters_Male" : masters_m[0]})
    if len(masters_f) > 0:
        runners.update({"Masters_Female" : masters_f[0]})

    return runners
    
def general_winner():
    runner = [x for x in config.runners]
    if len(runner) > 0:
        return runner[0]
    else:
        return []

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
    if len(list) > 0:
        for i in list:
            aux.append(i.strftime("%H:%M:%S"))
        return str(timedelta(seconds=sum(map(lambda f: int(f[0])*3600 + int(f[1])*60 + int(f[2]), map(lambda f: f.split(':'), aux)))/len(aux)))
    else:
        return 0



    
