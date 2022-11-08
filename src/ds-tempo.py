import pandas as pd
import numpy as np
from tqdm import tqdm

alpha = 0.24

# Load data
df_test = pd.read_csv('data/test.csv')
y_test = df_test.iloc[:, 2:].values
ontologies_names = df_test.columns[2:].values

# Load ontology
ontology = generate_ontology('utils/go.obo', specific_space=True, name_specific_space='molecular_function')

# Load predictions
preds_diamond = np.load('predictions/diamond.npy')
preds_tempo = np.load('predictions/tempo.npy')

# Ensemble predictions
f_pred = []
for i, j in zip(preds_diamond, preds_transformers):
  if np.sum(i) != 0:
    f_pred.append(i * (1-alpha) + j * alpha)
  else:
    f_pred.append(j)
f_pred = np.array(f_pred)

# Evaluate
p, r = evaluate(f_pred, y_test)