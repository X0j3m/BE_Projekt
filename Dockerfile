FROM prestashop/prestashop:1.7.8

ENV PS_INSTALL_AUTO=0

COPY ./prestashop_source /var/www/html

COPY ./modules/test_module /var/www/html/modules/test_module
COPY ./themes/mytheme/classic /var/www/html/themes/classic

COPY ./img/logo.png /var/www/html/img/logo.png
COPY ./img/logo.png /var/www/html/img/logo_mail.png
COPY ./img/logo.png /var/www/html/img/logo_invoice.png
COPY ./img/inpost-kurier.jpg /var/www/html/img/s/1.jpg
COPY ./img/orlen-paczka.jpg /var/www/html/img/s/2.jpg
COPY ./img/poczta-polska.jpg /var/www/html/img/s/3.jpg

RUN chown -R www-data:www-data /var/www/html
RUN rm -rf /var/www/html/install