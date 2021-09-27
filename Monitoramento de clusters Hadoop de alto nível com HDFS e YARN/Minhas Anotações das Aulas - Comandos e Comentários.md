# Monitoramento de clusters Hadoop de alto nível com HDFS e YARN



* ###  Teoria e Prática com HDFS



* Inicia os serviços

> ###### sudo service hadoop-hdfs-namenode start
> ###### sudo service hadoop-hdfs-secondarynamenode start
> ###### sudo service hadoop-hdfs-datanode start
> ###### sudo service hadoop-mapreduce-historyserver start
> ###### sudo service hadoop-yarn-resourcemanager start
> ###### sudo service hadoop-yarn-nodemanager start




> Copiar arquivo HDFS para local
>
> ###### hdfs dfs -get /tmp/file_teste.txt



> Coloca file_teste.txt no hdfs no diretorio /user/everis-bigdata
>
> ###### hdfs dfs -put file_teste.txt /user/everis-bigdata/



> Concede permissão 777 ao usuario hdfs na pasta /tmp
>
> ###### sudo -u hdfs hdfs dfs -chmod -R 777 /tmp



> Lista os diretorios do hdfs no barra /  (-h siginifica human readable)
>
> ###### hdfs dfs -ls -h /



> Le o arquivo file_teste.txt que esta no hdfs e le as primeiras 10 linhas
>
> ###### hdfs dfs -cat /tmp/file_teste.txt |head -10



> Remove o arquivo do hdfs
>
> ###### hdfs dfs -rm /tmp/file_teste.txt



> Cria um diretorio
>
> ###### hdfs dfs -mkdir /tmp/delete



> Copia arquivo para o diretorio /tmp/delete/
>
> ###### hdfs dfs -cp /tmp/file_teste.txt /tmp/delete/



> Cria um arquivo vazio
>
> ###### hdfs dfs -touchz /tmp/delete/empty_file



> Apaga o diretorio chamado delete
>
> ###### hdfs dfs -rm -R /tmp/delete



> Lista os usuarios
>
> ###### sudo -u hdfs hdfs dfs -du -h /user



> Lista informações importantes do hdfs como saude do cluster, replicacao, blocos 
>
> ###### sudo -u hdfs hdfs fsck /tmp/ -files -blocks



> Lista os comandos possiveis do fsck
>
> ###### hdfs fsck



> Exemplo de Job a ser executado
>
> ###### sudo -u hdfs yarn jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar wordcount /tmp/file_teste.txt/ /tmp/wc_output




* Observação
> hdfs - Nome do programa
> dfs - É o sub sistema
> Sair do modo seguro do hdfs
> sudo -u hdfs hdfs dfsadmin -safemode leave