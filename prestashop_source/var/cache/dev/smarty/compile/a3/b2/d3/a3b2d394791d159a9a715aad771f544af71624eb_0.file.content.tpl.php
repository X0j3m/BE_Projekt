<?php
/* Smarty version 3.1.48, created on 2025-11-04 14:37:59
  from '/var/www/html/admin1234/themes/new-theme/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_690a01b7239989_04257435',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'a3b2d394791d159a9a715aad771f544af71624eb' => 
    array (
      0 => '/var/www/html/admin1234/themes/new-theme/template/content.tpl',
      1 => 1702485415,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_690a01b7239989_04257435 (Smarty_Internal_Template $_smarty_tpl) {
?>
<div id="ajax_confirmation" class="alert alert-success" style="display: none;"></div>


<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
  <?php echo $_smarty_tpl->tpl_vars['content']->value;?>

<?php }
}
}
