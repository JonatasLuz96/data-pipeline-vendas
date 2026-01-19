import pandas as pd
import json
import os
import logging
from datetime import datetime

# Configuração de logs
LOG_PATH = "logs/pipeline.log"
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

RAW_PATH = "data-lake/raw"
PROCESSED_PATH = "data-lake/processed"

def get_latest_raw_file():
    files = [f for f in os.listdir(RAW_PATH) if f.endswith(".json")]
    if not files:
        raise FileNotFoundError("Nenhum arquivo RAW encontrado")
    files.sort()
    return os.path.join(RAW_PATH, files[-1])

def transform_data():
    logging.info("Iniciando trasnformação dos dados")

    raw_file = get_latest_raw_file()
    logging.info(f"Lendo arquivo RAW: {raw_file}")

    with open(raw_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    logging.info(f"Registros recebidos: {len(df)}")

    # Qualidade de dados
    if df.isnull().any().any():
        logging.warning("Dados nulos não encontrado")

    #Transformação
    df.columns = df.columns.str.lower()
    df["price"] = df["price"].astype(float)
    df["rating_rate"] = df["rating"].apply(lambda x: x["rate"])
    df["rating_count"] = df["rating"].apply(lambda x: x["count"])
    df.drop(columns=["rating"], inplace=True)

    df["processed-at"] = datetime.now()

    os.makedirs(PROCESSED_PATH, exist_ok=True)

    file_name = f"vendas_processed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.parquet"
    file_path = os.path.join(PROCESSED_PATH, file_name)

    df.to_parquet(file_path, index=False)

    logging.info("Transformação concluída. Arquivo salvo em {file_path}")

    return file_path

if __name__ == "__main__":
    transform_data()