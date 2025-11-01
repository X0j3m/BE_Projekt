{**
 * Footer template for PrestaShop
 *}
 
<!-- 🎉 TEST: DOCKER VOLUMES DZIAŁAJĄ -->
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 25px; text-align: center; margin-top: 40px;">
  <h3>✅ SUKCES! Stopka Edytowana Lokalnie</h3>
  <p><strong>Docker Volumes synchronizują pliki pomiędzy Twoim komputerem a kontenerem</strong></p>
  <p>Data testu: </strong></p>
</div>

<!-- Oryginalna struktura PrestaShop -->
<div class="container">
  <div class="row">
    {block name='hook_footer_before'}
      {hook h='displayFooterBefore'}
    {/block}
  </div>
</div>

<div class="footer-container">
  <div class="container">
    <div class="row">
    </div>
    
    <!-- Moja własna stopka -->
    <div class="row mt-4 pt-4 border-top">
      <div class="col-md-6">
        <h5>O naszym sklepie</h5>
        <p>Jesteśmy liderem w sprzedaży internetowej od 2024 roku. Zaufało nam już tysiące klientów!</p>
      </div>
      <div class="col-md-6 text-right">
        <h5>Kontakt</h5>
        <p>📞 +48 123 456 789<br>
           ✉️ kontakt@mojsklep.pl<br>
           📍 Warszawa, Polska</p>
      </div>
    </div>
    
    <!-- Stopka copyright -->
    <div class="row mt-3">
      <div class="col-md-12 text-center">
        <p class="mb-1"><strong>&copy; Mój Super Sklep PrestaShop</strong></p>
        <p class="text-muted"><small>Wszystkie prawa zastrzeżone | Powered by Docker & GitHub</small></p>
        <p style="color: #28a745; font-weight: bold;">🚀 EDYTOWANE LOKALNIE - DZIAŁA PERFEKCYJNIE!</p>
      </div>
    </div>

    <div class="row">
    </div>
  </div>
</div>