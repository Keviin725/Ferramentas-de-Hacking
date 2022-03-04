from threading import Thread
import time

def corrida(velocidade, piloto):
    trajeto = 0
    while trajeto < 100:
        trajeto += velocidade
        time.sleep(0.5)
        print('Piloto: {} Km/h: {} \n'.format(piloto, trajeto))



t_carro1 = Thread(target = corrida, args =[1, 'Kevin'])
t_carro2 = Thread(target = corrida, args =[1.5, 'Savage'])

t_carro1.start()
t_carro2.start()

