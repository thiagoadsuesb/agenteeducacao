# 🎓 Agente Educação

## 📌 Visão Geral

O **Agente Educação** é uma plataforma web educacional projetada para gerenciamento, armazenamento e análise de conteúdos acadêmicos, integrando autenticação moderna, computação em nuvem e práticas de engenharia de software.

O sistema foi desenvolvido com foco em **escalabilidade, segurança e organização de dados educacionais**, permitindo que usuários armazenem e acessem seus materiais de estudo de forma estruturada e eficiente.



## 🎯 Objetivos

* Centralizar conteúdos acadêmicos em ambiente seguro
* Facilitar o upload e organização de materiais educacionais
* Implementar autenticação robusta via provedores externos (OAuth2)
* Integrar armazenamento em nuvem com alta disponibilidade
* Aplicar boas práticas de desenvolvimento e versionamento



## 🧠 Arquitetura do Sistema

O projeto segue uma arquitetura baseada em camadas:

* **Apresentação (Frontend)**: Templates HTML (Django Templates)
* **Aplicação (Backend)**: Django (MVC adaptado)
* **Persistência**:

  * SQLite (desenvolvimento)
  * Google Cloud Storage (arquivos)
* **Autenticação**:

  * OAuth2 via Google (Django Allauth)



## 🏗️ Modelo Arquitetural (UML Simplificado)

```text
[Usuário]
   ↓
[Interface Web]
   ↓
[Views - Django]
   ↓
[Models]
   ↓
[Banco de Dados SQLite]

[Upload]
   ↓
[Google Cloud Storage]
```


## ⚙️ Stack Tecnológica

### 🔹 Linguagem e Framework

* Python 3.13
* Django 6.0.4

### 🔹 Bibliotecas Principais

* django-allauth 65.16.1 (autenticação social)
* django-storages 1.14.6 (integração com storage)
* google-cloud-storage 3.10.1 (armazenamento em nuvem)
* google-auth 2.49.2 (autenticação com Google Cloud)
* PyJWT 2.12.1 (tokens de autenticação)

### 🔹 Infraestrutura

* Google Cloud Platform (GCP)
* Cloud Storage (bucket privado)
* IAM (controle de acesso)

### 🔹 Ferramentas de Desenvolvimento

* Visual Studio Code
* Git / GitHub
* Ambiente virtual (venv)

---

## ☁️ Integração com Cloud

O sistema utiliza o **Google Cloud Storage** como backend de armazenamento de arquivos:

* Bucket privado (sem acesso público)
* Controle via IAM
* Autenticação por conta de serviço
* Upload seguro de arquivos



## 🔐 Segurança

* Autenticação baseada em OAuth2
* Credenciais protegidas por variáveis de ambiente
* Arquivos sensíveis não versionados (.gitignore)
* Bucket com acesso público desativado
* Controle de permissões via IAM



## ⚙️ Configuração do Ambiente

```bash
# criar ambiente virtual
python -m venv venv

# ativar ambiente (Windows)
venv\Scripts\activate

# instalar dependências
pip install -r requirements.txt

# aplicar migrações
python manage.py migrate

# executar servidor
python manage.py runserver
```

Acesso local:
http://127.0.0.1:8000/



## 🔑 Configuração do Google Cloud

```bash
set GOOGLE_APPLICATION_CREDENTIALS=caminho/para/credencial.json
```



## 🧱 Estrutura do Projeto

```bash
painel/
├── core/
│   ├── models.py
│   ├── views.py
│   └── migrations/
├── painel/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/
├── static/
├── credentials/ (não versionado)
├── db.sqlite3 (dev)
└── manage.py
```


## 🔄 Práticas de DevOps

* Versionamento com Git (Conventional Commits)
* Controle de dependências (requirements.txt)
* Separação de ambientes (dev/prod)
* Uso de variáveis de ambiente para segurança
* Integração com serviços cloud (GCP)



## 📊 Possibilidades de Expansão

* Deploy em Cloud Run / App Engine
* Banco de dados gerenciado (Cloud SQL)
* Interface SPA (React ou Vue)
* Integração com IA para análise de documentos
* Dashboard analítico para desempenho acadêmico


## 🚧 Status do Projeto

Em desenvolvimento contínuo, com foco em evolução para arquitetura escalável e deploy em produção.


## 👨‍💻 Autor

Thiago Prates
Universidade Estadual do Sudoeste da Bahia (UESB)


## 📌 Licença

MIT License
