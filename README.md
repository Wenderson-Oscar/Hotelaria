<h1> Hotelaria </h1>
🏫 (Atividade Acadêmica)

# Descrição do Projeto

Tem como funcionalidade  gerencia um 'Sistema' de Hotel que possa fazer reserva de quartos, usar serviços, desmarcar reserva, e listar clientes.

## Ferramentas usadas
🏦 Mysql

🐍 Python

🔨 Vscode

# 🛠️ Abrir e rodar o projeto


Primeiramente Teremos que Clonar o Repositorio
```
git clone https://github.com/Wenderson-Oscar/Hotelaria.git
```
Caso não tenha um ambiente virtual Criaremos um com o Comando a seguir
```
pip install virtualenv
```
Criando um ambiente virtual (**Linux**)

```
virtualenv env
```
Ativando o Ambiente Virtual
```
. env/bin/activate
```
Depois Teremos que baixar as devidas dependências
```
pip install -r requirements.txt
```
A seguir teremos que fazer a importação do banco **Fantasma**

obs: Na Pasta Hotelaria iremos aperta com o botão direito no mouse e entra na opção *abrir no terminal* ou caso tenha um conhecimento basico em comandos linux apenas navegue ate o diretorio dump 

Primeiramente teremos que entrar no terminal na pasta Hotelaria e executar o comando
```
cd dump
```
para podermos fazer a importação primeiro teremos que criar um banco com o nome hotel no mysql apos entra no seu mysql crie um banco de dados
```
CREATE DATABASE hotel;
```
depos execute o seguinte comando na pasta dump (terminal)
```
sudo mysql -u root hotel < hotel.sql
```
Caso tenha configurado uma senha no mysql, use
```
sudo mysql -u root -p hotel < hotel.sql
```