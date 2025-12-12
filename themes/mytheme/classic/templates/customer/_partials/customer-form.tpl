{**
 * Plik: themes/mytheme/templates/customer/_partials/customer-form.tpl
 *}
{block name='customer_form'}
  
  {block name='customer_form_errors'}
    {include file='_partials/form-errors.tpl' errors=$errors['']}
  {/block}

<form action="{block name='customer_form_actionurl'}{$action}{/block}" id="customer-form" class="js-customer-form" method="post">
  <section>
    
    <input type="hidden" name="firstname" value="Klient">
    <input type="hidden" name="lastname" value="Sklepu">
    <input type="hidden" name="id_gender" value="1">
    <input type="hidden" name="birthday" value="">
    <input type="hidden" name="optin" value="1"> 
    
    <div class="form-group row align-items-center">
        <label class="col-md-3 form-control-label text-md-right required">
          * E-mail:
        </label>
        <div class="col-md-6">
          <input class="form-control" name="email" type="email" value="" required>
        </div>
    </div>

    <div class="form-group row align-items-center">
        <label class="col-md-3 form-control-label text-md-right required">
          * Hasło:
        </label>
        <div class="col-md-6">
          <div class="input-group js-parent-focus">
            <input 
              class="form-control js-child-focus js-visible-password" 
              name="password" 
              id="field-password" 
              type="password" 
              value="" 
              pattern=".{literal}{5,}{/literal}"
              required
            >
          </div>
          <small class="form-text text-muted">Minimum 5 znaków</small>
        </div>
    </div>

    <div class="form-group row align-items-center">
        <label class="col-md-3 form-control-label text-md-right required">
          * Powtórz hasło:
        </label>
        <div class="col-md-6">
          <input class="form-control" id="field-password-confirm" type="password" value="" required>
          <small class="form-text text-muted" id="password-match-error" style="color:red; display:none;">Hasła muszą być identyczne</small>
        </div>
    </div>

    {foreach from=$formFields item="field"}
        {if $field.type === 'checkbox'}
          <div class="form-group row">
             <div class="col-md-3"></div>
             <div class="col-md-9">
                 <div class="custom-checkbox">
                    <input name="{$field.name}" type="checkbox" value="1" {if $field.required}required{/if}>
                    <label>{$field.label nofilter}</label>
                 </div>
             </div>
          </div>
        {/if}
    {/foreach}

  </section>

  <footer class="form-footer clearfix" style="margin-top: 30px; text-align: right;">
    <input type="hidden" name="submitCreate" value="1">
    
    <button class="btn btn-primary form-control-submit float-xs-right btn-register-dark" data-link-action="save-customer" type="submit" onclick="return validatePasswordMatch();">
      zarejestruj się
    </button>
  </footer>
</form>

{* Skrypt walidujący powtórzenie hasła *}
<script>
function validatePasswordMatch() {
    var pass = document.getElementById("field-password").value;
    var conf = document.getElementById("field-password-confirm").value;
    var errorMsg = document.getElementById("password-match-error");

    if (pass != conf) {
        errorMsg.style.display = "block";
        document.getElementById("field-password-confirm").style.borderColor = "red";
        return false;
    } else {
        errorMsg.style.display = "none";
        document.getElementById("field-password-confirm").style.borderColor = "#ccc";
        return true;
    }
}
</script>
{/block}