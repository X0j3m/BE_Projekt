#!/bin/bash

# Konfiguracja
CONTAINER_NAME="admin-mysql_db"
DB_USER="root"
DB_PASS="student"
DB_NAME="BE_197933"
BACKUP_DIR="backups"
OUTPUT_FILE="prestashop.sql"

# 1. Tworzenie folderu na backupy
mkdir -p $BACKUP_DIR

# 2. Archiwizacja starego pliku
echo "Archiwizacja starego pliku backupu..."
if [ -f "$OUTPUT_FILE" ]; then
    TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
    mv "$OUTPUT_FILE" "$BACKUP_DIR/prestashop_backup_$TIMESTAMP.sql"
    echo "✅ Poprzedni plik przeniesiono do: $BACKUP_DIR/prestashop_backup_$TIMESTAMP.sql"
fi

# 3. Tworzenie nowego zrzutu bazy danych
echo "Pobieranie bazy danych z kontenera..."

docker exec $CONTAINER_NAME mysqldump -u$DB_USER -p$DB_PASS --opt --no-tablespaces $DB_NAME > $OUTPUT_FILE

if [ $? -eq 0 ]; then
    echo "Sukces! Nowa baza zapisana jako $OUTPUT_FILE"
else
    echo "Błąd podczas eksportu bazy danych!"
fi
