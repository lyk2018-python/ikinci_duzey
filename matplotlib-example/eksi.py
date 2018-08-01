import json
import os
import matplotlib
import random

from multiprocessing.pool import ThreadPool, Pool

from helpers import frekansla_beni_scotty, _indir

matplotlib.use('Qt5Agg')
matplotlib.rcParams['backend.qt5'] = 'PySide2'
import matplotlib.pyplot as plt  # noqa: E402

if os.path.exists("eksi.json"):

    with open("eksi.json", "r") as f:
        butun_entryler = json.load(f)
else:
    pool = ThreadPool(10)
    butun_entryler_ham = pool.map(_indir, range(1, 70))
    butun_entryler = []

    for l in butun_entryler_ham:
        butun_entryler.extend(l)

    with open("eksi.json", "w") as f:
        json.dump(butun_entryler, f, indent=4)

if os.path.exists("bayagi_eksi.json"):

    with open("bayagi_eksi.json", "r") as f:
        sorted_words = json.load(f)
else:

    pool = Pool(4)
    words_scores = {}

    sonuc = pool.starmap(frekansla_beni_scotty, zip(butun_entryler, [butun_entryler] * len(butun_entryler)))

    for s in sonuc:
        words_scores.update(s)

    sorted_words = sorted(words_scores.items(), key=lambda x: (x[1][1], x[1][0]), reverse=True)

    with open("bayagi_eksi.json", "w") as f:
        json.dump(sorted_words, f, indent=4)

top_post_size = 24
top_posts = sorted_words[:top_post_size]
last = sorted_words[top_post_size:]
top_posts_x = [tpl[1][0] for tpl in top_posts]
top_posts_y = [tpl[1][1] for tpl in top_posts]
last_x = [tpl[1][0] for tpl in last]
last_y = [tpl[1][1] for tpl in last]
figure, ax = plt.subplots()
ax.scatter(last_x, last_y, 0.1)
ax.scatter(top_posts_x, top_posts_y, 3, color="red")

random_values = [random.random() for i in top_posts]
random_values.sort()
for index, (label, (x, y)) in enumerate(top_posts):
    ax.annotate(
        label, xy=(x, y), xytext=(x + 0.5 + random_values[index], y + 0.5 + random_values[index]),
        arrowprops=dict(width=0.01, headwidth=0.05, facecolor='black', shrink=0.05),
        horizontalalignment='right', verticalalignment='top',
    )
plt.show()
