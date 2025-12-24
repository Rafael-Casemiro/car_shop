# 🚗 Car Shop

**Car Shop** é uma plataforma web de marketplace automotivo desenvolvida com **Django**. O sistema permite que utilizadores se registem, anunciem os seus veículos para venda e comprem veículos de outros utilizadores, simulando um ambiente real de negociação com controle de inventário e histórico de transações.

---

## 📋 Funcionalidades

### 👤 Autenticação e Utilizadores
- **Login e Registo Personalizado:** Sistema de autenticação robusto utilizando um **User Model personalizado** (email como identificador principal).
- **Perfil do Utilizador:** Visualização de detalhes da conta e estatísticas básicas.
- **Segurança:** Proteção contra acesso não autorizado em rotas sensíveis (`@login_required`) e permissões de staff.

### 🚘 Marketplace (Loja)
- **Catálogo de Veículos:** Listagem de carros disponíveis com paginação e ordenação por data de criação.
- **Venda de Carros:** Utilizadores podem registar os seus próprios veículos com fotos, preço, placa, marca, modelo e ano.
- **Upload de Imagens:** Suporte para upload de fotos dos veículos, organizadas por ano e mês.
- **Filtro de Disponibilidade:** Veículos vendidos deixam automaticamente de aparecer no catálogo principal.

### 💰 Sistema de Compra
- **Transação Segura:** Lógica de backend que transfere a propriedade do veículo do vendedor para o comprador.
- **Regras de Negócio:**
  - O utilizador não pode comprar o próprio carro.
  - O utilizador não pode comprar um carro que já tenha sido vendido.
- **Feedback Visual:** Mensagens de sucesso ou erro (Toasts) para ações do utilizador.

### 📊 Painéis (Dashboards)
- **Minha Garagem:** Lista de carros que o utilizador comprou (histórico de aquisições).
- **Minhas Vendas:** Histórico de carros que o utilizador vendeu.
- **Detalhes do Carro:** Página exclusiva com informações técnicas, dados do vendedor e botão de compra.

---

## 🛠 Tecnologias Utilizadas

- **Backend:** Python 3, Django 6.0
- **Frontend:** HTML5, Tailwind CSS (via CDN)
- **Banco de Dados:** SQLite (Padrão de desenvolvimento)
- **Utilitários:** Faker (Para geração de dados de teste)

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python 3.10 ou superior instalado
* Git instalado

### Passo a Passo

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/rafael-casemiro/car_shop.git](https://github.com/Rafael-Casemiro/car_shop.git)
   cd car_shop

2. **Criar e ativar o ambiente virtual:**
   ```bash
   # Windows
    python -m venv venv
    .\venv\Scripts\activate
    
    # Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

3. *Instalar as dependências:**
   ```bash
   pip install django pillow faker
4. Realizar as migrações da base de dados:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
5. (Opcional) Popular a base de dados com utilizadores de teste: O projeto inclui um script para gerar 1000 utilizadores fictícios automaticamente.
   ```bash
   python utils/create_users.py
6. Criar um Admin Django:
   ```bash
   python manage.py createsuperuser
7. Rodar o servidor localmente:
   ```bash
   python manage.py runserver

# 📂 Estrutura do Projeto
O projeto está organizado em Aplicações (Apps) modulares:
- core/: Configurações principais do projeto (settings, urls, wsgi).

- user/: Gere a autenticação, modelos de utilizador, formulários de registo/login e visualização de perfis.

- car/: Gere a lógica de negócio dos veículos (CRUD, compra, venda, listagem).

- base_templates/: Templates globais (cabeçalho, rodapé, mensagens de alerta).

- utils/: Scripts auxiliares (ex: create_users.py).
