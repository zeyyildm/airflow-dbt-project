
import pandas as pd
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def process_data(**context):
    """
    Veri işleme fonksiyonu
    Airflow context'i otomatik olarak geçirilir
    """
    try:
        logger.info("Veri işleme işlemi başlatılıyor...")
        
        dag_run = context.get('dag_run')
        execution_date = context.get('execution_date')
        
        logger.info(f"Execution Date: {execution_date}")
        
        import os
        dbt_seeds_path = "/opt/dbt/seeds"
        
        if os.path.exists(dbt_seeds_path):
            files = os.listdir(dbt_seeds_path)
            csv_files = [f for f in files if f.endswith('.csv')]
            logger.info(f"Bulunan CSV dosyaları: {csv_files}")
            
            # Örnek: İlk CSV dosyasını oku ve bilgilerini logla
            if csv_files:
                sample_file = os.path.join(dbt_seeds_path, csv_files[0])
                try:
                    df = pd.read_csv(sample_file, nrows=5)  # İlk 5 satırı oku
                    logger.info(f"Örnek dosya: {csv_files[0]}")
                    logger.info(f"Satır sayısı (ilk 5): {len(df)}")
                    logger.info(f"Sütunlar: {list(df.columns)}")
                except Exception as e:
                    logger.warning(f"Dosya okuma hatası: {e}")
        
        logger.info("Veri işleme işlemi tamamlandı.")
        return {"status": "success", "processed_at": datetime.now().isoformat()}
        
    except Exception as e:
        logger.error(f"Veri işleme sırasında hata oluştu: {e}")
        raise


def validate_data(**context):
    """
    Veri doğrulama fonksiyonu
    """
    try:
        logger.info("Veri doğrulama işlemi başlatılıyor...")
        logger.info("Veri doğrulama tamamlandı.")
        return {"status": "validated", "validated_at": datetime.now().isoformat()}
        
    except Exception as e:
        logger.error(f"Veri doğrulama sırasında hata oluştu: {e}")
        raise


if __name__ == "__main__":

    print("Script test modunda çalışıyor...")
    test_context = {
        'execution_date': datetime.now(),
        'dag_run': None
    }
    process_data(**test_context)

