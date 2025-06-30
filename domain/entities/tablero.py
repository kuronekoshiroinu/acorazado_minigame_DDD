import random
from dataclasses import dataclass
from typing import List, Union
from domain.entities.acorazado import Acorazado
from domain.entities.bala import Bala
from domain.entities.celda import Celda


@dataclass
class Tablero:
    dimension_vertical: int
    dimension_horizontal: int
    celdas: List[Union[Celda,Acorazado]]=None
    nro_acorazados: int=3


    def build_celdas(self):
        self.celdas=[]
        for i in range(self.dimension_vertical):
            fila=[]
            for j in range(self.dimension_horizontal):
                celda_or_acorazado=self.get_celda_or_acorazado(i,j)
                fila.append(celda_or_acorazado)
            self.celdas.append(fila)

    def get_celda_or_acorazado(self,i:int,j:int)->Union[Celda,Acorazado]:
        if self.nro_acorazados>0 and random.random()>0.7:
            self.nro_acorazados = self.nro_acorazados -1
            return Acorazado(Celda(i,j))
        return Celda(i,j)

    def validate_coordinates(self, x:int, y:int):
        if x<=self.dimension_horizontal and y<=self.dimension_vertical:
            return True
        return False

    def check_collition_and_replace_cell(self, bala:Bala):
        if isinstance(self.celdas[bala.position_bullet.position_x_cell][bala.position_bullet.position_y_cell],Acorazado):
            print("hubo impacto")
            self.nro_acorazados=self.nro_acorazados+1
            self.celdas[bala.position_bullet.position_x_cell][bala.position_bullet.position_y_cell]=Celda(bala.position_bullet.position_x_cell,bala.position_bullet.position_y_cell)
            return True
        else:
            print("NO hubo impacto")
            return False

