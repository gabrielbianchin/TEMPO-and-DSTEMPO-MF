import matplotlib.pyplot as plt
from tqdm import tqdm
from sklearn.metrics import precision_recall_curve, auc

def evaluate(predictions, ground_truth):
  precisions = []
  recalls = []
  f1s = []
  thresholds = []
  f1_max_value = -1
  f1_max_threshold = -1

  for i in tqdm(range(1, 101)):
    threshold = i/100
    p, r = 0, 0
    number_of_proteins = 0

    for idx_protein in range(len(predictions)):
      protein_pred = set()
      protein_gt = set()

      for idx_term in range(len(ontologies_names)):
        if ground_truth[idx_protein][idx_term] == 1:
          protein_gt.add(ontologies_names[idx_term])
          for parent in ontology[ontologies_names[idx_term]]['ancestors']:
            protein_gt.add(parent)

        if predictions[idx_protein][idx_term] >= threshold:
          protein_pred.add(ontologies_names[idx_term])
          for parent in ontology[ontologies_names[idx_term]]['ancestors']:
            protein_pred.add(parent)
      
      if len(protein_pred) > 0:
        number_of_proteins += 1
        p += len(protein_pred.intersection(protein_gt)) / len(protein_pred)
      r += len(protein_pred.intersection(protein_gt)) / len(protein_gt)
      

    if number_of_proteins > 0:
      threshold_p = p / number_of_proteins
    else:
      threshold_p = 0

    threshold_r = r / len(predictions)

    precisions.append(threshold_p)
    recalls.append(threshold_r)
    
    f1 = 0
    if threshold_p > 0 or threshold_r > 0:
      f1 = (2 * threshold_p * threshold_r) / (threshold_p + threshold_r)
    
    f1s.append(f1)
    thresholds.append(threshold)

    if f1 > f1_max_value:
      f1_max_value = f1
      f1_max_threshold = threshold

  print('F1 max:', f1_max_value)
  print('F1 threshold:', f1_max_threshold)

  plt.plot(thresholds, recalls, label = 'Recall')
  plt.plot(thresholds, precisions, label = 'Precision')
  plt.plot(thresholds, f1s, label = 'F1')
  plt.xlabel('Threshold')
  plt.ylabel('Metric')
  plt.title('Precision, Recall and F1 score')
  plt.xticks(np.arange(0,1.1,0.1))
  plt.yticks(np.arange(0,1.1,0.1))
  plt.legend(loc='best')
  plt.show()
  
  precisions = np.array(precisions)
  recalls = np.array(recalls)
  sorted_index = np.argsort(recalls)
  recalls = recalls[sorted_index]
  precisions = precisions[sorted_index]
  aupr = np.trapz(precisions, recalls)
  print('AUPR:', aupr)
  print(auc(recalls, precisions))

  fig, ax = plt.subplots()

  f_scores = np.linspace(0.2, 0.8, num=4)
  lines, labels = [], []
  for f_score in f_scores:
    x = np.linspace(0.01, 1)
    y = f_score * x / (2 * x - f_score)
    (l,) = ax.plot(x[y >= 0], y[y >= 0], color="gray", alpha=0.2)
    ax.annotate("f1={0:0.1f}".format(f_score), xy=(0.9, y[45] + 0.02))

  ax.plot(recalls, precisions, color='purple')

  #add axis labels to plot
  ax.set_title('Precision-Recall Curve')
  ax.set_ylabel('Precision')
  ax.set_xlabel('Recall')
  ax.set_xlim([0.0, 1.0])
  ax.set_ylim([0.0, 1.05])

  #display plot
  plt.show()

  return precisions, recalls