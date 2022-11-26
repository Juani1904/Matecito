;Primero vamos a definir el dominio
(define (domain orden-cajas2)
    (:requirements :negative-preconditions)
    ;Definimos los predicados con los que vamos a trabajar
    (:predicates
        (caja ?x) (sobre ?x ?y) (mesa ?x) (nadaEncima ?x) (base ?x) (basepos ?x) (clear ?x) 
    )
    ;Definimos la funcion sacar, la cual me sirve para desapilar (pop) de mi pila o stack
    (:action sacar
        ;Los parametros con los que trabajaremos seran simplemente 2 cajas
        :parameters (?c1 ?c2)
        ;Las precondiciones son: Que c1 y c2 sean cajas que c1 este encima de c2 y que no haya nada encima de c1 (caja superior)
        :precondition (
            and (caja ?c1) (caja ?c2) (sobre ?c1 ?c2)
                (nadaEncima ?c1) (not(base ?c1))
        )
        ;Si esto se cumple el efecto sera que c1 no este mas sobre c2, que se encuentre desapilado y que no haya nada encima de c2
        ;El hecho de que c1 se encuentre "desapilado" da la posibilidad a que este sea la base de la pila luego
        ;No bastaria decir que c1 no tiene nada encima porque en este caso no tiene nada encima, pero no es la caja superior
        :effect (
            and (not(sobre ?c1 ?c2)) (mesa ?c1) (nadaEncima ?c2)
        )
    )

    (:action sacar-base
        ;Los parametros con los que trabajaremos seran simplemente 2 cajas
        :parameters (?c ?b)
        ;Las precondiciones son: Que c1 y c2 sean cajas que c1 este encima de c2 y que no haya nada encima de c1 (caja superior)
        :precondition (
            and (caja ?c) (basepos ?b) (base ?c) (not(clear ?b)) 
                (nadaEncima ?c)
        )
        ;Si esto se cumple el efecto sera que c1 no este mas sobre c2, que se encuentre desapilado y que no haya nada encima de c2
        ;El hecho de que c1 se encuentre "desapilado" da la posibilidad a que este sea la base de la pila luego
        ;No bastaria decir que c1 no tiene nada encima porque en este caso no tiene nada encima, pero no es la caja superior
        :effect (
            and  (mesa ?c) (not(base ?c)) (clear ?b)
        )
    )
	;Definimos la funcion poner, que me sirve para desapilar (push) una caja de mi pila o stack
  	(:action poner
        ;Vamos a trabajar nuevamente con 2 cajas
        :parameters (?c1 ?c2)
        ;Esta vez las precondiciones son que c1 y c2 sean cajas, que c1 que sencuentre desapilado y que no haya ninguna caja encima de c2
        ;Si esto se cumple entonces el robot colocara la caja c1 sobre c2, c1 dejara de estar desapilado y c2 comenzara a tener una caja encima
        ;Sin embargo c1 para a no tener nada encima
        :precondition (
            and (caja ?c1) (caja ?c2) (mesa ?c1) (nadaEncima ?c2)
        )

        :effect (
            and (sobre ?c1 ?c2) (not(mesa ?c1)) (not(nadaEncima ?c2))
        )
    )
  	
  	(:action poner-base
        ;Vamos a trabajar nuevamente con 2 cajas
        :parameters (?c ?b)
        ;Esta vez las precondiciones son que c1 y c2 sean cajas, que c1 que sencuentre desapilado y que no haya ninguna caja encima de c2
        ;Si esto se cumple entonces el robot colocara la caja c1 sobre c2, c1 dejara de estar desapilado y c2 comenzara a tener una caja encima
        ;Sin embargo c1 para a no tener nada encima
        :precondition (
            and (caja ?c) (basepos ?b) (mesa ?c) (nadaEncima ?c) (clear ?b)
        )

        :effect (
            and  (not(mesa ?c)) (base ?c) (not(clear ?b))
        )
    )
  )