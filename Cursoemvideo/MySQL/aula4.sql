/*contrains SQL  */
create database cadastro
default character set utf8 /* configurar para o padrao com acentuacao*/
default collate utf8_general_ci; 

create table pessoas(
   nome ,
   nascimento,
   sexo,
   peso,
   altura,
   nacionalidade
)DEFAULT CHARSET = utf8;