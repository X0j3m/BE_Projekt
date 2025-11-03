#!/bin/bash

echo "=== 🛑 Sprawdzanie czy PrestaShop jest już zainstalowany ==="

if [ -f "src/prestashop-core/config/settings.inc.php" ]; then
    echo "❌ WYKRYTO INSTALACJĘ PRESTASHOP W REPOZYTORIUM!"
    echo "To oznacza, że .gitignore nie działa poprawnie."
    echo ""
    echo "Naprawa:"
    echo "1. Usuń pliki core z gita:"
    echo "   git rm -r --cached src/prestashop-core/"
    echo "2. Dodaj .gitignore:"
    echo "   git add .gitignore"
    echo "3. Commit:"
    echo "   git commit -m 'Remove accidentally committed core files'"
    echo "4. Push:"
    echo "   git push"
    exit 1
else
    echo "✅ OK: Brak instalacji PrestaShop w repozytorium"
fi