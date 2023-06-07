# BrianCase

## Descrição
Este projeto é uma rede social que permite aos usuários se conectarem, compartilharem conteúdo, seguir outros usuários e interagir uns com os outros. O nome da rede social ainda não foi decidido, mas estamos trabalhando nisso!

## Funcionalidades
- Criação de perfil de usuário com informações pessoais, foto de perfil e biografia
- Compartilhamento de posts com texto, imagens e vídeos
- Feed de notícias personalizado com base nos usuários seguidos
- Possibilidade de seguir e ser seguido por outros usuários
- Interação com outros usuários através de comentários e curtidas em posts
- Pesquisa de usuários e posts por palavras-chave
- Notificações de novos seguidores, curtidas e comentários
- Sistema de mensagens privadas entre usuários

## Tecnologias utilizadas
  - Python

## Execução

### Criando ambiente virtual python para o servidor e instalando as bibliotecas
1. Abra a pasta Servidor no terminal linux e execute o comando 'make venv'
2. Execute o comando 'make install', para instalar todas as dependencias no ambiente virtual

## Execução do processo Servidor
1. Não esqueça de executar primeiramente o passo de criação do ambiente virtual
2. Abra a pasta Servidor no terminal linux e execute o comando 'make run'

### Criando ambiente virtual python para o cliente e instalando as bibliotecas
1. Abra a pasta Cliente no terminal linux e execute o comando 'make venv'
2. Execute o comando 'make install', para instalar todas as dependencias no ambiente virtual

### Execução do processo Cliente
1. Execute primeiro as instruções de execução do servidor
2. Não esqueça de executar primeiramente o passo de criação do ambiente virtual
3. Abra a pasta Cliente no terminal linux e execute o comando 'make run'