import statistics

import matplotlib
import requests

matplotlib.use('Qt5Agg')
matplotlib.rcParams['backend.qt5'] = 'PySide2'
import matplotlib.pyplot as plt  # noqa: E402

data = requests.get("http://127.0.0.1:5000/goc").json()[3:10]

total_population = [d["Total population"] for d in data]

avg_pop = statistics.mean(total_population)

provinces = []
provinces_idx = []
in_migration = []
out_migration = []
total_population = []
rate = []

for i, d in enumerate(data):
    provinces_idx.append(i)
    provinces.append(d["Province"])
    in_migration.append(d["In-migration"])
    out_migration.append(d["Out-migration"])
    total_population.append(d["Total population"])
    rate.append(d["Rate of net migration (‰)"])

figure, ax1 = plt.subplots()
ax2 = ax1.twinx()
p0 = ax1.plot(provinces_idx, [avg_pop for i in provinces], '--', color='lightgray')
p2 = ax1.bar(provinces_idx, total_population, 0.25)
p1 = ax1.bar([i + 0.3 for i in provinces_idx], in_migration, 0.25)
p3 = ax1.bar([i + 0.6 for i in provinces_idx], out_migration, 0.25)
p4 = ax2.plot(provinces_idx, rate)

plt.legend((p0[0], p1[0], p2[0], p3[0], p4[0]),
           ('Average Population', 'In Migration', 'Total Pop', 'Out Migration', 'rate'))
ax1.set_ylabel("Pop")
ax2.set_ylabel("‰")
ax1.set_xticks(provinces_idx)
ax1.set_xticklabels(provinces)
ax1.tick_params(labelrotation=90)
plt.show()
