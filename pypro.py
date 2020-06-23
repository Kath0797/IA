from bottle import request, route, run, template
from pyswip import Prolog

prolog = Prolog()
# Open tree
prolog.consult("familia.pl")

@route('/agregarfamilia', method='POST')
def agregarfamilia():
	data = request.json
	for d in data["padres"]:
		prolog.assertz('padres("'+d[0]+'","'+d[1]+'")')
	return data

@route('/tio', method='POST')
def tio():
	data = request.json
	for d in data["estio"]:
		print(d[0])
		print(d[1])
		tt = prolog.query('tios("'+d[0]+'","'+d[1]+'")')
		T = list(tt)
	if T :
		return {"Respuesta" : T[0]} 
	else: 
		return{"Respuesta" : T} 

@route('/primo', method='POST')
def primos():
	data = request.json

	for d in data["esprimo"]:
		print(d[0])
		print(d[1])
		pp = prolog.query('primos("'+d[0]+'","'+d[1]+'")')
		P = list(pp)
	if P :
		print("Es su primo")
		print(P[0])
		return {"Respuesta" : P[0]} 
	else: 
		return{"Respuesta" : P} 

run(host='localhost',port=3000)