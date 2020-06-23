hermanos(A,B) :- A\==B,
	padres(A,X),
	padres(B,X).

tios(A,B) :-
	padres(B,X),
	hermanos(X,A),
	X\==B.
abuelos(PA,PB):- padres(PA,X),padres(X,PB).

bisabu(A,B) :- A\==B,
	padres(A,X),
	padres(X,Y),
	padres(Y,B).

tatarabuelo(A,B) :- A\==B,
	bisabu(A,X),
	padres(X,B).

tatararabuelo(A,B) :- A\==B,
	tatarabuelo(A,X),
	padres(X,B).

tioabu(A,B) :- A\==B,
	padres(A,X),
	tios(X,B).

tiobis(A,B) :- A\==B,
	bisabu(A,X),
	hermanos(X,B).

bisnie(A,B) :- A\==B,
	bisabu(B,A).

primos(A,B) :- A\==B,
	padres(A,X),
	padres(B,Y),
	hermanos(X,Y).

primosseg(A,B) :- A\==B,
	padres(A,X),
	padres(X,Y),
	hermanos(Y,Z),
	padres(W,Z),
	padres(B,W).

primoster(A,B) :- A\==B,
	bisabu(A,X),
	hermanos(X,Y),
	bisnie(Y,B).

sobrinos(A,B) :- A\==B,
	tios(B,A).

sobrinietos(A,B) :- A\==B,
	tioabu(B,A).

sobribis(A,B) :- A\==B,
	tiobis(B,A).

duossue(A,B) :- A\==B,
	padres(W,A),
	padres(W,V),
	V\==A,
	padres(V,X),
	padres(X,B).