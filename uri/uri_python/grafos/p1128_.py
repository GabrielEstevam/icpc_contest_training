pre = []
low = []
stack = []
sc = []
N = 0 
k = 0 
cnt = 0

def GRAPHscTarjan (G):
   for i in range(N)
      pre.append(-1)
      low.append(-1)
      sc.append(-1)

   k = 0
   N = 0
   cnt = 0;
   for i in range(V): 
      if (pre[i] == -1)
         strongR( G, i, sc);
   
   pre.clear()
   low.clear()
   stack.clear()
   return k

def strongR(G, v, sc):
   pre[v] = cnt;
   cnt += 1
   mi = pre[v]; 
   stack[N] = v;
   N += 1
   
   for (link a = G->adj[v]; a != NULL; a = a->next) {
      vertex w = a->w;
      if (pre[w] == -1) {
         strongR( G, w, sc);
         if (low[w] < min) min = low[w]; /*A*/
      }
      else if (pre[w] < pre[v] && sc[w] == -1) {
         if (pre[w] < min) min = pre[w]; /*B*/
      }
   }
   low[v] = min;
   if (low[v] == pre[v]) {               /*C*/
      vertex u;
      do {
         u = stack[--N];
         sc[u] = k;
      } while (u != v);
      k++;
   }
