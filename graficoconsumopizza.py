import matplotlib.pyplot as plt

sabores = ["Mussarela", "Calabresa", "Portuguesa", "Calamusa", "Frango catupiry", "Marguerita"]
consumo = [20,15,2,8,50,2]

plt.pie(consumo,labels=sabores)
plt.show()