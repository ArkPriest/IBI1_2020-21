
country=['USA','India','Brazil','Russia','UK']
Total_Cases=[29862124,11285561,11205972,4360823,4234924]
total=sum(Total_Cases)
frequency_dictionary={}
Total_Cases={'USA':2986124,'India':11285561,'Brazil':11205972,'Russia':4360823,'UK':4324924}
#combine the countyies with their cases and list them

import numpy as np
import matplotlib.pyplot as plt
#pie chart, where the slices will be ordered and plotted counter-clockwise:
labels='USA','India','Brazil','Russia','UK'
sizes=[29862124*100/total,11285561*100/total,11205972*100/total,4360823*100/total,4234924*100/total]
explode=(0.05,0,0,0,0)
#specfies the fraction of the radius with which to offset each wedge
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.title('Coronavirus_rates')
plt.axis('equal')
#equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
