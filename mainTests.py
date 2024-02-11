import problem as prob
import solution as sol
import solver
import fastroute_problem as frp
import route_solution as rsol
import frp_rand_solver as frprs


print('Test des constructeurs des classes de base:')
my_prob = prob.Problem()
my_sol = sol.Solution()
my_solver = solver.Solver()

print('\nTest des constructeurs des classes spécialisées:')
my_frp = frp.FastRouteProb()
my_rsol = rsol.Route()

print('\nTest des fonctions d\'une solution:')
my_sol.evaluate()
my_sol.validate()

print('\nTest des fonctions d\'une route:')
my_rsol.evaluate()
my_rsol.validate()

print('\nTest du polymorphisme:')
for sol in (my_sol, my_rsol):
    sol.evaluate()
    sol.validate()

print('*** Tests FrpProblems ***')
print('L\'instance devrait s\'afficher:')
dist_matrix = [[0, 20, 30, 40],
[20, 0, 30, 5],
[30, 30, 0, 10],
[40, 5, 10, 0]]
frp_inst = frp.FastRouteProb(dist_matrix=dist_matrix)
print(str(frp_inst))


print('*** Tests Route ***')
print('La solution devrait s\'afficher:')
curr_rsol = rsol.Route(solvedProblem=frp_inst)
curr_rsol.visit_sequence = [0, 2, 3]
print(str(curr_rsol))

print('count_locations devrait donner 4:')
dist_matrix = [[0, 20, 30, 40],
[20, 0, 30, 5],
[30, 30, 0, 10],
[40, 5, 10, 0]]
frp_inst = frp.FastRouteProb(dist_matrix=dist_matrix)
print(frp_inst.count_locations())

print('n_locations devrait être égal à 4:')
curr_rsol = rsol.Route(solvedProblem=frp_inst)
n_locations = curr_rsol.problem.count_locations()
print(n_locations)

print('La séquence initiale devrait être invalide:')
print(curr_rsol.validate())
print('La séquence [0, 2, 3] devrait être invalide:')

curr_rsol.visit_sequence = [0, 2, 3]
print(curr_rsol.validate())

print('La séquence [1, 1, 1, 1] devrait être invalide:')
curr_rsol.visit_sequence = [1, 1, 1, 1]
print(curr_rsol.validate())
4
print('La séquence [0, 1, 2, 3] devrait être valide:')
curr_rsol.visit_sequence = [0, 1, 2, 3]
print(curr_rsol.validate())

print('La séquence [0, 2, 1, 3] devrait être valide:')
curr_rsol.visit_sequence = [0, 2, 1, 3]
print(curr_rsol.validate())

print('La valeur de la fonction objectif pour [0, 2, 3]',
' devrait être un grand nombre:')
curr_rsol.visit_sequence = [0, 2, 3]
print(curr_rsol.evaluate())
print('La valeur de la fonction objectif pour [0, 2, 1, 3] devrait être 65:')
curr_rsol.visit_sequence = [0, 2, 1, 3]
print(curr_rsol.evaluate())

print('*** Tests frp_rand_solver ***')
print('Retourne une solution sans afficher de sortie:')
frp_solver = frprs.FrpRandSolver()
frp_solver.max_time_sec = 3
frp_solver.verbose = 0
frp_sol = frp_solver.solve(frp_inst)
print('Solution retournée: ' + str(frp_sol))
print('Objectif: ' + str(frp_sol.evaluate()))