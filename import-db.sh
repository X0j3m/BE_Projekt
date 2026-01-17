#!/bin/bash
set -x

# 1. Czekanie na serwer bazy danych
until mysqladmin ping -h"$DB_SERVER" --silent; do
    echo "Czekam na serwer $DB_SERVER..."
    sleep 2
done

# 2. Tworzenie bazy danych, jeśli nie istnieje
echo "Tworzę bazę danych (jeśli nie istnieje): $DB_NAME"
mysql -h"$DB_SERVER" -u"$DB_USER" -p"$DB_PASSWD" -e "CREATE DATABASE IF NOT EXISTS \`$DB_NAME\`;"

# 3. Sprawdzenie czy baza jest pusta
TABLE_COUNT=$(mysql -h"$DB_SERVER" -u"$DB_USER" -p"$DB_PASSWD" "$DB_NAME" -e "SELECT count(*) FROM information_schema.tables WHERE table_schema = '$DB_NAME';" -sN)

if [ "$TABLE_COUNT" -eq 0 ]; then
    echo "Baza pusta. Importowanie backupu..."
    mysql -h"$DB_SERVER" -u"$DB_USER" -p"$DB_PASSWD" "$DB_NAME" < /tmp/prestashop.sql
else
    echo "Baza zawiera już tabele ($TABLE_COUNT). Pomijam import."
fi

# 4. Uruchomienie oryginalnego startu PrestaShop
exec /tmp/docker_run.sh