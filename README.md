# Projeto Comparando Algoritmos

##### Feito por:
*Victor Gustavo* | gustavo.victor@academico.ifpb.edu.br
*Leonardo Oliveira* | leonardo-oliveira.lo@academico.edu.ifpb.edu.br
##### Descrição:
O projeto consiste na apresentação e realização de um comparativo entre os algoritmos de ordenação mais comuns, explicando suas particularidades, vantagens e desvantagens; ao final desse processo será exibido um gráfico que exemplifica a performance dos algoritmos.

##### `Insertion Sort`
O `Insertion Sort` é um algoritmo bem simples que pode ser eficiente para listas pequenas, seu funcionamento consiste em realizar comparações entre os elementos até que o todo o vetor esteja ordenado. Para explicar o seu funcionamento iremos utilizar como exemplo um array com 10 índices.

`[30, 31, 44, 10, 9, 19, 11, 30, 35, 6]`

A maneira como o algoritmo funciona pode diferir dependendo de sua implementação, existem casos em que primeiro se busca o menor elemento da lista e existem casos que se utiliza o primeiro elemento da lista, independente da escolha a premissa do algoritmo ainda é a mesma. 

Utilizamos o índice `0` e comparamos com o elemento posterior, se o elemento atual for maior que o posterior suas posições são trocadas, se não, mantém o índice e prosseguimos para a próxima comparação.

**Em resumo:**
1º Passo: `[30, 31, 44, 10, 9, 19, 11, 30, 35, 6]`
*30 > 31? Não*

2º Passo: `[30, 31, 44, 10, 9, 19, 11, 30, 35, 6]`
*31 > 44? Não*

3º Passo: `[30, 31, 44, 10, 9, 19, 11, 30, 35, 6]`
*44 > 10? Sim, realiza a troca e iremos comparar com os elementos anteriores.*
`[30, 31, 10, 44, 9, 19, 11, 30, 35, 6]`
*31 > 10? Sim*
`[30, 10, 31, 44, 9, 19, 11, 30, 35, 6]`
*30 > 10? Sim*
`[10, 30, 31, 44, 9, 19, 11, 30, 35, 6]`

Nesse momento o `10` é o nosso menor elemento e está ocupando o lugar correto, agora continuamos as comparações.
*44 > 9? Sim, o 3º passo será repetido*

E assim o algoritmo segue até que todo vetor esteja ordenado corretamente; a forma como o vetor é organizado se assemelha a maneira que organizamos um conjunto de cartas de um baralho.

**Complexidade:**

Tempo:
- *Melhor Caso:* $O(n)$
- *Médio e Pior Caso:* $O(n²)$

Com isso em mente podemos perceber que apesar de ser um algoritmo relativamente eficiente para listas pequenas, a situação muda completamente quando aumentamos o tamanho da entrada, já que a complexidade de tempo dispara até chegar ao ponto que dependendo do tamanho da lista o uso de algoritmo se torna impraticável, quando temos um caso médio de $O(n²)$ significa que o tempo de execução aumenta ao quadrado do tamanho da entrada, por exemplo se o tamanho da entrada for 10, o tempo de execução será aproximadamente 100 unidades de tempo; se o tamanho da entrada é 100, o tempo de execução será aproximadamente 10.000 unidades de tempo e assim sucessivamente.

##### `Selection Sort`
O `Selection Sort` por sua vez ele trabalha de uma maneira um pouco diferente, utilizando uma variável que irá armazenar o índice do menor número encontrado no momento, com esse valor salvo podemos compará-lo com os valores subjacentes, se algum valor menor que o atual for encontrado a variável será atualizada até que chegue no final do vetor.

Vamos utilizar o mesmo vetor anteriormente usado.
`[30, 31, 44, 10, 9, 19, 11, 30, 35, 6]`

Iremos utilizar o primeiro elemento para realizar as comparações, o algoritmo se inicia e percorre a lista até que chegamos no `10`, nesse momento `10` é o nosso menor valor, em seguida o `9` até que por fim chegamos no número `6`, ao final dessa iteração o `6` estará no local correto.
`[6, 31, 44, 10, 9, 19, 11, 30, 35, 30]`

O processo se inicia novamente, dessa vez começando pelo `31`, em seguida encontramos o `9`, nenhum valor é menor que ele então trocamos suas posições.
`[6, 31, 44, 10, 9, 19, 11, 30, 35, 30]`

Trocamos o `31` pelo `9` e assim seguiremos até as iterações acabarem.
`[6, 9, 44, 10, 31, 19, 11, 30, 35, 30]`

 A premissa do `Selection Sort` é que a cada iteração, o algoritmo garante encontrar o menor número o posicioná-lo no devido local.

