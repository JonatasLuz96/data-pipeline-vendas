import pandas as pd
import os
import logging
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Carrega variáveis do ambiente
load_dotenv()

# Configuração de logs
LOG_PATH = "logs/pipeline.log"
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

PROCESSED_PATH = "data-lake/processed"

# Variáveis de ambiente
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DB_PASSWORD_ENCODED = quote_plus(DB_PASSWORD)

def get_latest_processed_file():
    files = [f for f in os.listdir(PROCESSED_PATH) if f.endswith(".parquet")]
    if not files:
        raise FileNotFoundError("Nenhum arquivo PROCESSED encontrado")
    files.sort()
    return os.path.join(PROCESSED_PATH, files[-1])

def load_data():
    logging.info("Iniciando carga de dados no MySQL")

    file_path = get_latest_processed_file()
    df = pd.read_parquet(file_path)

    engine = create_engine(
        f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD_ENCODED}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"                                   
    )

    df.to_sql(
        name="vendas",
        con=engine,
        if_exists="append", # não apaga dados antigos
        index=False # não cria coluna lixo
    )

    logging.info(f"Carga concluída com sucesso. Registros inseridos: {len(df)}")

if __name__ == "__main__":
    load_data()