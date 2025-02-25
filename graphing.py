import equations as e
import initial_numbers as c
import matplotlib.pyplot as plt
import numpy as np

#~~~~~~~~ GRAPHS ~~~~~~~~~~#

#time vs accIron, accEstrogen, hepcidin in storage

#time vs iron, prog, estrogen in reproductive

#total iron in blood over time (6 days)

#'''#hormone variation over menstrual cycle
fig, ax1 = plt.subplots()
color = 'purple'
ax1.set_xlabel('Time (day)')
ax1.set_ylabel('Estrogen (pg/L)', color=color)
ax1.plot(e.cycle, e.estgraph, color=color)
ax1.tick_params(axis='y', labelcolor='black')
ax2 = ax1.twinx()  
color = 'green'
ax2.set_ylabel('Progesterone (ng/mL)', color=color)  
ax2.plot(e.cycle, e.prog, color=color)
ax2.tick_params(axis='y', labelcolor='black')
fig.tight_layout()  
plt.xticks([1,4,8,12,16,20,24,28])
plt.axvspan(0, 6, facecolor='red', alpha=0.2)
plt.text(.1,14, "Menstruation");
plt.title('Hormone Variation Over Cycle')
#plt.show()

#blood loss over time during cycle
plt.plot(e.time, e.blossrate, "red", label='mL lost per day')
#plt.plot(e.time,e.totalblost, 'blue', label='total lost')
plt.title("Blood Loss Per Day Over Cycle")
plt.xlabel("Time (days)")
plt.ylabel("Blood Lost (mL)")
plt.fill_between(e.time, e.blossrate, alpha=0.3, color='red')
plt.text(5,10,'total blood lost = ')
plt.show()


