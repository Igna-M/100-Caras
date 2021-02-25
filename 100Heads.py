import random
import time

def tossCoin():
    global totalTosses
    result = random.choice(['head', 'tail'])
    return result



# Store Results
each_result = ['Para empezar']
max_len = 0

new_amount_rep = []

objetivo = 100
maxProcess = 50000000

sim_numb = 0
while len(each_result) < objetivo:
    if sim_numb != 0 and sim_numb % 5000000 == 0:
        print('')
        print('Llegamos a los', sim_numb, 'tosses.')
        if max_len > 20 and sim_numb > 19999999:
            print('Máximo de coincidencias seguidas:', max_len)
            print(new_amount_rep[-3:])
            # time.sleep(0.5)

    
    toss = tossCoin()
    sim_numb += 1

    if toss == each_result[-1]:
        each_result.append(toss)
        if len(each_result) > max_len:
            new_amount_rep.append([len(each_result), sim_numb])
            max_len = len(each_result)
            if max_len > 10 and max_len % 5 == 0:
                print('NUEVO MAX:', new_amount_rep[-5:])
                time.sleep(0.5)
    else:
        each_result.clear()
        each_result.append(toss)

    if len(each_result) == objetivo:
        print('')
        print('FELICITACIONES!!!!')
        print('Llegamos a los', objetivo, 'en', sim_numb, 'tosses')
        print(new_amount_rep)
        print('')
        for i in range(len(new_amount_rep)):
            print('Coincidencias:', new_amount_rep[i][0], '- Tosses:', new_amount_rep[i][1])

        print('')
    
    if sim_numb > maxProcess:
        print('')
        print('Se complicó!!!!')
        print('Nos quedamos en', max_len, 'coincidencias, en', sim_numb, 'tosses')
        print('')
        for i in range(len(new_amount_rep)):
            print('Coincidencias:', new_amount_rep[i][0], '- Tosses:', new_amount_rep[i][1])

        break

print('')
print('Gracias por venir...')
print('Vuelva pronto...')
print('')