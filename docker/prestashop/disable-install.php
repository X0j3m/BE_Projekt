<?php
/**
 * Blokada instalacji PrestaShop
 * Plik zostanie skopiowany do /var/www/html/install/disable-install.php
 */

header('HTTP/1.1 403 Forbidden');
header('Content-Type: text/html; charset=utf-8');

?>
<!DOCTYPE html>
<html>
<head>
    <title>PrestaShop już zainstalowany</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            text-align: center;
            background: rgba(255,255,255,0.1);
            padding: 40px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 20px;
        }
        p {
            font-size: 1.2em;
            margin-bottom: 10px;
        }
        .steps {
            text-align: left;
            margin: 20px 0;
            padding: 20px;
            background: rgba(255,255,255,0.2);
            border-radius: 8px;
        }
        .btn {
            display: inline-block;
            padding: 12px 24px;
            background: #4ecdc4;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            margin: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 PrestaShop jest już skonfigurowany!</h1>
        <p>Ten sklep został już zainstalowany i skonfigurowany.</p>
        
        <div class="steps">
            <p><strong>Co teraz zrobić:</strong></p>
            <p>1. Przejdź do strony głównej sklepu</p>
            <p>2. Użyj danych dostępowych do panelu administracyjnego</p>
            <p>3. Skontaktuj się z administratorem jeśli potrzebujesz dostępu</p>
        </div>
        
        <a href="/" class="btn">🏪 Przejdź do sklepu</a>
        <a href="/admin123" class="btn">⚙️ Panel administracyjny</a>
        
        <p style="margin-top: 20px; font-size: 0.9em; opacity: 0.8;">
            Jeśli jesteś developerem, sprawdź instrukcję w repozytorium projektu.
        </p>
    </div>
</body>
</html>