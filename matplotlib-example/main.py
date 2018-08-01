import statistics

import matplotlib
import matplotlib.pyplot as plt
import requests

matplotlib.use('Qt5Agg')
matplotlib.rcParams['backend.qt5'] = 'PySide2'

# matplotlib.use('Cairo')

data = requests.get("http://127.0.0.1:5000/goc").json()[3:]

total_population = [d["Total population"] for d in data]

avg_pop = statistics.mean(total_population)

provinces = []
in_migration = []
out_migration = []
total_population = []
rate = []

for d in data:
    provinces.append(d["Province"])
    in_migration.append(d["In-migration"])
    out_migration.append(d["Out-migration"])
    total_population.append(d["Total population"])
    rate.append(d["Rate of net migration (‰)"])

figure, ax1 = plt.subplots()
ax2 = ax1.twinx()
p0 = ax1.plot(provinces, [avg_pop for i in provinces])
p1 = ax1.bar(provinces, in_migration)
p2 = ax1.bar(provinces, [p - in_migration[i] for i, p in enumerate(total_population)], bottom=in_migration)
p3 = ax1.bar(provinces, out_migration, bottom=total_population)
p4 = ax2.plot(provinces, rate)

plt.legend((p0[0], p1[0], p2[0], p3[0], p4[0]),
           ('Average Population', 'In Migration', 'Total Pop', 'Out Migration', 'rate'))
ax1.set_ylabel("Pop")
ax2.set_ylabel("‰")
plt.xticks(rotation=90)
plt.show()
