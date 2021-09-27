SELECT numero, nome, ativo FROM banco ORDER BY numero;

UPDATE banco SET ativo = FALSE WHERE numero = 0;

BEGIN; -- Abre transação
UPDATE banco SET ativo = TRUE WHERE numero = 0;
SELECT numero, nome, ativo FROM banco WHERE numero = 0;
ROLLBACK; -- Desfaz transação


BEGIN; -- Abre transação
UPDATE banco SET ativo = TRUE WHERE numero = 0;
COMMIT; -- Confirma transação


-- Transação com SAVEPOINT
SELECT id, gerente, nome from funcionarios;
BEGIN;
UPDATE funcionarios SET gerente = 2 WHERE id = 3;
SAVEPOINT sf_func; -- Cria savepoint
UPDATE funcionarios SET gerente = NULL;
ROLLBACK TO sf_func; -- Desfaz ação do savepoint
UPDATE funcionarios SET gerente = 3 WHERE id = 5;
COMMIT;