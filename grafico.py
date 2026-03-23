
import matplotlib.pyplot as plt
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho' ]
vendas = [200, 300, 240, 305, 360, 400]
plt.plot(meses, vendas)
plt.title('Vendas no primeiro semestre')
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.savefig("grafico_linhas.png")