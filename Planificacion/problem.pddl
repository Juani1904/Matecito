;Definimos el problema, modificable segun el orden inicial que se de en el examen final y el orden final que se pida
;En este caso el orden inicial es, de arriba hacia abajo Arandela->Tuerca->Clavo->Tornillo
;Queremos llegar a  Tuerca->Tornillo->Arandela->Clavo
(define (problem orden-cajas-problema) (:domain orden-cajas2)
    (:objects arandelas tuercas clavos tornillos)
    (:init
        (caja arandelas) (caja tuercas) (caja clavos) (caja tornillos)
        (sobre arandelas tuercas) (sobre tuercas clavos) (sobre clavos tornillos)
     	(desapilado tornillos) (nadaEncima arandelas)
    )
    (:goal (
        and
        (sobre tuercas tornillos) (sobre tornillos arandelas) (sobre arandelas clavos)
        )
    )
)