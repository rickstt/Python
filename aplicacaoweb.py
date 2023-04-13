import matplotlib.pyplot as plt
import mpld3

marcas = ["Nike", "Adidas", "Puma", "New Balance", "Gucci"]
vendas = [10,50,2,10,5]

plt.pie(vendas,labels=marcas)
mpld3.show()