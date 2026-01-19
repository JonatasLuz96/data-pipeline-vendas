# Data Pipeline de Vendas

Projeto de pipeline de dados simulando um ambiente real de Engenharia de Dados Júnior.

## 📌 Objetivo
Finalizei um projeto pessoal onde desenvolvi um pipeline de dados completo, simulando um fluxo real de Engenharia de Dados, inspirado em arquiteturas usadas na AWS, mesmo rodando tudo localmente.

### 🔧 O que foi desenvolvido:

- Extração de dados (simulando uma fonte externa / API)

- Transformação e tratamento de dados com Pandas

- Estrutura de Data Lake (raw e processed) simulando Amazon S3

- Arquivos em Parquet, padrão muito usado em ambientes cloud

- Carga dos dados em MySQL usando SQLAlchemy

- Uso de variáveis de ambiente (.env) para segurança (padrão cloud)

- Logging para monitoramento do pipeline

- Projeto versionado no GitHub, seguindo boas práticas de produção

### 📚 O que aprendi com esse projeto:

- Como funciona um pipeline ETL do início ao fim

- Como estruturar um Data Lake pensando em cloud (mesmo localmente)

- Boas práticas de segurança e organização de código

- Como preparar um projeto para futura migração para AWS (S3, RDS)

- Diferença entre estudar ferramentas isoladas e aplicar tudo em um projeto real

💡 O foco foi reproduzir o dia a dia de um Engenheiro de Dados Júnior, usando as tecnologias mais comuns do mercado: Python, SQL e arquitetura cloud-oriented.

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

Crie o arquivo `.env ` baseado no `.env.example`

## Crie o banco no MySQL:

CREATE DATABASE pipeline_vendas;
<img width="1920" height="1080" alt="{D4867944-364A-47B8-B3D6-23F5972594DA}" src="https://github.com/user-attachments/assets/ad600d89-9ac9-49a8-bb09-0fd427e2c46c" />



## Execute o pipeline:

```bash
python src/extract.py
python src/transform.py
python src/load.py 
```

## 📊 Resultado

Os dados são carregados na tabela vendas no MySQL.

## 📌 Observações

Projeto desenvolvido com foco em simular atividades reais de um Engenheiro de Dados Júnior.
