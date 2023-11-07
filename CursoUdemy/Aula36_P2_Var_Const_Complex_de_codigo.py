"""
Constante = 'variaveis que não mudam nunca'
muitas condições no mesmo if (ruim)
    <- contagem de complexidade (RUIM)

"""

velocidade = 100 # velocodade atual do carro
local_carro = 101 # local que o carro esta 

RADAR_1 = 80 # velocidade máxima radar 1
LOCAL_1 = 100 # local do radar 1
RADAR_RANGE = 1 # distância que o radar alcança

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1

if velocidade_carro_passou_radar_1:
    print('velocidade excedida no radar 1')

if carro_multado_radar_1 and velocidade_carro_passou_radar_1:
    print('Multaaaaaa')






