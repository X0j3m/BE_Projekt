<?php
if (!defined('_PS_VERSION_')) { exit; }

class Ps_PageCopierFoot extends Module
{
    public function __construct()
    {
        $this->name = 'ps_pagecopierfoot';
        $this->tab = 'front_office_features';
        $this->version = '1.0.1';
        $this->author = 'Kuba Pastuszka';
        $this->bootstrap = true;
        parent::__construct();
        $this->displayName = 'Pancernik Footer';
        $this->description = 'Stopka a la Pancernik';
    }

    public function install()
    {
        return parent::install() &&
            $this->registerHook('displayFooterPancernik') && // Twój hook stopki
            $this->registerHook('displayHeader');            // <--- NOWY: Hook do ładowania CSS
    }

    // Funkcja ładująca CSS (wykonuje się w sekcji <head> strony)
    public function hookDisplayHeader()
    {
        $this->context->controller->registerStylesheet(
            'modules-ps_pagecopierfoot-style', // Unikalne ID stylu
            'modules/'.$this->name.'/views/css/front.css', // Ścieżka do pliku
            ['media' => 'all', 'priority' => 150] // Priorytet (wyższy = ładowany później)
        );
    }

    public function hookDisplayFooterPancernik($params)
    {
        return $this->display(__FILE__, 'views/templates/hook/footer_display.tpl');
    }
}