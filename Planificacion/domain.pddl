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
        ;Ademas c1 no debe ser la caja base
        :precondition (
            and (caja ?c1) (caja ?c2) (sobre ?c1 ?c2)
                (nadaEncima ?c1) (not(base ?c1))
        )
        ;Si esto se cumple el efecto sera que c1 no este mas sobre c2, que se encuentre desapilado y que no haya nada encima de c2
        :effect (
            and (not(sobre ?c1 ?c2)) (mesa ?c1) (nadaEncima ?c2)
        )
    )

    ;Definimos la funcion sacar-base, la cual es un caso especial de la funcion sacar para el caso donde la caja a retirar es la caja base
    (:action sacar-base
        ;Los parametros con los que trabajaremos es 1 caja y la base, pero ahora la base como parametro de posicion
        :parameters (?c ?b)
        ;Las precondiciones son: que c sea una caja, que b sea la posicion base, que c este en la base y que la base no este vacia
        :precondition (
            and (caja ?c) (basepos ?b) (base ?c) (not(clear ?b)) 
                (nadaEncima ?c)
        )
        
        ;Cumpliendose esto, c pasaria a esta desapilada, por ende no se encontraria en la base, y ademas la posicion base quedaria vacia
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
        :precondition (
            and (caja ?c1) (caja ?c2) (mesa ?c1) (nadaEncima ?c2)
        )

        :effect (
            and (sobre ?c1 ?c2) (not(mesa ?c1)) (not(nadaEncima ?c2))
        )
    )
  	
  	;Definimos la funcion poner-base, caso especial de poner, donde en este caso lo que se coloca es la caja en la poscion base
  	(:action poner-base
        ;Los parametros con los que trabajamos son una caja y la posicion base
        :parameters (?c ?b)
        
        ;Las precondiciones en este caso son que c sea una caja, que la posicion base sea b, que c se encuentre desapilado (sobre la mesa), no tenga
        ;nada encima y la posicion base este despejada.
        :precondition (
            and (caja ?c) (basepos ?b) (mesa ?c) (nadaEncima ?c) (clear ?b)
        )

        ;Si todo esto se cumple ele fecto sera que c dejara de estar desapilada, se coloca como caja base y la posicion base deja de estar vacia
        :effect (
            and  (not(mesa ?c)) (base ?c) (not(clear ?b))
        )
    )
  )