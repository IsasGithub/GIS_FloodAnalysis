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


data = [0.2, 2.6, 2.8, 37.9, 56.5, 100] # percentage values
labels = ["Artificial Surface (0.2%)", "Natural Bare Soil (2.6%)", "Other (2.8%)", "Natural Terrestrial Vegetation (37.9%)", "Cultivated Terrestrial Vegetation (56.5%)", "Total Area (100%)"]
colors = ["lightgrey", "lightgreen", "darkgreen", "grey", "orange", "red"]
patches = nested_circles(data, labels, textkw=dict(fontsize=14))

plt.title("Affected Landcover Classes in the Flooded Area [%]", fontweight='bold')
plt.show()
