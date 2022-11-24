def ejecutaAlgoritmo():
	# En este espacio vamos a programar el algoritmo de path finding, A* (o A estrella)
	# Para desarrollar el GUI o la interfaz grafica donde el algoritmo se vera en accion utilizaremos el modulo pygame
	import pygame
	import math
	from queue import PriorityQueue

	#Basado en el codigo implementado por el usuario de
	# youtube "Tech With Tim", el cual se encuentra en el siguiente link:
	# https://www.youtube.com/watch?v=JtiK0DOeI4A

	# Ancho de la ventana donde se mostrara el laberinto. Como sera de un tamaño NxN el alto sera igual al ancho
	ANCHO = 800
	# Creamos la ventana donde se mostrara el laberinto
	VENTANA = pygame.display.set_mode((ANCHO, ANCHO))
	pygame.display.set_caption("M.A.T.E.C.I.T.O A* pathfinding")

	# Definimos los distintos colores en escala RGB
	ROJO = (255, 0, 0)
	VERDE = (0, 255, 0)
	AZUL = (0, 255, 0)
	AMARILLO = (255, 255, 0)
	BLANCO = (255, 255, 255)
	NEGRO = (0, 0, 0)
	PURPURA = (128, 0, 128)
	NARANJA = (255, 165, 0)
	GRIS = (128, 128, 128)
	TURQUESA = (64, 224, 208)

	# Vamos a manejar a los nodos del laberinto con paradigma orientado a objetos, de manera que cada nodo
	# sera un objeto de la clase Nodo, el cual tiene atributos que nos permiten conocer
	# su posicion, su color, sus vecinos, su ancho y alto, etc


	class Nodo:

		# Definimos el constructor
		# Tener en cuenta que aca en los parametros:
		# fila: es la fila en la que se encuentra el nodo
		# columna: es la columna en la que se encuentra el nodo
		# ancho: es el ancho y alto DEL NODO, no de la ventana
		# total_filas: es el total de filas que tiene el laberinto
		def __init__(self, fila, columna, ancho, total_filas):
			self.fila = fila
			self.columna = columna
			# Teniendo en cuenta que el eje X+ es vertical hacia abajo y el eje Y+ es horizontal hacia la derecha
			# Las coordenadas x e y me indican el vertice del cuadradito que forma el nodo
			self.x = fila * ancho
			self.y = columna * ancho
			self.color = BLANCO
			self.vecinos = []
			self.ancho = ancho
			self.total_filas = total_filas

		# Declaramos los metodos

		# El metodo get_pos es un getter que me va a retornar la fila y columna donde se encuentra el nodo
		def get_pos(self):
			return self.fila, self.columna

		# METODOS IS
		# La idea de los metodos is es verificar el estado de un nodo segun el color que este tenga
		# El valor de retorno siempre sera un atributo == COLOR. Esto es porque se llama a estos
		# metodos en los if, si se cumple se verifica la condicion en el if, si no no.
		# CLOSED verifica si el nodo esta en rojo, que significa que se encuentra en el closedset (nodo ya analizado)
		def is_closed(self):
			return self.color == ROJO
		# OPEN verifica si el nodo esta en verde, que significa que se encuentra en el openset (aun no verificada)

		def is_open(self):
			return self.color == VERDE
		# BARRIER verifica si el nodo esta en negro, que significa que es un obstaculo (A modificar)

		def is_barrier(self):
			return self.color == NEGRO
		# START verifica si el nodo esta en naranja, que significa que es el punto inicial

		def is_start(self):
			return self.color == NARANJA
		# END verifica si el nodo esta en turquesa, que significa que es el punto final

		def is_end(self):
			return self.color == TURQUESA

		# El metodo reset torna el nodo nuevamente en blanco
		def reset(self):
			self.color = BLANCO

		# METODOS MAKE
		# Establece el color de los nodos
		# Establecemos el nodo de inicio en color naranja
		def make_start(self):
			self.color = NARANJA
		# Establecemos el nodo de closedset en color rojo

		def make_closed(self):
			self.color = ROJO
		# Establecemos el nodo de openset en color verde

		def make_open(self):
			self.color = VERDE
		# Establecemos el nodo de obstaculo en color negro (A modificar)

		def make_barrier(self):
			self.color = NEGRO
		# Establecemos el nodo final en color turquesa

		def make_end(self):
			self.color = TURQUESA
		# Establecemos el nodo de camino en color purpura

		def make_path(self):
			self.color = PURPURA

		# Con el metodo draw dibujamos el nodo (cuadradito) en la ventana que ya creamos antes.
		# Le pasamos la ventana donde queremos dibujarlo, las coordenadas del vertice del cubito, su ancho y largo(mismo que ancho)
		def draw(self, ventana):
			pygame.draw.rect(ventana, self.color,
							(self.x, self.y, self.ancho, self.ancho))

		# Con este metodo lo que hacemos es checkear lo que rodea a nuestro nodo.Si es un openset,closedset,barrier(obstaculo),start o end
		# Basicamente siempre que mis vecinos no sean obstaculos, los agrego dentro de mi lista de vecinos
		# Esto lo hago para que el algoritmo identifique cuando llegue a una barrera y no siga indagando sobre la misma
		# como posible vecino a ir, debido a que no puede
		def update_neighbors(self, grid):
			self.vecinos = []
			# OBSTACULO ABAJO
			if self.fila < self.total_filas - 1 and not grid[self.fila + 1][self.columna].is_barrier():
				self.vecinos.append(grid[self.fila + 1][self.columna])

			# OBSTACULO ARRIBA
			if self.fila > 0 and not grid[self.fila - 1][self.columna].is_barrier():
				self.vecinos.append(grid[self.fila - 1][self.columna])

			# OBSTACULO DERECHA
			if self.columna < self.total_filas - 1 and not grid[self.fila][self.columna + 1].is_barrier():
				self.vecinos.append(grid[self.fila][self.columna + 1])

			# OBSTACULO IZQUIERDA
			if self.columna > 0 and not grid[self.fila][self.columna - 1].is_barrier():
				self.vecinos.append(grid[self.fila][self.columna - 1])

		# Con este metodo lt lo que hago es comparar el nodo actual con el nodo other y retornar un False

		def __lt__(self, other):
			return False
	# Fin de la clase Nodo

	# Definimos la funcion heuristica con distancia de manhattan (tambien llamada taxi cab distance)


	def h(p1, p2):
		# P1 es un punto y P2 es otro punto
		# Con esta sintaxis obtenemos las coordenadas en x y en y de cada punto
		x1, y1 = p1
		x2, y2 = p2
		return abs(x1 - x2) + abs(y1 - y2)


	def reconstruct_path(came_from, current, draw):
		while current in came_from:
			current = came_from[current]
			current.make_path()
			draw()


	def algorithm(draw, grid, start, end):
		count = 0
		open_set = PriorityQueue()
		open_set.put((0, count, start))
		came_from = {}
		g_score = {spot: float("inf") for row in grid for spot in row}
		g_score[start] = 0
		f_score = {spot: float("inf") for row in grid for spot in row}
		f_score[start] = h(start.get_pos(), end.get_pos())

		open_set_hash = {start}

		while not open_set.empty():
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()

			current = open_set.get()[2]
			open_set_hash.remove(current)

			if current == end:
				reconstruct_path(came_from, end, draw)
				end.make_end()
				return True

			for neighbor in current.vecinos:
				temp_g_score = g_score[current] + 1

				if temp_g_score < g_score[neighbor]:
					came_from[neighbor] = current
					g_score[neighbor] = temp_g_score
					f_score[neighbor] = temp_g_score + \
						h(neighbor.get_pos(), end.get_pos())
					if neighbor not in open_set_hash:
						count += 1
						open_set.put((f_score[neighbor], count, neighbor))
						open_set_hash.add(neighbor)
						neighbor.make_open()

			draw()

			if current != start:
				current.make_closed()

		return False

	# Funcion para construir la cuadricula con los nodos en la ventana que creamos anteriormente
	# Solo le pedimos rows(filas) y no colum(columnas) porque tendremos el mismo numero de ambas
	# Lo que hacemos es basicamente crear una matriz o una lista de listas


	def make_grid(rows, width):
		grid = []
		gap = width // rows  # Ancho de cada nodo en el grid
		for i in range(rows):
			grid.append([])
			for j in range(rows):
				nodo = Nodo(i, j, gap, rows)
				grid[i].append(nodo)

		return grid

	# La anterior funcion nos setea los cuadrados, pero no la separacion entre ellos, para
	# eso creamos la funcion draw_grid

	# Funcion para dibujar las lineas de cuadricula (lineas entre nodos)
	def draw_grid(win, rows, width):
		gap = width // rows
		for i in range(rows):
			pygame.draw.line(win, GRIS, (0, i * gap), (width, i * gap))
			for j in range(rows):
				pygame.draw.line(win, GRIS, (j * gap, 0), (j * gap, width))


	# Funcion "main" de dibujo, es la que dibuja todo
	def draw(win, grid, rows, width):
		# Cada vez que actualizamos transformamos todo a blanco y luego lo cambiamos mas abajo
		# Es una forma de borrar lo que estaba
		win.fill(BLANCO)

		for row in grid:
			for nodo in row:
				# Aca utilizamos el METODO DE LA CLASE NODO .draw
				nodo.draw(win)

		draw_grid(win, rows, width)
		pygame.display.update()

	# Para que el programa identifique donde posiciono el mouse
	def get_clicked_pos(pos, rows, width):
		gap = width // rows
		y, x = pos

		row = y // gap
		col = x // gap

		return row, col

	# Iniciamos la definicion del main, donde todo lo que declaramos antes sera utilizado y aplicado junto


	def main(win, ancho):
		FILAS = 12  # Numero de filas (y de columnas)
		grid = make_grid(FILAS, ancho)  # Crea el grid(matriz de nodos)

		start = None  # Posicion inicial
		end = None  # Posicion final

		run = True  # Variable para hacer seguimiento a ver si el algoritmo esta activo o no
		while run:
			draw(win, grid, FILAS, ancho)
			# Aca lo que vamos a hacer es recorrer todos los eventos que suceden en pygame
			# Si alguno de ellos corresponde al atributo pygame.ARTRIBUTO, asignamos una accion
			for event in pygame.event.get():
				# Si el tipo de evento es un pygame.QUIT dejamos de runear el programa
				if event.type == pygame.QUIT:
					run = False

				# Si el evento es un click izquierdo.Pinta de uno de estos colores los nodos
				if pygame.mouse.get_pressed()[0]:  # Si hacemos click izquierdo
					posicion = pygame.mouse.get_pos()
					fila, columna = get_clicked_pos(posicion, FILAS, ancho)
					nodo = grid[fila][columna]

					# Si no hay nodo inicial, lo seteamos
					# Establecemos una segunda condicion de que no tiene que ser el nodo end, para no sobreescribirlos
					if not start and nodo != end:
						start = nodo
						start.make_start()

					# Si no hay nodo final, lo seteamos
					# Lo mismo que arriba pero con start
					elif not end and nodo != start:
						end = nodo
						end.make_end()

					# Si no es ninguno de los anteriores, lo seteamos como un obstaculo
					# Lo mismo que arriba pero con end y start
					elif nodo != end and nodo != start:
						nodo.make_barrier()

				# Si el evento es un click derecho.Borra los nodos colocados, o mas bien los reestablece en el color neutro
				elif pygame.mouse.get_pressed()[2]:  # Si hacemos click derecho
					posicion = pygame.mouse.get_pos()
					fila, columna = get_clicked_pos(posicion, FILAS, ancho)
					nodo = grid[fila][columna]
					nodo.reset()
					if nodo == start:
						start = None
					elif nodo == end:
						end = None

				# Con esto decimos que si el evento es presionar la barra espaciadora, se identifiquen los vecinos
				# alrededor de los nodos, para saber cuales nodos son efectivamente por los cuales podemos pasar
	# y finalmente ejecutamos el algoritmo A*
				# Si la tecla que tocamos es "C" reseteamos todo a blanco
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE and start and end:
						for fila in grid:
							for nodo in fila:
								nodo.update_neighbors(grid)
						#Para llamar al algoritmo Aestrella, utilizamos una funcion lambda, que simplemente es una funcion de una sola linea
						#Esta funcion como vemos llama a la funcion draw
						#Los otros parametros son grid, start y end
						#El usar una f. lambda lo hacemos para poder meter una llamada a funcion como parametro de otra funcion
						#Caso contrario no podriamos hacerlo
						algorithm(lambda: draw(win, grid, FILAS, ancho),
								grid, start, end)

					if event.key == pygame.K_c:
						start = None
						end = None
						grid = make_grid(FILAS, ancho)

		pygame.quit()

	main(VENTANA, ANCHO)


