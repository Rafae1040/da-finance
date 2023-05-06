plt.style.use('cyberpunk')

dados_fechamento.plot(y= 'ibovespa', use_index = True, legend = False)

plt.title("Ibovespa")

plt.savefig('ibovespa.png', dpi = 300)

plt.show()