def is_palindrom(t):
    flag = True
    for j in range(0, len(t) // 2):
        if not t[j] == t[len(t) - 1 - j]: flag = False
    return flag


def palindrom(n,t):
    counter = 0
    dl_lan = n
    palindromy = []

    obecna = []
    #szukamy palindromu poziomo
    for i in range(0, n): #rzad
        dl_lan = n
        while dl_lan >= 5:
            for j in range(0, n-dl_lan+1): #poczatkowe indexy lancucha
                for k in range(j, dl_lan+j):    #kolumna
                    obecna.append(t[i][k])

                if is_palindrom(obecna):
                    palindromy.append(obecna)
                obecna = []

            dl_lan -= 1

    # szukamy palindromu pionowo
    for i in range(0, n): #kolumna
        dl_lan = n
        while dl_lan >= 5:
            for j in range(0, n - dl_lan + 1):
                for k in range(j, dl_lan + j):  #rzad
                    obecna.append(t[k][i])

                if is_palindrom(obecna):
                    palindromy.append(obecna)
                obecna = []

            dl_lan -= 1

    #po ukosie od lewej góry do prawego dolu
    dl_lan = n
    while dl_lan >= 5:
        for i in range(0, n-dl_lan+1): #rzad
            for j in range(0, n-dl_lan+1): #kolumna    (i,j) poczatkowy index lancucha
                itei,itej = i,j
                for k in range(dl_lan):
                    obecna.append(t[itei][itej])
                    itei,itej = itei+1, itej+1

                if is_palindrom(obecna):
                    palindromy.append(obecna)
                obecna = []
        dl_lan -= 1

    if len(palindromy) >= 2:
        palindromy = sorted(palindromy, key=len, reverse=True)
        # print(palindromy)
        for i in range(1, len(palindromy)):
            if palindromy[i] == palindromy[i-1]:
                print("".join(palindromy[i]))
                return


n = int(input())
inp = [[]] * n
for i in range(n):
    inp[i] = list(input())

palindrom(n, inp)