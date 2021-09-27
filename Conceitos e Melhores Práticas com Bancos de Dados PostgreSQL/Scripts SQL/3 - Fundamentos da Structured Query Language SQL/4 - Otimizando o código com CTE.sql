-------------------------------------------------------------
-- Mão na Massa
-------------------------------------------------------------

SELECT numero, nome FROM banco;
SELECT banco_numero, numero, nome FROM agencia

-- Exemplo CTE 1

WITH tbl_tmp_banco AS (
	SELECT
		numero, nome
	FROM
		banco
)
SELECT 
	numero, nome
FROM 
	tbl_tmp_banco
	
-- Exemplo CTE 2

WITH params AS (
	SELECT 
		213 as banco_numero
), tbl_tmp_banco AS ( 
	SELECT numero, nome
	FROM banco
	JOIN params ON params.banco_numero = banco.numero
)
SELECT numero, nome FROM tbl_tmp_banco


-- Exemplo CTE 3

WITH clientes_e_transacoes As (
	SELECT 
		cliente.nome as cliente_nome, 
		tipo_transacao.nome as tipo_transacao_nome,
		cliente_transacoes.valor as tipo_transacao_valor
	FROM cliente_transacoes
	JOIN cliente ON cliente.numero = cliente_transacoes.cliente_numero
	JOIN tipo_transacao ON tipo_transacao.id =  cliente_transacoes.tipo_transacao_id
	JOIN banco ON banco.numero = cliente_transacoes.banco_numero AND banco.nome ILIKE '%itaú%'
)
SELECT cliente_nome, tipo_transacao_nome, tipo_transacao_valor from clientes_e_transacoes;