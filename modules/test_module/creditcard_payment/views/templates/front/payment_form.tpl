<form action="{$link->getModuleLink('creditcard_payment', 'validation', [], true)}" method="post">
  <div style="background: #f8f8f8; padding: 20px; border: 1px solid #ddd; border-radius: 5px; margin-bottom: 20px;">
    
    <p><strong>Dane karty</strong></p>
    
    <div class="form-group">
      <label>Numer karty</label>
      <input type="text" name="card_number" class="form-control" placeholder="0000 0000 0000 0000" required />
    </div>

    <div class="row">
      <div class="col-md-6">
        <div class="form-group">
          <label>Data ważności (MM/RR)</label>
          <input type="text" name="card_expiry" class="form-control" placeholder="12/25" required />
        </div>
      </div>
      <div class="col-md-6">
        <div class="form-group">
          <label>Kod CVV</label>
          <input type="text" name="card_cvv" class="form-control" placeholder="123" required />
        </div>
      </div>
    </div>

    <div class="form-group">
      <label>Właściciel karty</label>
      <input type="text" name="card_holder" class="form-control" required />
    </div>

  </div>
</form>