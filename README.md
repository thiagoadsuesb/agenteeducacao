# 🎓 Agente Educação

## 📌 Visão Geral

O **Agente Educação** é uma plataforma educacional desenvolvida para gerenciamento, organização e análise de conteúdos acadêmicos, com foco em produtividade, confiabilidade e escalabilidade.

O projeto nasceu a partir de uma necessidade real durante a graduação em **Análise e Desenvolvimento de Sistemas (ADS)** na UESB, diante de problemas recorrentes no ambiente Moodle institucional, como indisponibilidade de acesso, falhas em submissões e inconsistência no controle de atividades.

Como solução, foi idealizado um sistema independente, com foco em:

* Centralização de materiais acadêmicos
* Controle de entregas com integridade (hash de arquivos)
* Alta disponibilidade via cloud
* Autonomia do estudante em relação a plataformas externas


## 🎯 Objetivos

* Garantir organização e persistência de conteúdos acadêmicos
* Implementar autenticação segura via OAuth2 (Google)
* Utilizar armazenamento em nuvem com alta disponibilidade
* Aplicar conceitos reais de **Engenharia de Software e DevOps**
* Servir como projeto acadêmico e portfólio profissional



## 🧠 Arquitetura do Sistema

O sistema segue o padrão arquitetural **MVT (Model-View-Template)** do Django, com evolução planejada para arquitetura em camadas:

```text
[Usuário]
   ↓
[Interface Web]
   ↓
[Views - Django]
   ↓
[Camada de Serviços (futuro)]
   ↓
[Models]
   ↓
[Banco de Dados]

[Upload de Arquivos]
   ↓
[Google Cloud Storage]
```


## ⚙️ Stack Tecnológica

### 🔹 Backend

* Python 3.13
* Django 6.0.4

### 🔹 Bibliotecas Principais

* django-allauth (OAuth2 / login social)
* django-storages (integração com cloud)
* google-cloud-storage (armazenamento GCS)
* google-auth (autenticação GCP)
* PyJWT (tokens e segurança)

### 🔹 Banco de Dados

* SQLite (ambiente de desenvolvimento)
* Planejado: PostgreSQL / Cloud SQL



## ☁️ Infraestrutura Cloud

O sistema utiliza serviços da Google Cloud Platform:

* Cloud Storage (bucket privado)
* IAM (controle de acesso)
* Service Accounts (autenticação segura)

Preparado para deploy em:

* Cloud Run
* App Engine



## 🧠 Integração com IA (Visão Estratégica)

Inspirado em ferramentas como o NotebookLM, o projeto prevê evolução para:


* Geração de insights baseados em documentos
* Organização inteligente de materiais
* Mapas mentais automatizados


## 🔐 Segurança

* Autenticação via OAuth2 (Google)
* Uso de variáveis de ambiente
* Credenciais fora do versionamento (.gitignore)
* Bucket sem acesso público
* Controle de acesso via IAM



## ⚙️ Ambiente de Desenvolvimento

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Acesso local:
http://127.0.0.1:8000/



## 🔑 Configuração do Cloud

```bash
set GOOGLE_APPLICATION_CREDENTIALS=credentials/gcloud.json
```


## 🧱 Estrutura do Projeto

```bash
painel/
├── core/
├── painel/
├── templates/
├── static/
├── credentials/   # ignorado no git
├── db.sqlite3
└── manage.py
```



## 🔄 Práticas DevOps Aplicadas

* Versionamento com Git (Conventional Commits)
* Controle de dependências
* Separação de ambientes (dev/prod)
* Uso de variáveis de ambiente
* Integração com serviços cloud (GCP)


## 🚀 Roadmap DevOps

* Containerização com Docker
* Orquestração com Kubernetes
* CI/CD com GitHub Actions
* Infraestrutura como código (Terraform)
* Monitoramento com Cloud Logging



## 🖥️ Infraestrutura e Virtualização

O projeto demonstra conhecimentos em:

* Containers (Docker)
* Orquestração (Kubernetes)
* Virtualização (VMware)
* Ambientes isolados e escaláveis



## 📊 Diferenciais

* Baseado em problema real acadêmico
* Integração com cloud real (GCP)
* Arquitetura escalável
* Preparado para IA
* Aplicação prática de DevOps



## 🚧 Status

Projeto em evolução contínua com foco em:

* Deploy em produção
* Integração completa com cloud
* Automação DevOps
* Interface moderna



## 👨‍💻 Autor

Thiago Prates
UESB - Análise e Desenvolvimento de Sistemas


## 📌 Licença

MIT