**Complexidade:**
A forma como o `Selection Sort` funciona faz com que em todos os casos a sua complexidade de tempo seja $O(n²)$ já que é necessário comparar todos os elementos $n$ vezes, o que em listas grandes faz o algoritmo se tornar ineficiente e extremamente demorado.

##### `Bubble Sort`
O `Bubble Sort` recebe esse nome pelo fato de atuar de forma parecida como bolhas, no caso do algoritmo ele empurra os números maiores para o fim da lista tal qual as bolhas sobem para a superfície. O algoritmo irá verificar se o número da esquerda é maior que o número da direita, se sim os números são trocados de lugar e o "contador" avança para o próximo elemento, quando chegar no final da lista uma outra iteração se inicia até que todo o vetor esteja organizado.

Utilizando o mesmo vetor de antes o algoritmo funciona assim:
*30 > 31? Não*
*31 > 44? Não*
*44 > 10? Sim, troca de posição e continua comparando o maior número com o próximo*
`[30, 31, 10, 44, 9, 19, 11, 30, 35, 6]`
*44 > 9? Sim, troca de novo* 
`[30, 31, 10, 9, 44, 19, 11, 30, 35, 6]`

Como sabemos que `44` é o maior número, todos os elementos serão trocados até que `44` fique na última posição; quando chegar no fim do vetor, o algoritmo repete o processo de buscar e "empurrar" o maior elemento até o fim da lista.

**Complexidade:**
- *Melhor Caso:* $O(n)$
É um caso bastante improvável que acontece quando a lista já está ordenada, como nenhuma troca é feita o algoritmo percorre a lista até o tamanho de $n$.

- *Médio e Pior Caso:* $O(n²)$
O algoritmo se mostra não tão eficiente pelo fato de ser necessário sempre está percorrendo a lista $n²$ vezes, assim como o `Insertion` e `Selection` o uso desse algoritmo é pensado apenas para listas pequenas.

##### `Quick Sort`
A partir desse momento encontramos algoritmos que são conhecidos por serem bastante eficientes na grande maioria dos casos, principalmente quando se tratam de vetores muito extensos, o `Quick Sort` trabalha de uma maneira peculiar, seguindo a filosofia de "dividir para conquistar" e além disso ele é um algoritmo recursivo.

Seu funcionamento consiste em escolher um número arbitrário para servir de pivô, essa escolha pode variar de acordo com a implementação e dependendo do número o algoritmo tende a ser mais performático. Após a escolha do pivô, é iniciado um processado chamado "particionamento" onde é feito uma "divisão" da lista, todos os números maiores que o pivô serão posicionados à direita enquanto os menores à esquerda.

Utilizando o mesmo vetor de exemplo:
`[30, 31, 44, 10, 9, 19, 11, 30, 35, 6]`

Feito o particionamento ele ficará assim:
`[10,9,19,11,6,30,44,31,35,30]`

Mesmo que pareça que o vetor esteja bagunçado, lembre-se que nesse momento o foco é garantir que todos os elementos estejam no devido lugar, seja à direita, seja à esquerda.

Após o processo de particionamento, agora utilizaremos a recursão para repetir o passos anteriores (escolher o pivô e particionar a lista), a recursão irá chamar o algoritmo `Quick Sort`nas sub-listas que foram geradas, dessa forma fica assim:

- Números menores que o pivô: `[9,6,10,19,11]`
- Números maiores que o pivô: `[44,31,35,30,30]`

E todo o processo se repete até que o vetor esteja ordenado

**Complexidade:**
- *Melhor e Médio Caso:* $O(n\ log(n))$
- *Pior Caso:* $O(n²)$

A notação denota que o algoritmo desempenha de maneira eficiente em listas muito grandes, enquanto a lista cresce de maneira linear a sua complexidade entretanto cresce de forma logarítmica, o que significa que a quantidade de dados que podemos trabalhar é superior ao tempo que seria gasto processando-os.

Um detalhe que vale a pena ser destacado é que `Quick Sort` rearranja os elementos dentro da própria lista o que descarta a necessidade de alocar espaço para criar sub-listas.

##### `Merge Sort`
Mais um algoritmo recursivo que também utiliza da abordagem "dividir para conquistar" temos o `Merge Sort`, o *merge* no nome não é atoa pois ao final da execução do algoritmo as sub-listas ordenadas serão mescladas, assim nos entregando um vetor ordenado.

Primeiro o algoritmo começa "dividindo" o vetor em sub-listas, feito isso outra divisão é realizada nessas sub-listas até que os elementos fiquem sozinhos e possam ser mesclados de maneira ordenada.

Iremos utilizar um vetor menor para fins de exemplificação: 
`[9, 3, 7, 1]`

Com o vetor em mãos dividimos ele uma vez:
`[9 , 3]` e `[7, 1]`

