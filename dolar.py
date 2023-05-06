plt.style.use('cyberpunk')

dados_fechamento.plot(y= 'dolar', use_index = True, legend = False)

plt.title("Dolar")

plt.savefig('dolar.png', dpi = 300)

plt.show()