import math
def calculaProbabilidade(EV1, EV2, AT, D, prob):
    #print('c', prob)
    if EV2 <= 0:
        #print('r:', prob)
        return prob
    else:
        prob_local = 0
        if EV1 > D:
            aux = prob * (6 - AT) / 6
            if aux > 0.0000001:
                prob_local += calculaProbabilidade(EV1 - D, EV2 + D, AT, D, aux)
        aux = prob * AT / 6
        if aux > 0.0000001:
            prob_local += calculaProbabilidade(EV1 + D, EV2 - D, AT, D, aux)
        #print('r:', prob)
        return prob_local

while True:
    entry = input().split(" ")
    EV1 = int(entry[0])
    EV2 = int(entry[1])
    AT = int(entry[2])
    D = int(entry[3])
    if EV1 + EV2 + AT + D == 0:
        break
    '''
    prob = calculaProbabilidade(EV1, EV2, AT, D, 1)
    prob = pow(AT/6, math.ceil(EV2/D))
    soma = prob
    print('p:', prob)
    for i in range(10):
        prob *= (6 - AT)/6 * AT/6
        print('p:', prob)
        soma += prob
    prob *= pow((6 - AT) / 6, math.ceil(EV1/D) - 1)
    prob *= pow(AT/6, math.ceil(EV2/D))
    '''

    prop = 0
    X = math.ceil(EV2/D)
    soma = pow(AT/6, X)
    #print('s:', soma)
    m = math.ceil(EV1/D) - 1
    k = X - 1
    if m > 0:
        k += 1
    aux = k
    print('k', k)
    for i in range(1, 10, 1):
        #soma += k * pow(AT/6, X + i) * pow((6 - AT)/6, i)
        k *= aux
        print('k', k)
        print('s:', soma)
    print('{0:.1f}'.format(soma * 100))