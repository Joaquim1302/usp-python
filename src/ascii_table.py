print("Tabela ASCII de 32 a 127: ")
for i in range(32, 128, 3):
    print(f"ASCII[ {i:3d} ] = '{chr(i):s}'  |  "
          + f"ASCII[ {i+1:3d} ] = '{chr(i+1):s}'  |  "
          + f"ASCII[ {i+2:3d} ] = '{chr(i+2):s}'  ")
