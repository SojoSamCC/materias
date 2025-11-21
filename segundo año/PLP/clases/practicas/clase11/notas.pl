unico([x], x).
unico([H | T], H) :- not(member(T, H)).
unico([H | T], X) :- unico(T, X).

sinRepetidos([]).
sinRepetidos([x]).
sinRepetidos([H | T]) :- unico(H, [H, T]), sinRepetidos(T). 