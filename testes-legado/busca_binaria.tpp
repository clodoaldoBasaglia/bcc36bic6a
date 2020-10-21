{
Clodoaldo A Basaglia da Fonseca
968692
}
inteiro: vetor[20]

inteiro busca_binaria(inteiro: numero, inteiro: inicio, inteiro: fim)
	inteiro: i
	i:= 20
	se (vetor[i]==numero) entao
		retorna i
	fim
	se (inicio==fim) entao
		{não encontrou}
	senão
		se(vetor[i] < numero) então
			busca_binaria(numero,inicio+1,fim)
		senão
			busca_binaria(numero,inicio,i-1)
		fim
	fim
fim


inteiro principal()
	inteiro: i
	i:=0
	repita 
		vetor[i] := i
		i := i + 1
	até i = 20
	leia(numero)
	escreva(busca_binaria(numero,0,20))
	retorna 0
fim