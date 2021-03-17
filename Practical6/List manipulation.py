
gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]

import numpy as np

gene_lengths=np.array([9410,394141,4442,105338,19149,76779,126550,36296,842,15981])
exon_counts=np.array([51,1142,42,216,25,650,32533,57,1,523])
gene_lengths/exon_counts

exon_lengths=gene_lengths/exon_counts
exon_lengths.sort()

print(exon_lengths)

import numpy as np
import matplotlib.pyplot as plt

n=100
score=exon_lengths
plt.boxplot(score,
            vert=False,
            whis=1.0,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False
              )
plt.show()