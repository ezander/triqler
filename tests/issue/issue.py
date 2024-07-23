import numpy as np
from triqler import qvality
from data import scores, targets

qvalues_from_scores = qvality.getQvaluesFromScores
_, peps = qvalues_from_scores(
    scores[targets],
    scores[~targets],
    includeDecoys=True,
    includePEPs=True,
    tdcInput=True,
)
print(np.all(peps>=1.0))

try:
    import matplotlib.pyplot as plt
    plt.plot(scores, peps)
    plt.show()
except:
    pass
