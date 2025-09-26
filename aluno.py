# Função para validação das notas
def validar_prova(prova):
    while True:
        try:
            nota = float(input(f"Digite a nota da {prova}: "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida, digite um número de 0 a 10!")
        except ValueError:
            print("Valor inválido, digite um número!")

q = int(input("Informe a quantidade de alunos: "))
lista = []

#Armazena RMs cadastrados, para evitar duplicidade
rm_cadastrados = set()
 
for aluno in range(q):
    # Validação do nome
    while True:
        nome = input("Digite o nome do aluno: ")
        if all(c.isalpha() or c == " " for c in nome) and nome.strip():
            nome = ' '.join(nome.split())
            nome = nome.title()
            break
        else:
            print("Nome inválido, digite apenas letras!")

    # Validação do RM

    while True:
        rm = (input("Digite o RM do aluno: "))
        if not (rm.isdigit() and len(rm) == 6):
            print("Valor inválido, digite um RM que contenha valores númericos e 6 dígitos!")
        elif rm in rm_cadastrados:
            print("RM já cadastrado, digite outro RM!")
        else:
            rm_cadastrados.add(rm)
            break        

    # Validação das notas
    p1 = validar_prova("P1")
    p2 = validar_prova("P2")

    print()
    print("===Próximo aluno===")
    print()

    media = (p1 + p2) / 2
    lista.append([nome, rm, media])

for n in lista:
    print(f"\nAluno: {n[0]}\nRM: {n[1]}\nMédia: {n[2]:.1f}")