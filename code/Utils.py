import os

import numpy as np


def GetEvidence(eventID, model='A'):
    folder = 'results/event'+str(eventID)+'_'+model+'/'
    files = os.listdir(folder)
    evidence_file = [file for file in files if 'evidence.txt' in file][0]
    return np.loadtxt(folder+evidence_file)[0]
