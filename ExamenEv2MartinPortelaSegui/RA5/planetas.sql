-- Active: 1765876824391@@localhost@3306
create DATABASE planetas;

create user planetas@'localhost' IDENTIFIED by 'planetas'

create user planetas@'%' IDENTIFIED by 'planetas'

grant all PRIVILEGES on planetas.* to planetas@'localhost'

grant all PRIVILEGES on planetas.* to planetas@'%'