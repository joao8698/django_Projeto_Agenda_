Iniciar o projeto Django

python -m venv venv
. venv/Scripts/activate
pip install django
django-admin startproject project .
Configurar o git
python manage.py startapp 'nome do app'

# ============================= #

Configurando o Github

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT

# ============================= #

Migrando a base de dados do Django

python manage.py makemigrations
python manage.py migrate

# ============================= #

Criando e modificando a senha de um super usuário Django

python manage.py createsuperuser
python manage.py changepassword USERNAME