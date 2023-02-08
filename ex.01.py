n1 = float(input('insira a primeira nota do aluno: '))
n2 = float(input('insira a segunda nota do aluno: '))
n3 = float(input('insira a terceira nota do aluno: '))

média = (n1 + n2 + n3)/ 3
print('A média entre {}, {} e {} é igual a {}'.format(n1, n2, n3, média))

MA = (n1 + n2*2 + n3*3 + média)/7.

if MA >= 9:
    print("Sua média final foi: ", MA, ". Parabéns, Você foi aprovado")
elif MA<= 8:
    print("Sua média final foi: ", MA, ".  Cuidado, Você está de DP")
elif MA < 4:
    print("Sua média final foi: ", MA, ". Infelizmente você está reprovado")
else:
    print("Sua média final foi: ", MA)