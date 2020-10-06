# CHAT ASD PYTHON
Esse programa foi feito para o estudo da Arquitetura de Sistemas Distribuídos do Curso de Ciências da Computação, para o estudo da interação entre servidores e máquinas.

Um serviço chat em **Python**, **Socket**, **Pickle**. Os usurios podem trocar mensagens e arquivos entre sí. Uma conexão direta é feita entres os usuários com os dados fornecidos pelo servidor, o servidor guarda um registro das sessão de chat.

----------------------------------
Informação dos Autores
----------------------------------
Nome: Angelo Soares Dorfey\
E-mail: usbangelo@sempreceub.com

Nome: Arthur Correa\
E-mail: arthur.pcorrea@sempreceub.com

Nome: Guilherme Santana\
E-mail: guilherme.santana@sempreceub.com

Nome: Matheus Muniz\
E-mail: matheus.emuniz.dev@gmail.com

---------------------------------
Descrição da Aplicação
---------------------------------
É um serviço de chat **peer-to-peer(par a par)** e serviço de compartilhamento de arquivos. Um ou mais usuários vão poder logar a um servidor central e assim poder trocarem mensagens e arquivos entre si diretamente.

O sistema do chat consiste de um servidor central que gerencia chats e os usuarios podem participar dos chats como usuários. Eles fazem a conexão com o servidor central através de uma endereço de conhecimento dos usuários com o **endereço de IP e a porta.**

Uma vez conectado o servidor pede a cada cliente seu nome de usuário, caso o nome de usuário ja esteja em uso, o mesmo será avisado a mudar de nome. Ao escolher om nome de usuário válido ele tem acesso a uma serie de opções:

1. MSG - Mensagem global
2. PRIVATE - Mensagem Privada (entre usuários específicos)
3. NICK - Trocar de nome de usuário
4. SNDFILE - Enviar arquivo
5. RECFILE - Receber arquivo
6. DISCNN - Disconectar do servidor

-----------------------------------------------------
Compilação e Execução do programa
-----------------------------------------------------
1. Faça download do projeto pelo arquivo `.zip` do repositorio ou com `git clone`:
```
...git clone https://github.com/matheus-emuniz/chat-asd-python
...cd chat-asd-python
```
2. Acesse a pasta clonada ou os arquivos extraidos da pagina nova;
3. Abra seu `terminal/bash` e execute o arquivo `server.py`;
4. Agora abra um novo `terminal/bash` e execute o arquivo `client.py`;
5. O servidor vai te perguntar seu nome de usuário (Caso seja um nome de usuário inválido terá de inserir um novo);
6. Você vai ser indicado a escolher uma série de opções printadas na tela (Msg pública/Msg privada/Mudar nick/Enviar arquivo/Receber arquivo);
7. O usuário ...
8. ...

-------------------------
Detalhes Tecnicos
--------------------------
1. O programa foi feito para enviar `.png`, `.jpg`, e `.txt`. Ele pode ser modificado para ter suporte a mais tipos de arquivos.
2. ...

git commit -m "Modificações no arquivo readme.md / Incremento de texto "