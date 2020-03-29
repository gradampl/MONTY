region_capitals = {'Białystok', 'Bydgoszcz', 'Gdańsk', 'Gorzów', 'Katowice', 'Kielce',
                   'Kraków', 'Lublin', 'Łódź', 'Olsztyn', 'Opole', 'Poznań', 'Rzeszów',
                   'Szczecin', 'Toruń', 'Warszawa', 'Wrocław', 'Zielona Góra'}


over_240_k = {'Warszawa', 'Kraków', 'Łódź', 'Wrocław', 'Poznań', 'Gdańsk', 'Szczecin',
              'Bydgoszcz', 'Lublin', 'Białystok', 'Katowice', 'Gdynia'}


over_100_k = {'Warszawa', 'Kraków', 'Łódź', 'Wrocław', 'Poznań', 'Gdańsk', 'Szczecin',
              'Bydgoszcz', 'Lublin', 'Białystok', 'Katowice', 'Gdynia', 'Częstochowa',
              'Radom', 'Sosnowiec', 'Toruń', 'Kielce', 'Rzeszów'}

print(region_capitals | over_240_k | over_100_k) # suma zbiorów
print(region_capitals & over_240_k & over_100_k) # iloczyn zbiorów
print(region_capitals - over_240_k) # różnica zbiorów