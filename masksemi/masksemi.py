import numpy as np
import random

def mask(true_labels, percentage):

    mask = np.ones((1,len(true_labels)),dtype=bool)[0]
    labels = true_labels.copy()
    
    for l, enc in zip(np.unique(true_labels),range(0,len(np.unique(true_labels)))):
        
        deck = np.argwhere(true_labels == l).flatten()        
        random.shuffle(deck)
        
        mask[deck[:int(percentage * len(true_labels[true_labels == l]))]] = False

        labels[labels == l] = enc

    labels[mask] = -1
    
    return np.array(labels).astype(int)
