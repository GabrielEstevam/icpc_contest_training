def buscaProfundidade(G):
   N = len(G)
   cor = []
   floresta = []
   tempoInicial = []
   tempoFinal = []
   for i in range(N):
      cor.append(-1) #pinta de branco
      tempoInicial.append(0)
      tempoFinal.append(0)
   t = 0
   while True:    
      x = 0
      i = 0
      arvore = []
      while True:
         if G[x][i]:
            break
         i += 1
         if i == N:
            i = 0
            x += 1
            if x == N:
               break
      if x == N:
         break       
      pilha = []     
      pilha.append(x)
      cor[x] = 0 #pinta de azul
      tempoInicial[x] = t
      t += 1 
      while len(pilha) > 0:
         x = pilha[len(pilha) - 1]
         cor[x] = 0 #pinta de uma cor
         flag = True
         for i in range(N):
            if G[x][i]:
               if cor[i] == -1:
                  cor[i] = 0 #pinta de azul
                  pilha.append(i)
                  arvore.append([x, i]) # x é pai de i
                  tempoInicial[i] = t
                  t += 1                  
                  flag = False
                  break
         if flag:
            pilha.pop()
            tempoFinal[x] = t
            t +=1
      floresta.append(arvore)
      flagCor = True
      for i in cor:
         if i == -1:
            flagCor = False
            flagLinha = True
      if flagCor:
         break
   return [floresta, tempoInicial, tempoFinal]

# Main
entry = input().split(" ")
V = int(entry[0])
E = int(entry[1])
while V != 0:
   G = []
   Gs = [] # Grafo transposto
   for i in range(V):
      G.append([])
      Gs.append([])
      for j in range(V):
         G[i].append(0)
         Gs[i].append(0)
   for i in range(E):
      entry = input().split(' ')
      x = int(entry[0]) - 1
      y = int(entry[1]) - 1
      z = int(entry[2])
      G[x][y] = 1
      Gs[y][x] = 1
      if z == 2:
         G[y][x] = 1
         Gs[x][y] = 1
   r = buscaProfundidade(G)
   #print(r[0])
   #print(r[1])
   #print(r[2])

   # Encontra componentes conexas


   N = len(Gs)
   cor = []
   floresta = []
   tempoInicial = []
   tempoFinal = []
   for i in range(N):
      cor.append(-1) #pinta de branco
      tempoInicial.append(0)
      tempoFinal.append(0)
   t = 0
   while True:
      imaior = 0
      flag = True
      for i in range(len(r[2])):
         if cor[i] == -1:
            imaior = i
            flag = False
      if flag:
         break
      for i in range(len(r[2])):
         if r[2][i] > r[2][imaior] and cor[i] == -1:
            imaior = i
      x = imaior
      i = 0
      arvore = []       
      pilha = []     
      pilha.append(x)
      cor[x] = 0 #pinta de azul
      tempoInicial[x] = t
      t += 1 
      while len(pilha) > 0:
         x = pilha[len(pilha) - 1]
         cor[x] = 0 #pinta de uma cor
         flag = True
         for i in range(N):
            if Gs[x][i]:
               if cor[i] == -1:
                  cor[i] = 0 #pinta de azul
                  pilha.append(i)
                  arvore.append([x, i]) # x é pai de i
                  tempoInicial[i] = t
                  t += 1                  
                  flag = False
                  break
         if flag:
            pilha.pop()
            tempoFinal[x] = t
            t +=1
      floresta.append(arvore)
      flagCor = True
      for i in cor:
         if i == -1:
            flagCor = False
            flagLinha = True
      if flagCor:
         break
   #print(floresta)
   print(len(floresta), "componentes fortemente conexas")
   
   entry = input().split(" ")
   V = int(entry[0])
   E = int(entry[1])