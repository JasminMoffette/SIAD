import amplpy
import os 
import pandas as pd
import numpy as np

class FrpAmplMipSolver:

    ampl_env = amplpy.Environment() # environnment ampl
    ampl = amplpy.AMPL(ampl_env) # traducteur ampl
    ampl.setOption('solver', 'gurobi') # choix solveur
    ampl.setOption('gurobi_options', 'timelim 600 outlev 1') # limite temps 10 min
    model_dir = os.path.normpath('./ampl_siad') # trouver le fichier ampl
    ampl.read(os.path.join(model_dir, 'siad.mod')) # lire le fichier.mod de ampl

    # instamciation du modele




