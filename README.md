# AIprojects
Projects for AI discipline made in python.
  
  It has:
    
    A interactive menu to cycle through the projects (please dont be mean to the input read);
    
    Implementation of A* search algorithm;
    
    Implementation of BFS search algorithm;
    
    Implementation of D search algorithm;
    
    Implementation of Dijkstra's search algorithm;
    
    Sliding puzzle problem implementation
    
    The River Crossing problem's implementation
    
    Romenian map data (just for tests)
  
  To run it you will need:
    
    Python version 3.6.3 (the version used is for windows);
    
    Patience;
    
    To run it: 
      Open the console in the same directory as the Main.py;
      type python ./Main.py;
      
Here is the content(in portuguese) of the pdf that specificates what each project is:

Inteligência Artificial

Trabalho 1

Regras do trabalho:

• O trabalho é individual.

• E vetada a prática de plágio. 

• E permitida a utilização de materiais de apoio, desde que as fontes sejam informadas. 

• As implementações podem ser realizadas em qualquer linguagem de programação.

• As implementações devem ser entregues com código-fonte e arquivo explicando a utilização do
programa.

• As implementações devem ser suficientemente comentadas, de forma a propiciar um entendimento
adequado do funcionamento do código.

• O trabalho deve ser enviado por email para ****** até a aula do dia 26 de outubro.

I. (4,0 pts) Considere o seguinte cenário: “um fazendeiro está levando uma raposa, uma galinha e um saco
de grãos para casa. Para chegar lá, ele precisa atravessar um rio de barco. Só que ele pode levar consigo
apenas um item de cada vez. Se a raposa for deixada sozinha com a galinha, ela comerá a galinha. Se
a galinha for deixada sozinha com os grãos, ela comerá os grãos. Como o fazendeiro poderá atravessar
o rio mantendo todo seu suprimento intacto?”. Esta situação pode ser modelada como um problema de
busca. Pede-se:

1. Formule o problema especificando o estado inicial, as ações possíveis, o modelo de transição, o teste
de objetivo e o custo do caminho.
  
  Resposta:
  b = boatman;
  c = chicken;
  f = fox;
  g = grains;
  | = river;
  
  • Estado inicial: b,c,f,g|;
  
  • Ações possiveis: mover o barqueiro e algum outro elemento para o outro lado;
  
  • Modelo de transição: Resultado(Em(b,c,f,g|),Mover(b,c)) = (f,g|b,c);
  
  • Teste de objetivo: state==(|boatman,chicken,fox,grains)?true:false;
  
  • Custo do caminho: 1 unidade para cada movimento

2. Implemente um algoritmo de busca sem informação que resolva o problema, retornando como resposta
a sequência de ações necessárias para alcançar o estado objetivo a partir do estado inicial.

II. (2,0 pts) Leia o artigo “Is it an agent, or just a program?”, de S. Franklin e A. Graesser (1997), disponível
em http://robotics.cs.tamu.edu/dshell/cs631/papers/franklingraesser96agents.pdf, e faça uma
resenha do mesmo. O texto gerado deve ter uma lauda completa. A resenha será avaliada segundo os
seguintes critérios: conteúdo, clareza, organização e linguagem.

III. (4,0 pts) Considere o quebra-cabeça do bloco deslizante contendo 8 peças. Implemente
o algoritmo A∗ para resolvê-lo. O programa deve permitir a entrada dos estados inicial e
objetivo.

Special thanks to:
  Tutorials Point(https://www.tutorialspoint.com/python/)
  Stack Overflow(for all the already answered questions i had through learning python and implementing the projects)
  Mom and dad
