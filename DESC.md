This file contains very basic descriptions for modules and themes, making it easier to navigate through them:

**THEMES**

#TO READ
# https://devdocs.prestashop-project.org/9/themes/reference/template-inheritance/
# https://devdocs.prestashop-project.org/9/themes/reference/templates/templates-layouts/

 * themes/mytheme/classic/templates/layouts/layouts-both-columns.tpl -->> This file is on the top of hierarchy, contains only blocks of main page (header, footer etc.). Each of this block has
code line that references to specific template, for example in footer block there is an evaluation of '{include file="_partials/footer.tpl"}' and so on. Inside this file we set only the overall page
layout.

**MODULES**

#TO READ
# https://devdocs.prestashop-project.org/9/modules/creation/tutorial/
# https://devdocs.prestashop-project.org/1.7/modules/concepts/hooks/#using-hooks
# https://devdocs.prestashop-project.org/9/themes/reference/hooks/

 * modules/test_module/mymodule -->> This folder has one .php file which contains various operation to be made on our page. The most important thing is, that inside this file we can create and register __HOOK__ (Hook is a 'handle' to a function which later on can be called from many different points of our project). At this point we have one new hook named 'displayHome' which only prints simple text. We use this hook on {_partials/footer.tpl} -> 
 
<div class="row">
      {block name='hook_footer_after'}
        {hook h='displayHome'}
      {/block}
</div>
 
We can immediately see its result on our page after "mymodule" installation and page refreshing. 

