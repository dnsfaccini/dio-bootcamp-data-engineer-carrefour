-- Consulta o Schema de um banco de dados, com nome de colunas, etc
SELECT * FROM information_schem.columns WHERE table_name ='banco'

SELECT numero, nome FROM banco;

SELECT banco_numero, numero, nome FROM agencia;

SELECT numero, nome, email nome FROM cliente;

SELECT banco_numero, agencia_numero, cliente_numero FROM cliente_transacoes;
-----------------------------------------------------------

- Faz a Média por valor 
SELECT AVG(valor) FROM cliente_transacoes;

- Conta numero
SELECT COUNT(numero) FROM cliente;

-- Conta emails do Gmail.com
SELECT 
	COUNT(numero), email
FROM 
	cliente 
WHERE 
	email ILIKE'%@gmail.com%'
GROUP BY 
	email;

- Obtem a maior transcao
SELECT 
	MAX(valor)
FROM
	cliente_transacoes;
	
- Obtem a menor transcao
SELECT 
	MIN(valor)
FROM
	cliente_transacoes;
	
-- Obtem maior transacao por tipo
SELECT 
	MAX(valor), tipo_transacao_id
FROM
	cliente_transacoes
GROUP BY
	tipo_transacao_id;
	
-- Obtem menor transacao por tipo
SELECT 
	MIN(valor), tipo_transacao_id
FROM
	cliente_transacoes
GROUP BY
	tipo_transacao_id;

-- Conta as trancoes por cliente	
SELECT 
	COUNT(id), tipo_transacao_id
FROM 
	cliente_transacoes
GROUP BY
	tipo_transacao_id;

-- Conta as trancoes por cliente porem que tiveram mais de 150 trancoes
SELECT 
	COUNT(id), tipo_transacao_id
FROM 
	cliente_transacoes
GROUP BY
	tipo_transacao_id
HAVING 
	COUNT(id) > 150;

-- Soma todos valores
SELECT 
	SUM(valor)
FROM
	cliente_transacoes;

-- Soma as trancoes por tipo id	e ordena
SELECT 
	SUM(valor), tipo_transacao_id
FROM
	cliente_transacoes
GROUP BY
	tipo_transacao_id
ORDER BY 
	tipo_transacao_id;