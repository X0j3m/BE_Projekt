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
 * If you did not receive a copy of the license and are unable to
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
{**
 * Footer Pancernik Style
 *}
<div class="footer-container-pancernik">
    <div class="container">
        <div class="row">
            {* KOLUMNA 1: ZAMÓWIENIA *}
            <div class="col-md-3 col-sm-6 footer-column">
                <h3>Zamówienia</h3>
                <ul>
                    <li><a href="#" title="Status zamówienia">Status zamówienia</a></li>
                    <li><a href="#" title="Czas realizacji i dostawa">Czas realizacji i dostawa</a></li> {* Zmień ID CMS *}
                    <li><a href="#" title="Logowanie i rejestracja">Logowanie i rejestracja</a></li>
                    <li><a href="#" title="Metody płatności">Metody płatności</a></li> {* Zmień ID CMS *}
                    <li><a href="#" title="Zamówienia publiczne i B2B">Zamówienia publiczne i B2B</a></li>
                </ul>
            </div>

            {* KOLUMNA 2: OBSŁUGA KLIENTA *}
            <div class="col-md-3 col-sm-6 footer-column">
                <h3>Obsługa klienta</h3>
                <ul>
                    <li><a href="#" title="Zwroty i reklamacje">Zwroty i reklamacje</a></li>
                    <li><a href="#" title="Najczęściej zadawane pytania">Najczęściej zadawane pytania</a></li>
                    <li><a href="#" title="Uszkodzenie w transporcie">Uszkodzenie w transporcie</a></li>
                    <li><a href="#" title="Kody rabatowe & promocje">Kody rabatowe & promocje</a></li>
                    <li><a href="#" title="Zgłoś niebezpieczny produkt">Zgłoś niebezpieczny produkt</a></li>
                    <li><a href="#" title="Newsletter">Newsletter</a></li>
                    <li><a href="#" title="Opinie Trustmate">Opinie Trustmate</a></li>
                </ul>
            </div>

            {* KOLUMNA 3: O FIRMIE *}
            <div class="col-md-3 col-sm-6 footer-column">
                <h3>O firmie</h3>
                <ul>
                    <li><a href="#" title="Regulamin">Regulamin</a></li>
                    <li><a href="#" title="Ustawienia plików cookies">Ustawienia plików cookies</a></li>
                    <li><a href="#" title="Polityka prywatności">Polityka prywatności</a></li>
                    <li><a href="#" title="Kariera">Kariera</a></li>
                    <li><a href="#" title="Program partnerski">Program partnerski</a></li>
                    <li><a href="#" title="Ochrona środowiska">Ochrona środowiska</a></li>
                    <li><a href="#" title="Blog">Blog</a></li>
                    <li><a href="#" title="Sklep stacjonarny">Sklep stacjonarny</a></li>
                    <li><a href="#" title="Współpraca marketingowa">Współpraca marketingowa</a></li>
                    <li><a href="#" title="O Sklepie">O Sklepie</a></li>
                    <li><a href="#" title="Kontakt">Kontakt</a></li>
                </ul>
            </div>

            {* KOLUMNA 4: KONTAKT *}
            <div class="col-md-3 col-sm-6 footer-column contact-column">
                <h3>Kontakt</h3>
                <div class="contact-data">
                    <a href="tel:+48699577774" class="phone-number">
                        <i class="material-icons">phone</i> +48 699 577 774
                    </a>
                    <p class="working-hours">pon - pt: 8:00 - 17:30</p>
                    
                    <a href="{$urls.pages.contact}" class="contact-link"><i class="material-icons">email</i> Formularz kontaktowy</a>
                    <a href="mailto:sklep@pancernik.eu" class="contact-link"><i class="material-icons">alternate_email</i> sklep@pancernik.eu</a>
                    
                    <div class="address-data">
                        <i class="material-icons">place</i>
                        <span>
                            Lotnicza 35A<br>
                            63-400 Ostrów Wielkopolski
                        </span>
                    </div>
                </div>

                {* IKONY SOCIAL MEDIA *}
                <div class="social-icons">
                    <a href="#" target="_blank"><i class="material-icons">facebook</i></a>
                    <a href="#" target="_blank"><i class="material-icons">camera_alt</i></a> {* Instagram *}
                    <a href="#" target="_blank"><i class="material-icons">play_circle_filled</i></a> {* Youtube *}
                </div>

                {* NEWSLETTER *}
                <div class="footer-newsletter">
                    <p>Zapisz się do newslettera, by otrzymywać informacje o promocjach i nowościach</p>
                    <form action="{$urls.pages.index}#footer" method="post">
                        <div class="input-wrapper">
                            <input name="email" type="email" value="" placeholder="Wpisz swój adres email" required>
                            <button class="btn btn-primary" name="submitNewsletter" type="submit">
                                <i class="material-icons">email</i>
                            </button>
                        </div>
                        <p class="small-text">Informacje o przetwarzaniu danych osobowych znajdują się w pkt. 1 i 3 <a href="#">Polityki prywatności</a>.</p>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="line" style="border-top: 1px solid #5b5b5b;"></div>
<div class="bottom-footer" style="width: 100%; height: 60px; margin-top: 20px; padding-bottom: 20px;">
  <div style="float: left; width: 33%;"><img class="logo" src="{$urls.img_url}logopancernik.png" alt="{$shop.name}" style="max-height: 60px;"></div>
  <div style="float: left; width: 34%;"><p class="bottom-footer-text">Copyright 2025 Pancernik.eu. All rights reserved.</p></div>
  <div style="float: left; width: 33%; text-align:right;"><a href="https://pl.prestashop.com/" target="_blank" rel="noopener" title="Sklep internetowy prestashop"><img src="{$urls.img_url}prestashop.png" alt="PANCERNIK" class="bottom-footer-shoper" style="max-height: 55px;"></a></div>
</div>
