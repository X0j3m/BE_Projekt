{block name='login_form'}

  {block name='login_form_errors'}
    {include file='_partials/form-errors.tpl' errors=$errors['']}
  {/block}

  <form id="login-form" action="{block name='login_form_actionurl'}{$action}{/block}" method="post">
   
    <section>
      <input type="hidden" name="submitLogin" value="1">
      {block name='login_form_fields'}
        {foreach from=$formFields item="field"}
          {block name='form_field'}
            {* Tu wymuszamy prosty wygląd inputów bez zbędnych divów Presty *}
            <div class="form-group row">
              <label class="col-md-12 form-control-label required" style="font-weight:bold; font-size:14px;">
                {$field.label}
              </label>
              <div class="col-md-12">
                <input 
                  class="form-control" 
                  name="{$field.name}" 
                  type="{$field.type}" 
                  value="{$field.value}" 
                  {if $field.required}required{/if}
                  placeholder=""
                >
              </div>
            </div>
          {/block}
        {/foreach}
      {/block}
      
      <div class="forgot-password">
        <a href="{$urls.pages.password}" rel="nofollow">
          {l s='Forgot your password?' d='Shop.Theme.Customeraccount'}
        </a>
      </div>
    </section>

    <footer class="form-footer text-xs-center clearfix">
      
      {block name='form_buttons'}
        <button id="submit-login" class="btn btn-primary" data-link-action="sign-in" type="submit">
          {l s='Sign in' d='Shop.Theme.Actions'}
        </button>
      {/block}
    </footer>
  </form>
{/block}
