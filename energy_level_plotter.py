#for the plots
from pylab import *
#for ordered dicts
import collections
#list of all the materials and workfunctions
from full_materials_list_mod import full_materials_list

#colours for the plots, max number of plots currently limited to number of values in this list e.g. 11
colours = ['#d3d3d3', '#bdbdbd', '#a8a8a8', '#939393', '#7e7e7e', '#696969', '#545454', '#3f3f3f', '#2a2a2a', '#151515', '#000000']

#Make a dictionary of all the materials, doesn't really need to be an ordered one
all_materials = collections.OrderedDict(full_materials_list)

#Empty list for all the material to be plotted
list_materials = []

#Enter the name of the material to be plotted or type exit to end entering new materials
while True:
	item = str(raw_input('Next material name or exit:'))
	if item == 'exit':
		break
	#add each material to the list
	list_materials.append(item)


#make a new dictionary using the list of materials names to match the keys in the full dict
materials = collections.OrderedDict((k, all_materials[k]) for k in list_materials if k in all_materials)

#the max energy on the graph
maximum = 0
#the min enery on the graph rounded down from the lowest value in the materials selected
minimum = int(round((min(l[0] for l in materials.values())) - 1))

ticks =[]
tick_labels = []
fig, ax = plt.subplots()
i = 1
#Go through each material and plot HOMO LUMO or wf for each
for key, value in materials.iteritems():
	#Choose a new colour from the list for each
	colour = colours[i-1]
	lumo = max(value)
	homo = min(value)
	#if its a wf just plot one
	if homo == lumo:
		ax.broken_barh([(i-0.5,1)] , (homo, minimum-homo), facecolors=colour)
	#otherwise plot both HOMO and LUMO
	else:
		ax.broken_barh([(i-0.5,1)] , (homo, minimum-homo), facecolors=colour)
		ax.broken_barh([(i-0.5,1)] , (lumo, maximum-lumo), facecolors=colour)
	ticks.append(i)
	tick_labels.append(key)	
	i = i + 1

ax.set_title('Energy Level Diagram')
ax.set_xlim(0,i)
ax.set_ylim(minimum,0)
ax.set_ylabel('Energy Level (eV)')
ax.set_xticks(ticks)
ax.set_xticklabels(tick_labels)
ax.grid(True)

plt.show()
