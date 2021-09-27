# Conceitos e Melhores Práticas com Bancos de Dados PostgreSQL



* ### Introdução ao banco de dados PostgreSQL



* Postgree é modelo cliente/servidor. Cliente(interface grafica, terminal, aplicação)



> ###### postmaster 
> Processo principal do postgresql



> ###### childs
> São copias do postmaster que gerenciam as conexoes que entram e saem do postgresql



> ###### Processos de memoria
shared_buffesrs, wal_buffers, clog_buffers, lock space


* #### INSTALAÇÃO DO POSTGRESQL -- UBUNTU

> Site para download
> https://www.postgresql.org/download/linux/ubuntu/



> Cria a configuração do repositório de arquivos
>
> ###### sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'



> Importa as chaves de assinatura do repositório:
>
> ###### wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -



> Atualiza as listas de pacotes:
>
> ###### sudo apt-get update

> Instala a versão mais recente do PostgreSQL.
> Se você quiser uma versão específica, usar 'postgresql-12' ou similar em vez de 'postgresql'
>
> ###### sudo apt-get -y install postgresql



* #### pgAdmin
> https://www.pgadmin.org/download/pgadmin-4-apt/



> * Instalar o curl antes
> * Instalar a chave pública para o repositório
>
> ######  sudo curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add



> Cria o arquivo de configuração do repositório
>
> ###### sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'



> Instala nos modos desktop e web
>
> ###### sudo apt install pgadmin4



* senha inicial é: admin



> ###### pg_config --version
> Verifica a versão do postgres



> ###### pg_lsclusters
> Lista os clusters do postgresql



> ###### pg_createcluster -d /home/postgres/aula 13 aula --start
> Cria cluster



> ###### su - postgres
> Muda para o usuario postgres




* ### Objetos e Tipos de Dados no PostgreSQL



> ###### Cluster
> São coleções de bancos de dados que compartilham as mesma configurações



> ###### Banco de dados
> Conjunto de schemas com seus objetos e relações(tabelas,funções, views,etc)



> ###### Schema
> Conjunto de objetos e relações(tabelas,funções, views,etc)



> ###### vi /etc/postgresql/13/nomecluster/postgresql.conf
> abre o arquivo de configuração do postgresql no vi



> ###### pg_hba.conf
> Arquivo responsavel pelo controle de autenticação dos usuarios



> ###### pg_indet.conf
> Faz o mapeamento entre o usuario do sistema operacional com o do banco de dados



> ###### pg_createcluster versao nomecluster
> Cria um novo cluster



> ###### pg_dropcluster versao nomecluster
> Apaga um cluster



> ###### pg_ctlcluster versao nomecluster ação
> Executa uma ação no cluster (start,stop,status,restart)



* dump é um pseudo backup (pg_dump)




> ###### vi /etc/postgresql/13/nomecluster/postgresql.conf
> abre o arquivo de configuração do postgresql no vi



> ###### listen_addresses
> Neste parametro colocar o ip que deseja colocar 
> Não colocar "*" pois libera para qualquer ip acessar



> ###### para acessar via psql
> -h 127.0.0.1 -p 5432 -U postgres bancodedados



> ###### ALTER USER postgres PASSWORD '123';
> Altera a senha do usuario postgres



> ###### \q
> Sai do banco

