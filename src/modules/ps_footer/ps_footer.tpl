{**
 * Copyright since 2007 PrestaShop SA and Contributors
 * PrestaShop is an International Registered Trademark & Property of PrestaShop SA
 *
 * NOTICE OF LICENSE
 *
 * This source file is subject to the Academic Free License 3.0 (AFL-3.0)
 * that is bundled with this package in the file LICENSE.md.
 * It is also available through the world-wide-web at this URL:
 * https://opensource.org/licenses/AFL-3.0
 * If you did not receive a copy of the license and unable to
 * obtain it through the world-wide-web, please send an email
 * to license@prestashop.com so we can send you a copy immediately.
 *
 * DISCLAIMER
 *
 * Do not edit or add to this file if you wish to upgrade PrestaShop to newer
 * versions in the future. If you wish to customize PrestaShop for your
 * needs please refer to https://devdocs.prestashop.com/ for more information.
 *
 * @author    PrestaShop SA and Contributors <contact@prestashop.com>
 * @copyright Since 2007 PrestaShop SA and Contributors
 * @license   https://opensource.org/licenses/AFL-3.0 Academic Free License 3.0 (AFL-3.0)
 *}

{* ===== TWOJA NOWA STOPKA ===== *}
<div style="background: #28a745; color: white; padding: 20px; text-align: center; margin-bottom: 20px;">
  <h3>✅ DZIAŁA! Docker Volumes</h3>
  <p>Edytujesz: src/modules/ps_footer/ps_footer.tpl</p>
  <p>Data: <strong></strong></p>
</div>

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
      
      <div class="col-md-4">
        <h5>O naszym sklepie</h5>
        <p>Jesteśmy najlepszym sklepem internetowym! Dostarczamy wysokiej jakości produkty od 2024 roku.</p>
        <p><strong>Telefon:</strong> +48 123 456 789</p>
        <p><strong>Email:</strong> kontakt@twojsklep.pl</p>
      </div>

      <div class="col-md-4">
        <h5>Szybkie linki</h5>
        <ul class="list-unstyled">
          <li><a href="{$urls.pages.contact}">Kontakt</a></li>
          <li><a href="{$urls.pages.stores}">Nasze sklepy</a></li>
          <li><a href="{$urls.pages.sitemap}">Mapa strony</a></li>
          <li><a href="{$urls.pages.prices-drop}">Promocje</a></li>
        </ul>
      </div>

      <div class="col-md-4">
        <h5>Social Media</h5>
        <div class="social-links">
          <a href="#" class="btn btn-outline-secondary btn-sm mb-2">Facebook</a>
          <a href="#" class="btn btn-outline-secondary btn-sm mb-2">Instagram</a>
          <a href="#" class="btn btn-outline-secondary btn-sm mb-2">Twitter</a>
        </div>
      </div>

    </div>

    <div class="row mt-4 pt-3 border-top">
      <div class="col-md-12 text-center">
        <p class="mb-0">
          <strong>&copy; Twój Sklep Internetowy</strong><br/>
          <small>Wszystkie prawa zastrzeżone | Stworzone z miłością przez nasz zespół</small>
        </p>
        <p class="text-muted mt-2">
          <small>To jest MOJA ZMIENIONA STOPKA! Działa!</small>
        </p>
      </div>
    </div>

  </div>
</div>
