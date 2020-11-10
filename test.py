import Main
from tabulate import tabulate


pathPrefix = 'LicPlateImages'
listOfImages = [
    '1.png',
    '2.png',
    '3.png',
    '4.png',
    '5.png',
    '6.png',
    '7.png',
    '8.png',
    '9.png',
    '10.png',
    '11.png',
    '12.png',
    '13.png',
    '14.png',
    '15.png',
    '16.png',
    'br1.jpg',
    'br2.png',
    'br3.jpg'
]
expectedResults = [
    'MCLRNF1',                # 1.png
    'LOLWATT',                # 2.png
    'RIPLS1',                 # 3.png
    'NICESKY',                # 4.png
    'NVSBLE',                 # 5.png
    'NYSJ',                   # 6.png
    'ANBYOND',                # 7.png
    '1ZM961',                 # 8.png
    'PNYEXPS',                # 9.png
    'ZOOMN65',                # 10.png
    'HOR5SH1T',               # 11.png
    'FALLYOU',                # 12.png
    'EZEY',                   # 13.png
    'NITESKY',                # 14.png
    'U8NTBAD',                # 15.png
    'GAY247',                 # 16.png
    'GKC4144',                # br1.jpg
    'BEE4R22',                # br2.png
    'AA000BZ'                 # br3.jpg
]
plateResults = []
successCount = 0
output = []
for index, image in enumerate(listOfImages):
    plateNumber = Main.main(f'{pathPrefix}/{image}')
    success = plateNumber == expectedResults[index]
    if success:
        successCount = successCount + 1
    output.append([plateNumber, expectedResults[index], success])
print(tabulate(output, headers=['Obtido', 'Esperado', 'Certo']))
print(f'\nNúmero de acertos: {successCount} / {len(expectedResults)}')