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
        ampl_path = os.path.normpath('C:/Users/Darks/AMPL')
        ampl_env = amplpy.Environment(ampl_path)
        ampl = amplpy.AMPL(ampl_env)
       
        #Gurobi
        ampl.setOption("solver", "gurobi")
        ampl.setOption('gurobi_options', 'timelim 600 outlev 1')
        #Lire le fichier .mod
        ampl.read(os.path.normpath('C:/Users/Darks/Desktop/mqt-2100_2024h_TPE/Question 2/Q2.mod'))

        
        #Générer une route par défaut
        route = rsol.Route(prob)
        

        #Générer les datas selon la matrice prob reçue en paramètre
        matrice = prob._dist_matrix
        c = [i for i in range(1, len(prob._dist_matrix)+1)]
        ct_df = pd.DataFrame(matrice,columns = c, index = c)
        #Assigner le CT dans le .data aux datas du problème
        ampl.set['C'] = c
        ampl.get_parameter('CT').set_values(ct_df)
       

        #Résoudre le problème
        ampl.solve()

        solution_ampl = ampl.getVariable('z').get_values()
        print(solution_ampl)
        path = []
        recherche = 1
        done = True
        
        while done == True:
            for element in solution_ampl:

                if element[0] == recherche:
                    if element[2] == 1:
                        path.append(element[1])
                        recherche = element[1]

            if len(path) == len(c):
                done = False
        
        #fermer l'engine
        ampl.close()
        
        route.visit_sequence = path
        return route



