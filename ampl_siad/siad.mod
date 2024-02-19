
set L;
param D{L,L}; # Matrice de distances
var x{L,L} binary; # Choix du trajet


minimize DistanceTotal: sum{i in L, j in L: i != j} D[i,j] * x[i,j];

# Chaque lieu est visité exactement une fois

subject to UneVisite{i in L}: sum{j in L} x[i,j] = 1;
subject to UnDepart{j in L}: sum{i in L} x[i,j] = 1;


# Élimination des sous-tours
subject to PasBoucle{i in L, j in L}: x[i, j] + x[j, i] <= 1;  



