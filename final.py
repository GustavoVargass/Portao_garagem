import serial
import Main
conexao = serial.Serial('COM3', 9600)
plateImagePath = 'LicPlateImages/br2.png'
allowedPlates = [
    'PLACA011'
    'BEE5R22'
]
plateNumber = Main.main(plateImagePath)
# O(pen) / C(lose)
print(f'Placa lida: {plateNumber}')
if plateNumber in str(allowedPlates):
    print('Abrindo...')
    conexao.write(b'O') # Open
else:
    print('Fechando...')
    conexao.write(b'C') # Close
conexao.close()
