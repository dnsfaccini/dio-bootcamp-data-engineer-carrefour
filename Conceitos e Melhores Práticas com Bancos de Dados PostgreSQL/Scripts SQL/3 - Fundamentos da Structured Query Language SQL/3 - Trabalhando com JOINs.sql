SELECT numero, nome FROM banco;

SELECT banco_numero, numero, nome FROM agencia;

SELECT numero, nome FROM cliente;

SELECT banco_numero, agencia_numero, numero, digito, cliente_numero FROM conta_corrente;

SELECT id, nome FROM tipo_transacao;

SELECT banco_numero, agencia_numero, conta_corrente_numero, conta_corrente_digito, cliente_numero, valor FROM cliente_transacoes;

SELECT count(1) FROM banco; -- 151
SELECT count(1) FROM agencia; -- 296

---------------------------------------------------


-- INNER JOIN
SELECT
	banco.numero,
	banco.nome,
	agencia.numero,
	agencia.nome
FROM
	banco
JOIN
	agencia
ON
	agencia.banco_numero = banco.numero

	
-- Registros distintos
SELECT
	count(distinct(banco.numero))
FROM
	banco
JOIN
	agencia
ON
	agencia.banco_numero = banco.numero
	
-- LEFT JOIN
SELECT
	banco.numero,
	banco.nome,
	agencia.numero,
	agencia.nome
FROM
	banco
LEFT JOIN
	agencia
ON
	agencia.banco_numero = banco.numero


-- FULL JOIN
SELECT
	banco.numero,
	banco.nome,
	agencia.numero,
	agencia.nome
FROM
	banco
FULL JOIN
	agencia
ON
	agencia.banco_numero = banco.numero;



---------------------------------------------------

CREATE TABLE IF NOT EXISTS teste_a (id serial primary key, valor varchar(10));
CREATE TABLE IF NOT EXISTS teste_b (id serial primary key, valor varchar(10));

INSERT INTO teste_a (valor) VALUES ('Teste 1');
INSERT INTO teste_a (valor) VALUES ('Teste 2');
INSERT INTO teste_a (valor) VALUES ('Teste 3');
INSERT INTO teste_a (valor) VALUES ('Teste 4');

INSERT INTO teste_b (valor) VALUES ('Teste A');
INSERT INTO teste_b (valor) VALUES ('Teste B');
INSERT INTO teste_b (valor) VALUES ('Teste C');
INSERT INTO teste_b (valor) VALUES ('Teste D');

SELECT 
	tbla.valor, 
	tblb.valor
FROM 
	teste_a tbla
CROSS JOIN
	teste_b tblb

DROP TABLE IF EXISTS teste_a;
DROP TABLE IF EXISTS teste_b;

---------------------------------------------------

SELECT
	banco.nome,
	agencia.nome,
	conta_corrente.numero,
	conta_corrente.digito,
	cliente.nome
FROM
	banco
JOIN
	agencia
ON
	agencia.banco_numero = banco.numero
JOIN conta_corrente ON conta_corrente.banco_numero  = banco.numero
	AND conta_corrente.agencia_numero =agencia.numero
	AND conta_corrente.agencia_numero = agencia.numero
JOIN
	cliente
ON cliente.numero = conta_corrente.cliente_numero;