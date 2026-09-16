<h1 align="center">Missão Aurora</h1>
<h2>📑 Sobre o projeto</h2>
  
<p>
  O projeto Missão Aurora basicamente é um simulador de decolagem de foguete.
</p>
<img width="400" alt="capa" src="https://github.com/user-attachments/assets/cdb3f7cf-9675-4a8c-8249-f685a9777a2b" />
<img width="400" alt="github 2" src="https://github.com/user-attachments/assets/55a83262-3b2b-4016-bfda-55648bd492f3" />
<img width="400" alt="github 3" src="https://github.com/user-attachments/assets/2522f372-559c-4285-aa85-ad96c7d6828a" />
<img width="400" alt="github 4" src="https://github.com/user-attachments/assets/da935833-42e5-4376-8593-69a97e66ae4c" />

<p>
  O simulador coleta as informações inseridas inicialmente pelo usuário, verificando se estão aptas para uma decolagem segura, caso contrário, a decolagem é abortada. Durante a decolagem, as variáveis sofrem alterações constantemente, sendo atualizadas a cada segundo. As principais variáveis que estão presentes no projeto são:
<p/> 
<ul>
  <li>Integridade estrutural</li>
  <li>Módulos críticos</li>
  <li>Combustível</li>
  <li>Energia</li>
  <li>Temperatura interna</li>
  <li>Temperatura externa</li>
  <li>Pressão dos tanques</li>
</ul> 
<p>
A variavel integridade estrutural sofre alteração quando algum módulo do foguete apresenta alguma falha. A variável combustível sofre um decréscimo de 1129 quilogramas por segundo durante o voo. A variável energia sofre um descréscimo de 0,5% por segundo durante o voo. A variável temperatura interna sofre um aumento da velocidade do foguete multiplicado por 0,003 a cada segundo durante o voo. A variável temperatura externa sofre um aumento da velocidade do foguete multiplicado por 0,1 a cada segundo durante o voo. A variável pressão dos tanques sofre um aumento de 0,3 bar por segundo durante o voo. Os módulos críticos sofrem falha de maneira aleatória a cada segundo durante o voo, sendo totalmente imprevisível.
</p>
<p>
  Durante a queda, caso o combustível acabe, a velocidade do foguete vai sofrendo uma força reversa da gravidade, sendo de 0,00981 quilômetros a cada segundo. O foguete começa a despencar quando a velocidade passa a ser negativa, sendo a partir daí subtraído a cada segundo da variável altitude o valor da velocidade. Durante este momento, a variável temperatura interna sofre uma adição a cade segundo do valor da velocidade multiplicado por 60 e por 0,001; a varivável temperatura externa sofre praticamente a mesma adição, só mudando que ao invés de ser 0,001 é 0,08.
</p>
<p>
  Caso o foguete despenque, atingindo o chão, ele acaba explodindo e parando a simulação. Caso alguma variável fique na cor vermelho escuro, houve um problema gravíssimo, onde sempre resultará uma explosão decorrente do comprometimento de algo relacionado ao foguete, exceto o combustível, onde de imediato ele não explode, apenas quando atingi o solo terrestre.
</p>
<p>
  A simulação é concluída com sucesso quando o foguete consegue chegar a uma altitude superior a 130000 quilômetros de distância do solo terrestre com os componentes intactos.
</p>

<h2>🛠️ Funcionalidades</h2>
<ul>
  <li>🚀 Simulação de decolagem de foguete</li>
  <li>📊 Monitoramento das variáveis durante a decolagem</li>
  <li>⛽ Consumo de combustível em tempo real</li>
  <li>⚡ Controle do nível de energia</li>
  <li>🌡️ Monitoramento da temperatura interna e externa</li>
  <li>💨 Monitoramento da pressão dos tanques</li>
  <li>🛡️ Verificação da integridade estrutural</li>
  <li>⚠️ Detecção de falhas nos módulos do foguete</li>
  <li>💥 Simulação de explosão em situações críticas</li>
  <li>📉 Simulação da queda do foguete em caso de falha</li>
  <li>🌍 Simulação da chegada ao espaço</li>
  <li>⏱️ Cronômetro durante a missão</li>
  <li>🛑 Possibilidade de interromper a simulação</li>
  <li>🔄 Reinicialização dos dados da missão</li>
</ul>
<h2>⚙️ Instruções de uso</h2>
<p>
  Caso o usuário queira rodar o código no próprio IDE é possível, só sendo necessário clonar o arquivos do repositório e executar o algoritmo.py, todavia, recomendamos fortemente para simplificar o processo, <a href="https://github.com/denis-bezerrax/simulador-foguete/releases/tag/simulador-foguete-1.3">baixar o executável</a> e inicia-lo no seu sistema operacional. Após inicializar o programa, insira as informações nos campos exigidos e clique no botão "Iniciar", instantaneamente irá começar a simulação. Caso queira parar a simulação, basta apertar o botão "Parar" do programa. Qualquer problema que resultar durante a simulação será mostrada na parte "Descrição" do programa.
</p>

<h2>👥 Autores</h2>

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/anapaula363">
        <img src="https://avatars.githubusercontent.com/u/265589133?v=4" width="115"><br>
        <sub>Ana Silva</sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/denis-bezerrax">
        <img src="https://avatars.githubusercontent.com/u/314802520?s=400&u=6073ed5be1b524436244bea5f53a388d07afee94&v=4" width="115"><br>
        <sub>Denis Bezerra</sub>
      </a>
    </td>
  </tr>
</table>
