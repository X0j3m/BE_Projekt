{**
 * Plik: themes/mytheme/templates/customer/registration.tpl
 *}
{extends file='page.tpl'}

{block name='page_title'}
  {l s='Create an account' d='Shop.Theme.Customeraccount'}
{/block}

{block name='page_content'}
    
    <div class="register-social-login mb-4">
        <h3 class="h3" style="font-size: 16px; margin-bottom: 15px;">Zaloguj się przez konto społecznościowe</h3>
        <div class="social-buttons-wrapper">
             {* Tutaj pojawią się przyciski Facebook/Google z modułu, jeśli go masz *}
             {hook h='displayCustomerLoginFormAfter'}
        </div>
        <hr style="margin: 30px 0; border-top: 1px solid #eee;">
    </div>

    <div class="register-form-container">
        {block name='register_form_container'}
          {$hook_create_account_top nofilter}
          
          <section class="register-form">
            <h3 class="h3" style="font-size: 18px; margin-bottom: 20px; font-weight: bold;">Rejestracja</h3>
            
            {* Wczytujemy plik z polami (Krok 2) *}
            {render file='customer/_partials/customer-form.tpl' ui=$register_form}
          </section>
        {/block}
    </div>
{/block}