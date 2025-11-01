#!/bin/bash

TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="db/backup-${TIMESTAMP}.sql"

echo "💾 Tworzenie backupu bazy danych..."

docker exec prestashop-db mysqldump -u root -proot prestashop > $BACKUP_FILE

if [ $? -eq 0 ]; then
    echo "✅ Backup utworzony: $BACKUP_FILE"
    
    # Tworzymy też initial-data.sql jako główny backup
    cp $BACKUP_FILE db/initial-data.sql
    echo "✅ Zaktualizowano db/initial-data.sql"
else
    echo "❌ Błąd podczas tworzenia backupu!"
    exit 1
fi