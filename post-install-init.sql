-- Konfiguracja adresu email
UPDATE ps_configuration SET value = 3 WHERE name = 'PS_MAIL_TYPE';
UPDATE ps_configuration SET value = 2 WHERE name = 'PS_MAIL_METHOD';
UPDATE ps_configuration SET value = 'smtp.gmail.com' WHERE name = 'PS_MAIL_SERVER';
UPDATE ps_configuration SET value = 'presta.pancernik@gmail.com' WHERE name = 'PS_MAIL_USER';
UPDATE ps_configuration SET value = 'hrxh ncbc tvqq uwxw' WHERE name = 'PS_MAIL_PASSWD';
UPDATE ps_configuration SET value = 'ssl' WHERE name = 'PS_MAIL_SMTP_ENCRYPTION';
UPDATE ps_configuration SET value = 465 WHERE name = 'PS_MAIL_SMTP_PORT';

-- Konfiguracja przewoznikow
DELETE FROM prestashop.ps_delivery WHERE id_carrier >= 1;
DELETE FROM prestashop.ps_carrier_lang WHERE id_carrier >= 1;
DELETE FROM prestashop.ps_carrier_shop WHERE id_carrier >= 1;
DELETE FROM prestashop.ps_carrier WHERE id_carrier >= 1;
DELETE FROM prestashop.ps_range_weight WHERE id_range_weight >= 1;
ALTER TABLE prestashop.ps_carrier AUTO_INCREMENT = 1;
ALTER TABLE prestashop.ps_delivery AUTO_INCREMENT = 1;
ALTER TABLE prestashop.ps_range_weight AUTO_INCREMENT = 1;

INSERT INTO prestashop.ps_carrier (id_reference, id_tax_rules_group, name, url, active, deleted, shipping_handling, range_behavior, is_module, is_free, shipping_external, need_range, external_module_name, shipping_method, position, max_width, max_height, max_depth, max_weight, grade) VALUES (1, 0, 'Kurier InPost', 'https://inpost.pl/sledzenie-przesylek/?number=@', 1, 0, 0, 1, 0, 0, 0, 0, '', 1, 0, 41, 38, 64, 50.000000, 1);
INSERT INTO prestashop.ps_carrier (id_reference, id_tax_rules_group, name, url, active, deleted, shipping_handling, range_behavior, is_module, is_free, shipping_external, need_range, external_module_name, shipping_method, position, max_width, max_height, max_depth, max_weight, grade) VALUES (2, 0, 'ORLEN Paczka', 'https://www.orlenpaczka.pl/sledz-paczke/@', 1, 0, 0, 1, 0, 0, 0, 0, '', 1, 1, 41, 38, 64, 50.000000, 1);
INSERT INTO prestashop.ps_carrier (id_reference, id_tax_rules_group, name, url, active, deleted, shipping_handling, range_behavior, is_module, is_free, shipping_external, need_range, external_module_name, shipping_method, position, max_width, max_height, max_depth, max_weight, grade) VALUES (3, 0, 'List polecony ekonomiczny', 'https://emonitoring.poczta-polska.pl/@', 1, 0, 0, 1, 0, 0, 0, 0, '', 1, 2, 41, 38, 64, 50.000000, 2);

INSERT INTO prestashop.ps_carrier_lang (id_carrier, id_shop, id_lang, delay) VALUES (1, 1, 1, '1-2 dni robocze');
INSERT INTO prestashop.ps_carrier_lang (id_carrier, id_shop, id_lang, delay) VALUES (2, 1, 1, '1-2 dni robocze');
INSERT INTO prestashop.ps_carrier_lang (id_carrier, id_shop, id_lang, delay) VALUES (3, 1, 1, '1-7 dni robocze');

INSERT INTO prestashop.ps_carrier_shop (id_carrier, id_shop) VALUES (1, 1);
INSERT INTO prestashop.ps_carrier_shop (id_carrier, id_shop) VALUES (2, 1);
INSERT INTO prestashop.ps_carrier_shop (id_carrier, id_shop) VALUES (3, 1);

INSERT INTO prestashop.ps_delivery (id_shop, id_shop_group, id_carrier, id_range_price, id_range_weight, id_zone, price) VALUES (null, null, 1, null, 1, 1, 4.900000);
INSERT INTO prestashop.ps_delivery (id_shop, id_shop_group, id_carrier, id_range_price, id_range_weight, id_zone, price) VALUES (null, null, 1, null, 2, 1, 9.900000);
INSERT INTO prestashop.ps_delivery (id_shop, id_shop_group, id_carrier, id_range_price, id_range_weight, id_zone, price) VALUES (null, null, 1, null, 3, 1, 19.900000);
INSERT INTO prestashop.ps_delivery (id_shop, id_shop_group, id_carrier, id_range_price, id_range_weight, id_zone, price) VALUES (null, null, 2, null, 1, 1, 4.900000);
INSERT INTO prestashop.ps_delivery (id_shop, id_shop_group, id_carrier, id_range_price, id_range_weight, id_zone, price) VALUES (null, null, 2, null, 2, 1, 9.900000);
INSERT INTO prestashop.ps_delivery (id_shop, id_shop_group, id_carrier, id_range_price, id_range_weight, id_zone, price) VALUES (null, null, 2, null, 3, 1, 19.900000);
INSERT INTO prestashop.ps_delivery (id_shop, id_shop_group, id_carrier, id_range_price, id_range_weight, id_zone, price) VALUES (null, null, 3, null, 1, 1, 1.900000);
INSERT INTO prestashop.ps_delivery (id_shop, id_shop_group, id_carrier, id_range_price, id_range_weight, id_zone, price) VALUES (null, null, 3, null, 2, 1, 3.900000);
INSERT INTO prestashop.ps_delivery (id_shop, id_shop_group, id_carrier, id_range_price, id_range_weight, id_zone, price) VALUES (null, null, 3, null, 3, 1, 6.900000);

INSERT INTO prestashop.ps_range_weight (id_range_weight, id_carrier, delimiter1, delimiter2) VALUES (1, 1, 0.000000, 10.000000);
INSERT INTO prestashop.ps_range_weight (id_range_weight, id_carrier, delimiter1, delimiter2) VALUES (2, 1, 10.000000, 25.000000);
INSERT INTO prestashop.ps_range_weight (id_range_weight, id_carrier, delimiter1, delimiter2) VALUES (3, 1, 25.000000, 50.000000);

-- Konfiguracja darmowej wysylki
UPDATE ps_configuration SET value = 0 WHERE name = 'PS_SHIPPING_HANDLING';
UPDATE ps_configuration SET value = 2000 WHERE name = 'PS_SHIPPING_FREE_PRICE';