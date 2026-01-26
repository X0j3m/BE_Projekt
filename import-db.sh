#!/bin/bash
set -x

# 1. Czekanie na serwer bazy danych
until mysqladmin ping -h"$DB_SERVER" --silent; do
    echo "Czekam na serwer $DB_SERVER..."
    sleep 2
done

# 2. Resetowanie bazy danych (Usunięcie i utworzenie na nowo)
echo "Czyszczenie bazy danych: $DB_NAME"
# Usuwamy bazę, aby mieć pewność, że żadne stare tabele nie zostaną
mysql -h"$DB_SERVER" -u"$DB_USER" -p"$DB_PASSWD" -e "DROP DATABASE IF EXISTS \`$DB_NAME\`;"
echo "Tworzenie czystej bazy danych: $DB_NAME"
mysql -h"$DB_SERVER" -u"$DB_USER" -p"$DB_PASSWD" -e "CREATE DATABASE \`$DB_NAME\`;"

# 3. Import backupu (teraz robimy to zawsze)
echo "Importowanie świeżego backupu..."
mysql -h"$DB_SERVER" -u"$DB_USER" -p"$DB_PASSWD" "$DB_NAME" < /tmp/prestashop.sql

# 4. Aktualizacja portu SSL i domeny w bazie danych
echo "Aktualizuję konfigurację domeny na localhost:19793..."
mysql -h"$DB_SERVER" -u"$DB_USER" -p"$DB_PASSWD" "$DB_NAME" -e "UPDATE ps_shop_url SET domain='localhost:19793', domain_ssl='localhost:19793' WHERE id_shop=1;"

# Włączanie SSL w konfiguracji
mysql -h"$DB_SERVER" -u"$DB_USER" -p"$DB_PASSWD" "$DB_NAME" -e "UPDATE ps_configuration SET value='1' WHERE name IN ('PS_SSL_ENABLED', 'PS_SSL_ENABLED_EVERYWHERE');"

# 5. Uruchomienie oryginalnego startu
exec /tmp/docker_run.sh
