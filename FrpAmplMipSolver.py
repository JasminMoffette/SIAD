import solver
import amplpy
import os
import fastroute_problem
import route_solution as rsol
import pandas as pd

class FrpAmplMipSolver(solver.Solver):

    def __init__(self):
        super(FrpAmplMipSolver, self).__init__()

    def solve(self, prob: fastroute_problem.FastRouteProb=None):
        #Générer l'environnement AMPL
        ampl_path = os.path.normpath('C:/Users/Darks/Desktop/ampl_mswin64')
        ampl_env = amplpy.Environment(ampl_path)
        ampl = amplpy.AMPL(ampl_env)
       
        #Gurobi
        ampl.setOption("solver", "gurobi")
        ampl.setOption('gurobi_options', 'timelim 600 outlev 0')
        #Lire le fichier .mod
        ampl.read(os.path.normpath('C:/Users/Darks/Desktop/equipe18_TPE/AMPL/tpe.mod'))

        
        #Générer une route par défaut
        route = rsol.Route(prob)
        

        #Générer les datas selon la matrice prob reçue en paramètre
        matrice = prob._dist_matrix
        indexi = [i for i in range(1, len(prob._dist_matrix)+1)]
        distance_df = pd.DataFrame(matrice,columns = indexi, index = indexi)
        #Assigner le CT dans le .data aux datas du problème
        ampl.set['I'] = indexi
        ampl.set['J'] = indexi
        ampl.get_parameter('distance').set_values(distance_df)
        ampl.get_parameter('chemins').set(len(prob._dist_matrix)-1)
       

        #Résoudre le problème
        ampl.solve()

        solution_ampl = ampl.getVariable('Y').get_values().to_list()
        
        #Récupérer la solution en Route
        valeurs_vrai = [triplet for triplet in solution_ampl if triplet[2] == 1]
        combinaison = [(x, y) for x, y, z in valeurs_vrai]
        tuple = 0
        for j in combinaison:
            if j[0] not in [i[1] for i in combinaison]:
                tuple = j
                break
      
        combinaison.remove(tuple)
        liste_tuple = [tuple]
        while len(liste_tuple) < len(prob._dist_matrix)-1 :
            for j in combinaison:

                if tuple[1] == j[0]:
                    liste_tuple.append(j)
                    tuple = j

        chemin_final = [liste_tuple[0][0]]
        for i in liste_tuple:
            chemin_final.append(i[1])
        
        #fermer l'engine
        ampl.close()
        
        route.visit_sequence = chemin_final
        return route



