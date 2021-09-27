---------------------------------------------------------
-- SLIDES
---------------------------------------------------------
-- Criação de Roles

CREATE ROLE administradores
	CREATEDB
	CREATEROLE
	INHERIT
	NOLOGIN
	REPLICATION
	BYPASSRLS
	CONNECTION LIMIT -1;
	
CREATE ROLE professores
	NOCREATEDB
	NOCREATEROLE
	INHERIT
	NOLOGIN
	NOBYPASSRLS
	CONNECTION LIMIT 10;

CREATE ROLE alunos
	NOCREATEDB
	NOCREATEROLE
	INHERIT
	NOLOGIN
	NOBYPASSRLS
	CONNECTION LIMIT 90;
	
CREATE ROLE daniel LOGIN CONNECTION LIMIT 1 PASSWORD '123' IN ROLE professores
-- A role daniel passa a assumir as permissões da role professores

CREATE ROLE daniel LOGIN CONNECTION LIMIT 1 PASSWORD '123' IN ROLE professores
-- A role professores passa a fazer parte da role daniel assumindo suas permissões

CREATE ROLE daniel LOGIN CONNECTION LIMIT 1 PASSWORD '123'

GRANT professores TO daniel
-- Associa as roles
	
REVOKE professores FROM daniel
-- Desassocia a role, daniel não é mais pertencente a role professores

DROP ROLE daniel
-- Apaga a role daniel

---------------------------------------------------------
-- Mão na Massa 
---------------------------------------------------------

--Cria ROLE professores
CREATE ROLE professores
	NOCREATEDB
	NOCREATEROLE
	INHERIT
	NOLOGIN
	NOBYPASSRLS
	CONNECTION LIMIT 10;

-- Altera a role professores e coloca uma senha	
ALTER ROLE professores PASSWORD '123';
	
-- Cria ROLE daniel com senha
CREATE ROLE daniel LOGIN PASSWORD '123';

-- Apaga role daniel
DROP ROLE daniel;

-- Cria Role daniel pertentencete a role professores
CREATE ROLE daniel LOGIN PASSWORD '123' IN ROLE professores;

-- Cria Role onde professores fazem parte do grupo daniel
CREATE ROLE daniel LOGIN PASSWORD '123' ROLE professores;

-- Concede todos privilegios para professores na tabela teste
GRANT ALL ON TABLE teste TO professores

-- Cria Role daniel Herda a role professores
CREATE ROLE daniel INHERIT LOGIN PASSWORD '123' IN ROLE professores;

-- Revoga as permissões de daniel da role de professores
REVOKE professores FROM daniel;
	
-- Verifica ROLES criadas	
SELECT * FROM pg_roles;

---------------------------------------------------------
CRETE TABLE teste (nome varchar);

