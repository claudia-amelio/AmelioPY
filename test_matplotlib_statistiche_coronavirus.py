import matplotlib.pyplot as plt

data = {'Napoli': 125706, 'Roma': 135785, 'Milano': 183220, 'Firenze': 35608}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
fig.suptitle('Le statistiche del coronavirus')


plt.show()
