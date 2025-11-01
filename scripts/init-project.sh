#!/bin/bash

echo "=== 🚀 PrestaShop Developer Setup ==="

# Sprawdź czy Docker jest dostępny
if ! command -v docker &> /dev/null; then
    echo "❌ Docker nie jest zainstalowany!"
    exit 1
fi

# Cleanup
echo "🧹 Czyszczenie starych kontenerów..."
docker-compose down -v

# Tworzenie katalogów
echo "📁 Tworzenie struktury katalogów..."
mkdir -p src/themes src/modules src/override db docker/mysql docker/prestashop/config scripts

# Uruchamianie
echo "🐳 Uruchamianie kontenerów..."
docker-compose up -d

# Czekanie na bazę danych
echo "⏳ Oczekiwanie na uruchomienie bazy danych..."
sleep 20

echo "✅ Gotowe!"
echo ""
echo "🌐 Adresy:"
echo "   PrestaShop: http://localhost:8080"
echo "   Adminer (DB): http://localhost:8081"
echo ""
echo "📝 Następne kroki:"
echo "   1. Wejdź na http://localhost:8080"
echo "   2. Wykonaj ręczną instalację PrestaShop"
echo "   3. Użyj tych danych do bazy:"
echo "      - Serwer: db"
echo "      - Baza: prestashop"
echo "      - User: prestashop_user"
echo "      - Hasło: prestashop_pass"
echo "   4. Po instalacji uruchom: ./scripts/backup-db.sh"