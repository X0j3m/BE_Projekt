{**
 * Plik: themes/mytheme/templates/customer/authentication.tpl
 *}
{extends file='page.tpl'}

{block name='page_title'}
  {l s='Log in to your account' d='Shop.Theme.Customeraccount'}
{/block}

{block name='page_content'}
    
    <div class="social-login-section mb-4">
        <h3 class="h3" style="font-size: 16px; margin-bottom: 15px;">Zaloguj się przez konto społecznościowe</h3>
        <div class="social-buttons-wrapper">
             {* Tutaj wpinają się moduły FB/Google. Jeśli ich nie masz, to miejsce będzie puste *}
             {hook h='displayCustomerLoginFormAfter'}
        </div>
    </div>
    
    <hr style="margin: 30px 0; border-top: 1px solid #ddd;">

    <div class="row">
        <div class="col-md-6 col-xs-12 login-container">
            <h3 class="h3" style="font-size: 18px; margin-bottom: 15px; font-weight: bold;">Zaloguj się</h3>
            
            <div class="login-form-wrapper">
                 {* Wczytujemy plik z polami formularza (Krok 2) *}
                 {render file='customer/_partials/login-form.tpl' ui=$login_form}
            </div>
        </div>

        <div class="col-md-6 col-xs-12 register-container">
            <h3 class="h3" style="font-size: 18px; margin-bottom: 15px; font-weight: bold;">Zarejestruj się</h3>
            
            <div class="register-benefits">
                <p class="mb-2">Otrzymasz liczne dodatkowe korzyści:</p>
                <ul class="benefits-list">
                    <li>podgląd statusu realizacji zamówień</li>
                    <li>podgląd historii zakupów</li>
                    <li>brak konieczności wprowadzania swoich danych przy kolejnych zakupach</li>
                    <li>możliwość otrzymania rabatów i kuponów promocyjnych</li>
                </ul>

                <div class="no-account mt-3">
                    <a href="{$urls.pages.register}" data-link-action="display-register-form" class="btn btn-secondary btn-register">
                        zarejestruj się
                    </a>
                </div>
            </div>
        </div>
    </div>
{/block}