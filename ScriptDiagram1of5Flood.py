import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection


def nested_circles(data, labels=None, ax=None, textkw={}):
    ax = ax or plt.gca()
    data = np.array(data)
    R = np.sqrt(data/data.max())
    p = [plt.Rectangle((0, 0), r, r) for r in R[::-1]]

    ax.add_collection(PatchCollection(p, facecolor=colors, edgecolor='none'))

    ax.axis("off")
    ax.set_aspect("equal")
    ax.autoscale()

    if labels is not None:
        kw = dict(color="black", va="center", ha="right")
        kw.update(textkw)
        ax.text(-0.05, R[0]-0.02, labels[0], **kw)
        for i in range(1, len(R)):
            y_offset = (R[i]-R[i-1])/2
            ax.text(-0.05, R[i]-y_offset, labels[i], **kw)

    return p


data = [2.0, 5.0, 36.2, 56.8, 100] # percentage values
labels = ["Natural Bare Soil (2.0%)", "Other (5.0%)", "Natural Terrestrial Vegetation (36.2%)", "Cultivated Terrestrial Vegetation (56.8%)", "Total Area (100%)"]
colors = ["lightgrey", "lightgreen", "darkgreen", "grey", "orange", "red"]
patches = nested_circles(data, labels, textkw=dict(fontsize=14))

plt.title("Affected Landcover Classes in a 1 of 5 Chance per Year Flood [%]", fontweight='bold')
plt.show()