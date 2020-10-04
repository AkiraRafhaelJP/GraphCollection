import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

#f(x)= e^x + 5x^2
y1 = np.exp(x) + 5 * x ** 2
plt.plot(x, y1, 'b-', label='f(x)=e^x + 5x^2')

#f(x)= x^3 + 2x^2+ 10x - 20
y2 = x ** 3 + 2 * x ** 2 + 10 * x - 20
plt.plot(x, y2, 'g--', label='f(x)= x^3 + 2x^2+ 10x - 20')

#f(x)= xe^-x + 1
y3 = x * np.exp(-x) + 1
plt.plot(x, y3, 'm:', label='f(x)= xe^-x + 1')

#additional feature
plt.legend()
plt.grid(True, linestyle='-')
plt.xlim([-10, 10])
plt.ylim([-10, 10])
plt.title('Grafik Tugas 1 MetNum')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

