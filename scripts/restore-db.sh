#!/bin/bash

if [ -z "$1" ]; then
    echo "🎯 Użycie: ./scripts/restore-db.sh [plik.sql]"
    echo "   Dostępne backup:"
    ls -la db/*.sql
    exit 1
fi

BACKUP_FILE=$1

if [ ! -f "$BACKUP_FILE" ]; then
    echo "❌ Plik $BACKUP_FILE nie istnieje!"
    exit 1
fi

echo "🔄 Przywracanie bazy danych z $BACKUP_FILE..."

docker exec -i prestashop-db mysql -u root -proot prestashop < $BACKUP_FILE

if [ $? -eq 0 ]; then
    echo "✅ Baza przywrócona pomyślnie!"
else
    echo "❌ Błąd podczas przywracania bazy!"
    exit 1
fi