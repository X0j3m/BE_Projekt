FROM prestashop/prestashop:1.7.8

COPY ./prestashop_source /var/www/html

COPY ./modules/test_module /var/www/html/modules
COPY ./themes/mytheme/classic /var/www/html/themes/classic

COPY ./img/logo.png /var/www/html/img/logo.png
COPY ./img/logo.png /var/www/html/img/logo_mail.png
COPY ./img/logo.png /var/www/html/img/logo_invoice.png
COPY ./img/inpost-kurier.jpg /var/www/html/img/s/1.jpg
COPY ./img/orlen-paczka.jpg /var/www/html/img/s/2.jpg
COPY ./img/poczta-polska.jpg /var/www/html/img/s/3.jpg

RUN chown -R www-data:www-data /var/www/html

COPY ./ssl/cert.pem /etc/ssl/certs/ssl-cert-snakeoil.pem
COPY ./ssl/key.pem /etc/ssl/private/ssl-cert-snakeoil.key

COPY ./prestashop.sql /tmp/prestashop.sql
COPY ./import-db.sh /usr/local/bin/import-db.sh
RUN chmod +x /usr/local/bin/import-db.sh

RUN rm -rf /var/www/html/install

RUN a2enmod ssl && a2ensite default-ssl

ENTRYPOINT ["/usr/local/bin/import-db.sh"]