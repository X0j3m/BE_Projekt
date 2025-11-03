{**
 * Global Footer - Widoczny dla wszystkich
 *}

<!-- 🎯 GLOBALNA STOPKA - DZIAŁA DLA WSZYSTKICH -->
<div class="global-footer" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 40px 0 20px; margin-top: 50px;">
  <div class="container">
    <div class="row">
      
      <!-- Sekcja 1: O nas -->
      <div class="col-md-4">
        <h4 style="color: #ffd700;">🌍 Nasza Firma</h4>
        <p>Jesteśmy liderem w branży e-commerce. Działamy globalnie od 2024 roku!</p>
        <div class="contact-info">
          <p>📞 <strong>+48 123 456 789</strong></p>
          <p>✉️ <strong>global@firma.pl</strong></p>
          <p>📍 <strong>Warszawa, Polska</strong></p>
        </div>
      </div>

      <!-- Sekcja 2: Linki -->
      <div class="col-md-4">
        <h4 style="color: #ffd700;">🔗 Przydatne linki</h4>
        <ul style="list-style: none; padding: 0;">
          <li style="margin-bottom: 8px;">
            <a href="{$urls.pages.contact}" style="color: #e0e0e0; text-decoration: none;">📞 Kontakt</a>
          </li>
          <li style="margin-bottom: 8px;">
            <a href="{$urls.pages.stores}" style="color: #e0e0e0; text-decoration: none;">🏪 Nasze sklepy</a>
          </li>
          <li style="margin-bottom: 8px;">
            <a href="{$urls.pages.sitemap}" style="color: #e0e0e0; text-decoration: none;">🗺️ Mapa strony</a>
          </li>
          <li style="margin-bottom: 8px;">
            <a href="{$urls.pages.prices-drop}" style="color: #e0e0e0; text-decoration: none;">🔥 Promocje</a>
          </li>
        </ul>
      </div>

      <!-- Sekcja 3: Social Media -->
      <div class="col-md-4">
        <h4 style="color: #ffd700;">👥 Social Media</h4>
        <div class="social-links">
          <a href="#" style="display: block; color: #e0e0e0; text-decoration: none; margin-bottom: 8px;">
            📘 Facebook
          </a>
          <a href="#" style="display: block; color: #e0e0e0; text-decoration: none; margin-bottom: 8px;">
            📷 Instagram
          </a>
          <a href="#" style="display: block; color: #e0e0e0; text-decoration: none; margin-bottom: 8px;">
            🐦 Twitter
          </a>
        </div>
        
        <!-- Newsletter -->
        <div style="margin-top: 20px;">
          <h5 style="color: #ffd700;">📧 Newsletter</h5>
          <p>Zapisz się do naszego newslettera!</p>
          <form>
            <input type="email" placeholder="Twój email" style="width: 100%; padding: 8px; border: none; border-radius: 4px;">
            <button type="submit" style="width: 100%; padding: 8px; background: #ff6b6b; color: white; border: none; border-radius: 4px; margin-top: 8px;">
              Zapisz się
            </button>
          </form>
        </div>
      </div>

    </div>

    <!-- Stopka copyright -->
    <div style="border-top: 2px solid rgba(255,255,255,0.3); margin-top: 30px; padding-top: 20px;">
      <div class="row">
        <div class="col-md-6">
          <p style="margin: 0; font-weight: bold;">
            &copy; <span style="color: #ffd700;">GLOBALNA FIRMA</span>
          </p>
          <small>Wszystkie prawa zastrzeżone</small>
        </div>
        <div class="col-md-6 text-right">
          <p style="margin: 0;">
            <strong>Płatności:</strong> 💳 🏦 📱
          </p>
          <small>Bezpieczne zakupy</small>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- Informacja dla developerów -->
<div style="background: #28a745; color: white; padding: 10px; text-align: center;">
  <small>🔄 STOPKA GLOBALNA - Edytuj plik: src/modules/ps_footer/ps_footer.tpl</small>
</div>