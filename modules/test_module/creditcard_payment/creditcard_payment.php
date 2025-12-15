<?php
/**
 * Moduł płatności kartą - wersja edukacyjna
 * Nazwa modułu: creditcard_payment
 */

if (!defined('_PS_VERSION_')) {
    exit;
}

use PrestaShop\PrestaShop\Core\Payment\PaymentOption;

class CreditCard_Payment extends PaymentModule
{
    public function __construct()
    {
        $this->name = 'creditcard_payment';
        $this->tab = 'payments_gateways';
        $this->version = '1.0.0';
        $this->author = 'Michał Ptasznik';
        $this->need_instance = 0;
        $this->ps_versions_compliancy = ['min' => '1.7', 'max' => _PS_VERSION_];
        $this->bootstrap = true;

        parent::__construct();

        $this->displayName = $this->l('Płatność Kartą');
        $this->description = $this->l('Płatność kartą z zapisem danych do zamówienia.');
    }

    public function install()
    {
        return parent::install() &&
            $this->registerHook('paymentOptions') &&
            $this->registerHook('paymentReturn');
    }

    public function hookPaymentOptions($params)
    {
        if (!$this->active) {
            return;
        }

        $paymentOption = new PaymentOption();
        $paymentOption->setModuleName($this->name)
            ->setCallToActionText($this->l('Zapłać kartą kredytową / debetową'))
            ->setAction($this->context->link->getModuleLink($this->name, 'validation', array(), true))
            ->setForm($this->fetch('module:creditcard_payment/views/templates/front/payment_form.tpl'));

        return [$paymentOption];
    }

    public function hookPaymentReturn($params)
    {
        return $this->l('Płatność została pomyślnie zarejestrowana.');
    }
}