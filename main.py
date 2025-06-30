from domain.entities.tablero import Tablero
from domain.entities.bala import Bala
from domain.entities.celda import Celda

def main():
    tablero=Tablero(3,4)
    print(tablero)
    tablero.build_celdas()
    print("nro filas= ",len(tablero.celdas))
    print("nro columnas= ", len(tablero.celdas[0]) )
    print(tablero)
    nro_balas=3



    while True and nro_balas>0:
        nro_balas=nro_balas-1
        ingreso=input("ingrese coordenada x: ")
        print(ingreso)
        if ingreso=="exit":
            break
        if ingreso.isnumeric():
            x_coor=int(ingreso)
            y_coor=int(input("ingrese coordenada y: "))
            print(y_coor)
            if tablero.validate_coordinates(x_coor,y_coor):
                tiro=Bala(Celda(x_coor,y_coor))
                print(tiro)
                impacto=tablero.check_collition_and_replace_cell(tiro)
                print(impacto)
                print(tablero)
                print("Balas disponibles= ", nro_balas)
                if tablero.nro_acorazados==3:
                    print("GANASTE")
                    break

        else:
            print("Ingrese un valor entero o exit")





if __name__ == "__main__":
    main()
