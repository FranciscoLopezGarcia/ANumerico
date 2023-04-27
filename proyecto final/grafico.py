import matplotlib.pyplot as plt
from front import main


resultao = main()

valor_x = [x for _, x, _ in resultao]
valor_y = [y for _, _, y in resultao]


plt.plot(valor_x, valor_y, marker='o', linestyle='-')


plt.xlabel('x')
plt.ylabel('y')
plt.title('Runge-Kutta Method')


plt.show()
