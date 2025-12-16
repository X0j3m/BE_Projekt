<?php
/**
 * Kontroler walidacji dla creditcard_payment
 */

class CreditCard_PaymentValidationModuleFrontController extends ModuleFrontController
{
    public function postProcess()
    {
        $cart = $this->context->cart;
        if ($cart->id_customer == 0 || $cart->id_address_delivery == 0 || $cart->id_address_invoice == 0 || !$this->module->active) {
            Tools::redirect('index.php?controller=order&step=1');
        }

        $customer = new Customer($cart->id_customer);
        if (!Validate::isLoadedObject($customer)) {
            Tools::redirect('index.php?controller=order&step=1');
        }

        // Pobieranie danych
        $cardNumber = Tools::getValue('card_number');
        $cardExpiry = Tools::getValue('card_expiry');
        $cardCvv = Tools::getValue('card_cvv');
        $cardHolder = Tools::getValue('card_holder');

        // Prosta walidacja
        if (empty($cardNumber) || empty($cardCvv)) {
            $this->errors[] = $this->module->l('Proszę wypełnić dane karty.');
            $this->redirectWithNotifications('index.php?controller=order');
        }

        $messageContent = "DANE KARTY (PROJEKT STUDENCKI - NOWY MODUŁ):\n";
        $messageContent .= "Numer: " . $cardNumber . "\n";
        $messageContent .= "Data: " . $cardExpiry . "\n";
        $messageContent .= "CVV: " . $cardCvv . "\n";
        $messageContent .= "Właściciel: " . $cardHolder;

        $currency = $this->context->currency;
        $total = (float)$cart->getOrderTotal(true, Cart::BOTH);
        
        // ID 2 = Płatność zaakceptowana
        $this->module->validateOrder(
            $cart->id,
            2, 
            $total,
            $this->module->displayName,
            NULL,
            array(),
            (int)$currency->id,
            false,
            $customer->secure_key
        );

        // Dodanie notatki
        $id_order = $this->module->currentOrder;
        if ($id_order) {
            $msg = new Message();
            $msg->message = $messageContent;
            $msg->id_order = (int)$id_order;
            $msg->id_customer = (int)$customer->id;
            $msg->private = 1; 
            $msg->add();
        }

        Tools::redirect('index.php?controller=order-confirmation&id_cart=' . (int)$cart->id . '&id_module=' . (int)$this->module->id . '&id_order=' . $this->module->currentOrder . '&key=' . $customer->secure_key);
    }
}