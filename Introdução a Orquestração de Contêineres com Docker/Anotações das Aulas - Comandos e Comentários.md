# Introdução a Orquestração de Contêineres com Docker



* ### Introdução ao Tema

  

> ###### Container image
Pacote com todas dependencias para criar o container/aplicacao

> ###### Dockerfile
É um arquivo de texto que contem todas instruções para fazer a build da imagem

> ###### Build
É a ação que cria uma imagem atraves do dockerfile 

> ###### Container
É uma instancia da imagem que representa a execução de uma aplicação/processo/servico

> ###### Volumes
Permite que o container armazene arquivos/dados em disco

> ###### Tag
Ajuda no versionamento das imagens

> ###### Multi-Stage Build
Contem multi estagios de Build, nele podemos usar uma imagem para compilar uma aplicacao
Exemplo uma imagem sem python chama outra imagem que contem python e na que nao tem executa

> ###### Repository
É uma coleção de imagens

> ###### Registry
É um serviço que prove acesso a um repositorio dockerhub

> ###### Dock Hub
É um repositorio publico e privado onde contem as imagens docker

> ###### Compose 
> É uma ferramenta de metadata que atraves de comandos voce pode criar multiplos containers






> * VM Docker Online
> https://labs.play-with-docker.com/

> ###### docker run --namge -meuprimeirocontainer -p 80:80 nginx
> Cria um container contendo a imagem nginx(Servidor Web) na porta 80

> ###### docker images
> Lista as imagens

> ###### docker ps
> Lista a imagens docker que estão rodando

> ###### docker rm nomecontainer
> Remover container

> ###### docker rm -f nomecontainer
> Remover container forçadamente

> ###### docker rmi imagem
> Remove a imagem do nginx



* ### Primeiros Passos com Docker

> ###### apt-get install docker.io
> Instala Docker no Uubuntu

> ###### run
> Cria o container

> ###### ps
> lista os containers

> ###### info
> Mostra informações do docker

> ###### images
> imagens utilizadas para criar os containers

> ###### exec
> para executar binarios no containers ou comandos especificos

> ###### stop/start

> ###### logs
> lista outputs

> ###### inspect
> lista configuracoes usadas no container

> ###### pull
> baixar imagens de repositorios

> ###### commit
> para commitar ações nos containers

> ###### tag
> para o versionamento 

> ###### login/logout
> para logar a um repositorio

> ###### push
> para apos a criação de uma imagem compartilhar 

> ###### search
> para procurar uma imagem

> ###### rm
> para remover container

> ###### rmi
> para remover imagem

> ###### export/import
> para exportar ou importar um container

> ###### save/load
> para salvar uma imagem de docker


* ### Rede do Docker

> ###### docker network ls
> Lista as redes docker

> ###### docker network create -d bridge nomerede
> Cria uma rede docker






* Material de apoio em:
https://github.com/luistkd4/docker101

