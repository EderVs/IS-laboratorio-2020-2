def decoratorFunction(f):
	def new_function(matrix):
		print("Before function")
		f(matrix)
		print("After function")
	return new_function

@decoratorFunction
def espejo(matriz):
	nueva=[]
	i = 0;
	for renglon in matriz:
		aux=[]
		j = len(renglon)-1
		for elemento in renglon:
			aux.append(matriz[i][j])
			j-=1
		nueva.append(aux)
		i+=1
	print(nueva)
	return nueva

espejo([[1,2,3],[4,5,6],[7,8,9]])