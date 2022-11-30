;Definimos el problema, modificable segun el orden inicial que se de en el examen final y el orden final que se pida
;En este caso el orden inicial es, de arriba hacia abajo Tuercas->Clavos->Arandelas->Tornillo
;Queremos llegar a  Arandelas->Tuercas->Tornillos->Clavos
(define (problem orden-cajas-problema) (:domain orden-cajas2)
    (:objects arandelas tuercas clavos tornillos base1)
    (:init
        (caja arandelas) (caja tuercas) (caja clavos) (caja tornillos) (basepos base1)
        (sobre tuercas tornillos) (sobre tornillos clavos) (sobre clavos arandelas)
     	(base arandelas) (nadaEncima tuercas) (not(clear base1))
    )
    (:goal (
        and
        (sobre arandelas tornillos) (sobre tornillos tuercas) (sobre tuercas clavos) (base clavos)
        )
    )
)