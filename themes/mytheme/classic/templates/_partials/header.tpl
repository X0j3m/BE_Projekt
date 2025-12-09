<div class="header-pancernik" style="
background-color: #323334;
padding: 0 0 0 0;
">
  <div class="header-banner-pancernik" style="
background-color: #4a4c4e;
text-align: center;
padding: 0 0 0 0;">
  <a href="#" style="text-decoration: none; color: #fff; padding: 0 0 0 0;">
    <p style="color: #fff;"> 🎁 <strong>Kody rabatowe i promocje</strong>  - sprawdź aktualne oferty! ⚡ </p>
  </a>
</div>
  <div class="header-top-pancernik" style="text-align: right; padding: 0px 50px 0px 0px;">
    <a href="http://localhost:8080/login?create_account=1" data-link-action="display-register-form" style="color: #ccc;">
      Zarejestruj się
    </a>
    <a href="http://localhost:8080/my-account" title="Zaloguj się do swojego konta klienta" rel="nofollow" style="color: #ccc;">
      <i class="material-icons"></i>
      <span class="hidden-sm-down">Zaloguj się</span>
    </a>
  </div>

  <div class="header-kontakt-pancernik" style="text-align: right; padding: 20px 50px 20px 0; font-size: 16px">

    tel.: 
    <a href="tel:+48699577774" style="color: #e3bf5d;">+48 699 577 774</a> 
    e-mail:
    <span style="color: #e3bf5d;">sklep@pancernik.eu</span>
  </div>

  <div class="header-main-bar" style="
      display: flex; 
      align-items: center; 
      justify-content: space-between; 
      padding: 0px 50px;
      gap: 30px;
  ">
      
      <div class="logo-wrapper" style="flex-shrink: 0;">
         <a href="{$urls.base_url}">
           <img class="logo" src="{$urls.img_url}reprezentant.webp" alt="{$shop.name}" style="max-height: 120px;">
         </a>
      </div>
      

      <div class="search-cart-wrapper" style="
          text-align: right;
          display: flex; 
          align-items: center; 
          flex-grow: 1; 
          justify-content: flex-end; 
          gap: 15px;
      ">
          
          <div class="custom-search" style="max-width: 800px; text-align:right; flex-grow: 1;">
              {widget name='ps_searchbar'}
          </div>

          <div class="custom-cart" style="min-width: 100px;">
              <div id="_desktop_cart">
                  <a href="{$urls.base_url}cart" title="Koszyk" rel="nofollow" style="text-decoration: none; color: inherit;">
                      {widget name='ps_shoppingcart'}
                  </a>
              </div>
          </div>

      </div>

  </div>

</div>

<div class="header-menu-pancernik" style="
      background-color: #262626; /* Ciemne tło menu */
      border-top: 1px solid #444; /* Lekka linia oddzielająca */
      width: 100%;
  ">
      <div class="container" style="color: #fff;">
          {widget name='ps_mainmenu'}
      </div>
  </div>

</div>
</div>