Dividimos mais uma vez:
`[9]`, `[3]`, `[7`] e `[1]`

Quando o processo de divisão terminar, inicia-se o processo de mesclagem dos índices, comparando o primeiro elemento com o subjacente, nesse caso `9` é maior que `3` e `7` é maior que `1`, trocamos suas respectivas posições e mesclamos em um novo vetor, após isso checamos novamente as posições dos índices e por fim teremos um vetor devidamente ordenado.

Para ficar mais fácil imaginar o processo, acompanhe o exemplo abaixo:
```
   [8, 3, 5, 4, 7, 6, 1, 2]  -> Dividir em sublistas
      /                 \
 [8, 3, 5, 4]        [7, 6, 1, 2]  -> Dividir novamente
  /       \           /       \
[8, 3]  [5, 4]     [7, 6]   [1, 2]  -> Dividir até sublistas de um único elemento
  \       /           \       /
  [3, 8]  [4, 5]     [6, 7]  [1, 2]  -> Mesclar sublistas ordenadamente
     \     /             \    /
    [3, 4, 5, 8]        [1, 2, 6, 7]  -> Mesclar novamente
         \                  /
         [1, 2, 3, 4, 5, 6, 7, 8]  -> Lista totalmente ordenada

```

**Complexidade:**
- *Melhor e Médio e Pior Caso:* $O(n\ log(n))$

Baseado nessas informações é seguro afirmar que para vetores extensos sem dúvidas o `Merge Sort` é uma boa opção, o fato de se manter constante até no pior dos casos certamente chama atenção, os motivos abordados no algoritmo anterior também são aplicados aqui, a quantidade de dados que podem ser trabalhos é maior do que o tempo que levaríamos para executar o algoritmo.

##### Gráficos:
Os testes foram realizados em duas máquinas distintas com as seguintes configurações:

Máquina 1:
- CPU: AMD Phenom X2 560 3.3Ghz
- GPU: Nvidia GT 740
- RAM: 14GB DDR3
- OS: Manjaro Linux
  
Máquina 2:
- CPU: Intel Core I5-9400F 2.9Ghz
- GPU: Nvidia GTX 1660
- RAM: 8GB DDR4
- OS: Windows 11

**Nota: O código em questão foi testado em duas máquinas diferentes e não foram utilizados meios para igualar os testes, os resultados apresentados podem diferir em outros cenários, portanto não devem ser utilizados para um resultado definitivo e devem ser encarados de maneira ilustrativa.**

Ao todo foram realizados dois testes em cada computador, utilizando 500 e 1000 elementos.

**Máquina 1 com 500 elementos.**
![[AMD500.png]]

**Máquina 1 com 1000 elementos.**
![[AMD1000.png]]

**Máquina 2 com 500 elementos.**
![[Intel500.png]]

**Máquina 2 com 1000 elementos.**
![[Intel1000.png]]

Comparando os gráficos fica evidente a diferença de performance entre os computadores, principalmente quando olhamos para o `Bubble Sort` que cresce mais no quesito tempo. Olhando novamente para o gráfico é possível perceber que na **Máquina 2** o crescimento é uma tangente suave, enquanto na **Máquina 1** algumas irregularidades pode ser percebidas e isso se dá por conta da grande carga que esse tipo de operação gera na CPU que, em alguns momentos chegou a ficar em 100% de uso.

No geral é notável que o `Quick Sort` e o `Merge Sort` foram os algoritmos que melhor desempenharam nesses testes, comprovando a sua eficiência na prática, enquanto o `Insertion Sort` e `Selection Sort` tiveram uma curva de crescimento perceptível mas não a ponto de torná-los inutilizáveis, a situação fica preocupante mesmo quando analisamos a curva de tempo do `Bubble Sort`, fica evidente que nesse tipo de situação mesmo com essa quantidade "generosa" de vetores, ainda assim o algoritmo demorou um certo tempo para ser executado.

O que podemos aprender com isso tudo é que a melhor coisa que devemos fazer é conhecer nossas ferramentas e qual é o momento ideal para usá-las, não é porquê o `Bubble Sort` teve o pior resultado que ele é completamente descartável, em uma lista menor por exemplo é possível que ele tenha um desempenho melhor que algoritmos muito mais complexos que ele em suas implementações. Entender quando e por quê utilizar certos algoritmos é o que diferencia de um programador de um amador, com esses conceitos em mente é possível escrever códigos mais eficientes, eficazes e escaláveis.

> *"Uma sólida base de conhecimento e técnica de algoritmos é uma característica que separa os programadores verdadeiramente qualificados dos novatos. Com a moderna tecnologia computacional, você pode executar algumas tarefas sem saber muito sobre algoritmos; porém, com uma boa base em algoritmos, é possível fazer muito, muito mais."*
> - Thomas Cormen
