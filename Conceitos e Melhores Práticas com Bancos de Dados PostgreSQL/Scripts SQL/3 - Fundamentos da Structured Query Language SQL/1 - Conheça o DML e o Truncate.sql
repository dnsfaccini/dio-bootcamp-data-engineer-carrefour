SELECT * from cliente_transacoes;

SELECT numero, nome, ativo FROM banco;

SELECT banco_numero, numero, nome FROM agencia;

SELECT numero, nome, email FROM cliente;

SELECT id, nome FROM tipo_transacao;

SELECT banco_numero, agencia_numero, numero, cliente_numero FROM conta_corrente;

SELECT banco_numero, agencia_numero, cliente_numero FROM cliente_transacoes;


--------------------------------------------------

CREATE TABLE IF NOT EXISTS teste (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(50) NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS teste;

CREATE TABLE IF NOT EXISTS teste (
	cpf VARCHAR(11) NOT NULL,
	nome VARCHAR(50) NOT NULL,
	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (cpf)
);

INSERT INTO teste (cpf,nome,created_at)
VALUES ('655456465','Zé Colméia', '2019-07-01 12:00:00');

INSERT INTO teste (cpf,nome,created_at)
VALUES ('655456465','Zé Colméia', '2019-07-01 12:00:00') ON CONFLICT(cpf) DO NOTHING;

UPDATE teste SET nome = 'Pedro Alvares' WHERE cpf = '655456465';