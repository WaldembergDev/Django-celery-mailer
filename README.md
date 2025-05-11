# django-celery-mailer

Este projeto é uma aplicação Django que permite o registro de usuários e o envio de e-mails personalizados com imagens geradas dinamicamente. Ele utiliza **Celery** para processamento assíncrono e **Pillow** para manipulação de imagens.

## Funcionalidades

- Registro de usuários com validação de dados.
- Envio de e-mails personalizados com conteúdo HTML.
- Geração dinâmica de imagens personalizadas com o nome do usuário.
- Embutimento de imagens no corpo do e-mail.
- Processamento assíncrono de tarefas com Celery e Redis.

## Tecnologias Utilizadas

- **Django**: Framework web para desenvolvimento rápido e seguro.
- **Celery**: Processamento assíncrono de tarefas.
- **Redis**: Broker para Celery.
- **Pillow**: Biblioteca para manipulação de imagens.
- **Python Decouple**: Gerenciamento de variáveis de ambiente.
- **Django-Celery-Results**: Armazenamento de resultados de tarefas no banco de dados.

## Requisitos

- Python 3.10+
- Redis
- Virtualenv (opcional)

