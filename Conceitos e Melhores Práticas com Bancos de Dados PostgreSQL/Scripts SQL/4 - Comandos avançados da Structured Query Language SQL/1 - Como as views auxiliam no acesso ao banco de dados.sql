SELECT numero, nome, ativo from banco

CREATE OR REPLACE VIEW vw_bancos AS (
	SELECT
		numero,
		nome,
		ativo
	FROM
		banco
);

SELECT numero, nome, ativo FROM vw_bancos;



CREATE OR REPLACE VIEW vw_bancos2 (banco_numero, banco_nome, banco_ativo) AS (
	SELECT
		numero,
		nome,
		ativo
	FROM
		banco
);

SELECT banco_numero, banco_nome, banco_ativo FROM vw_bancos2;


-- Inserção na view criada
INSERT INTO vw_bancos2 (banco_numero, banco_nome, banco_ativo)
VALUES (51, 'Banco Boa Ideia', TRUE)

SELECT banco_numero, banco_nome, banco_ativo FROM vw_bancos2 WHERE banco_numero = 51

-- Atualização na view criada
UPDATE vw_bancos2 SET banco_ativo = FALSE WHERE banco_numero = 51



-- Criar View Temporaria
CREATE OR REPLACE TEMPORARY VIEW vw_agencias AS (
	SELECT nome FROM agencia
);

SELECT nome FROM vw_agencias;



-- Cria view com WITH LOCAL CHECK OPTION, onde ela antes de inserir um valor checa se ja existe
CREATE OR REPLACE VIEW vw_bancos_ativos AS (
	SELECT numero, nome, ativo
	FROM banco
	WHERE ativo IS TRUE
)WITH LOCAL CHECK OPTION;

INSERT INTO vw_bancos_ativos (numero, nome, ativo)
VALUES (51, 'Banco Boa Ideia', FALSE)




CREATE OR REPLACE VIEW vw_bancos_com_a AS (
	SELECT numero, nome, ativo
	FROM vw_bancos_ativos
	WHERE nome ILIKE 'a%'
)WITH LOCAL CHECK OPTION;


INSERT INTO vw_bancos_com_a (numero, nome, ativo)
VALUES (333, 'Alfa', TRUE)

select numero, nome, ativo from vw_bancos_com_a

---------------------------------------------------------------------------
-- Criando uma View Recursiva
---------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS funcionarios (
	id SERIAL,
	nome VARCHAR(50),
	gerente INTEGER,
	PRIMARY KEY(id),
	FOREIGN KEY (gerente) REFERENCES funcionarios(id)
);

INSERT INTO funcionarios (nome, gerente) VALUES ('Anselmo', null);
INSERT INTO funcionarios (nome, gerente) VALUES ('Beatriz', 1);
INSERT INTO funcionarios (nome, gerente) VALUES ('Magno', 1);
INSERT INTO funcionarios (nome, gerente) VALUES ('Cremilda', 2);
INSERT INTO funcionarios (nome, gerente) VALUES ('Wagner', 4);

-- Retorna apenas o null, pois o gerente 999 não existe
SELECT id, nome, gerente FROM funcionarios where gerente IS NULL
UNION ALL
SELECT id, nome, gerente FROM funcionarios where gerente = 999;

-- Cria view recursiva 
CREATE OR REPLACE RECURSIVE VIEW AS vw_func(id, gerente, funcionario) AS (
	SELECT id, gerente, nome
	FROM funcionarios
	WHERE gerente IS NULL
	
	UNION ALL
	
	SELECT funcionarios.id, funcionarios.gerente, funcionarios.nome
	FROM funcionarios
	JOIN vw_func ON vw_func.id = funcionarios.gerente
);

SELECT id, gerente, funcionario FROM vw_func;
