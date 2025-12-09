<?php
if (!defined('_PS_VERSION_')) {
    exit;
}


class MyModule extends Module{

    public function __construct()
    {
        $this->name = 'mymodule';
        $this->author = 'Rysiek';
        $this->version = '1.0.0';
        $this->displayName = $this->l('Mymodule');
        $this->description = $this->l('Pierwszy nowy modul BE');
        $this->ps_versions_compliancy = array('min' => '1.7.0.0', 'max' => '1.7.999');
        $this->bootstrap = true;
        parent::__construct();
    }
    public function install()
    {
        return parent::install() && $this->registerHook('displayHome');
    }
    public function uninstall()
    {
        return parent::uninstall();
    }
    public function hookDisplayHome()
    {
        return $this->display(__FILE__, 'views/templates/hook/home.tpl');
    }
}