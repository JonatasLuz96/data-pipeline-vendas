import requests
import json
import os
import logging
from datetime import datetime

# Configurações do logs
LOG_PATH = "logs/pipeline.log"
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(massage)s"
)

API_URL = "https://fakestoreapi.com/products"
RAW_PATH = "data-lake/raw"

def extract_data():
    logging.info("Iniciando extração de dados da API")

    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()

        os.makedirs(RAW_PATH, exist_ok=True)

        file_name = f"vendas_raw_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        file_path = os.path.join(RAW_PATH,file_name)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        logging.info(f"Extrações concluída com sucesso. Arquivo salvo em {file_path}")

        return file_path

    except requests.exceptions.RequestException as e:
        logging.error(f"Erro na extração de dados: {e}")
        raise

if __name__ == "__main__":
    extract_data()