
def ler_csv(emd):
    dados = []
    with open(emd, 'r') as arquivo:
        cabecalho = arquivo.readline().strip().split(',')
        for linha in arquivo:
            linha = linha.strip().split(',')
            linha_dict = {}
            for i in range(len(cabecalho)):
                linha_dict[cabecalho[i]] = linha[i]
            dados.append(linha_dict)
    return dados

dados = ler_csv("emd.csv")

def modalidades (dados):
    modalidade = set()
    for linha in dados:
        modalidade.add(linha['modalidade'])
    return sorted(modalidade)

def aptos(dados):
    nAtletas = len(dados)
    nAptos = 0
    for linha in dados:
        if linha['resultado'] == 'true':
            nAptos +=1
    perAptos = (nAptos / nAtletas)*100
    perInaptos = 100 - perAptos
    return perAptos, perInaptos

def escalao(dados):
    escaloes = {}
    for idade in range (20, 40, 5):
        idades = f"[{idade}-{idade+4}]"
        ateletas = [linha for linha in dados if int(linha['idade']) >= idade and int(linha['idade']) <= idade+4]
        escaloes[idades] = len(ateletas)
    return escaloes

print("Lista ordenada alfabeticamente das modalidades desportivas:")
modalidade = modalidades(dados)
for modalidade_sorted in modalidade:
    print(modalidade_sorted)

apto, inapto = aptos(dados)
print("\nPercentagens de atletas aptos e inaptos para a prática desportiva:")
print(f"Atletas aptos: {apto:.2f}%")
print(f"Atletas inaptos: {inapto:.2f}%")


print("\nDistribuição de atletas por escalão etário:")
escaloes = escalao(dados)
for idades, nAtletas in escaloes.items():
    print(f"{idades}: {nAtletas}")