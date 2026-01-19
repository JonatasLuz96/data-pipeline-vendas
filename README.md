# Data Pipeline de Vendas

Projeto de pipeline de dados simulando um ambiente real de Engenharia de Dados Júnior.

## 📌 Objetivo
Extrair dados de vendas, processar e armazenar em um banco de dados MySQL utilizando boas práticas de Data Engineering.

## 🛠 Tecnologias
- Python
- Pandas
- SQL
- MySQL
- SQLAlchemy
- Parquet
- Logging
- dotenv

## 🧱 Arquitetura
Raw → Processed → Database

## ⚙️ Como executar

1. Clone o repositório
2. Crie o ambiente virtual
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt

Crie o arquivo .env baseado no .env.example

Crie o banco no MySQL:

CREATE DATABASE pipeline_vendas;


Execute o pipeline:

python src/extract.py
python src/transform.py
python src/load.py

📊 Resultado

Os dados são carregados na tabela vendas no MySQL.

📌 Observações

Projeto desenvolvido com foco em simular atividades reais de um Engenheiro de Dados Júnior.