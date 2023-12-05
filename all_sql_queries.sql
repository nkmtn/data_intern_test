-----------------
-- DAU
-----------------

-- GENERAL
SELECT date, COUNT(*) FROM account_date_session GROUP BY date;
-- APAC
SELECT date, COUNT(*) FROM account_date_session
LEFT JOIN account on account.account_id=account_date_session.account_id
WHERE account.country_code IN ('MH', 'IN', 'HK', 'MO', 'HM', 'PW', 'MM', 'MV', 'PG', 'GU', 'NR', 'NP', 'ID', 'WS', 'KR', 'KG', 'SG', 'MN', 'NF', 'MP', 'PN', 'MY', 'FM', 'JP', 'PK', 'LA', 'KI', 'KV', 'NU', 'PH', 'TF', 'CC', 'CK', 'TL', 'TK', 'CX', 'CN', 'TO', 'KH', 'TM', 'TV', 'BN', 'IO', 'BT', 'UM', 'BD', 'UZ', 'VU', 'AU', 'AQ', 'VN', 'AS', 'WF', 'TH', 'TJ', 'NC', 'FJ', 'LK', 'PF', 'NZ', 'TW', 'SB')
GROUP BY date;
-- EMEA
SELECT date, COUNT(*) FROM account_date_session
LEFT JOIN account on account.account_id=account_date_session.account_id
WHERE account.country_code IN ('NE', 'UG', 'YE', 'PS', 'UA', 'AE', 'GS', 'GB', 'OM', 'NO', 'SN', 'SS', 'SC', 'EH', 'ZA', 'SO', 'NG', 'SL', 'RS', 'SY', 'ES', 'TZ', 'CH', 'SH', 'SE', 'RW', 'RU', 'SZ', 'TG', 'SJ', 'SA', 'RO', 'SD', 'RE', 'QA', 'SM', 'PT', 'PL', 'ST', 'TN', 'TR', 'SK', 'SI', 'LB', 'KM', 'CD', 'CG', 'CI', 'HR', 'CY', 'CZ', 'DK', 'TD', 'DJ', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FO', 'FI', 'FR', 'EG', 'CF', 'CV', 'CM', 'AF', 'AX', 'AL', 'DZ', 'AD', 'AO', 'AM', 'AT', 'AZ', 'BH', 'BY', 'BE', 'BJ', 'BA', 'BW', 'BV', 'BG', 'BF', 'BI', 'GA', 'GM', 'GE', 'DE', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MK', 'MG', 'MW', 'ML', 'MT', 'MR', 'MU', 'YT', 'MD', 'MC', 'ME', 'MA', 'MZ', 'ZM', 'NL', 'LV', 'KE', 'GH', 'GI', 'GR', 'GL', 'GG', 'GN', 'GW', 'VA', 'HU', 'IS', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JE', 'JO', 'KZ', 'KW', 'ZW')
GROUP BY date;
-- NA
SELECT date, COUNT(*) FROM account_date_session
LEFT JOIN account on account.account_id=account_date_session.account_id
WHERE account.country_code IN ('CA', 'US')
GROUP BY date;
-- LATAM
SELECT date, COUNT(*) FROM account_date_session
LEFT JOIN account on account.account_id=account_date_session.account_id
WHERE account.country_code IN ('PY', 'PE', 'KY', 'TT', 'CL', 'PR', 'CO', 'BL', 'CR', 'JM', 'CU', 'CW', 'KN', 'TC', 'LC', 'PM', 'DM', 'DO', 'EC', 'VC', 'SV', 'SR', 'HN', 'HT', 'GY', 'GF', 'GT', 'GP', 'GD', 'MF', 'PA', 'SX', 'BR', 'NI', 'VI', 'VG', 'MS', 'AI', 'AG', 'AR', 'VE', 'AW', 'BS', 'BB', 'MX', 'BZ', 'UY', 'BQ', 'BO', 'MQ', 'BM')
GROUP BY date;

-----------------
-- DAU TRENDS
-----------------

-- GENERAL
SELECT date, COUNT(*) AS count FROM account_date_session
LEFT JOIN account ON account.account_id=account_date_session.account_id
GROUP BY date;
-- APAC
SELECT date, COUNT(*) AS count FROM account_date_session
LEFT JOIN account on account.account_id=account_date_session.account_id
WHERE account.country_code IN ('MH', 'IN', 'HK', 'MO', 'HM', 'PW', 'MM', 'MV', 'PG', 'GU', 'NR', 'NP', 'ID', 'WS', 'KR', 'KG', 'SG', 'MN', 'NF', 'MP', 'PN', 'MY', 'FM', 'JP', 'PK', 'LA', 'KI', 'KV', 'NU', 'PH', 'TF', 'CC', 'CK', 'TL', 'TK', 'CX', 'CN', 'TO', 'KH', 'TM', 'TV', 'BN', 'IO', 'BT', 'UM', 'BD', 'UZ', 'VU', 'AU', 'AQ', 'VN', 'AS', 'WF', 'TH', 'TJ', 'NC', 'FJ', 'LK', 'PF', 'NZ', 'TW', 'SB')
GROUP BY date;
-- EMEA
SELECT date, COUNT(*) AS count FROM account_date_session
LEFT JOIN account on account.account_id=account_date_session.account_id
WHERE account.country_code IN ('NE', 'UG', 'YE', 'PS', 'UA', 'AE', 'GS', 'GB', 'OM', 'NO', 'SN', 'SS', 'SC', 'EH', 'ZA', 'SO', 'NG', 'SL', 'RS', 'SY', 'ES', 'TZ', 'CH', 'SH', 'SE', 'RW', 'RU', 'SZ', 'TG', 'SJ', 'SA', 'RO', 'SD', 'RE', 'QA', 'SM', 'PT', 'PL', 'ST', 'TN', 'TR', 'SK', 'SI', 'LB', 'KM', 'CD', 'CG', 'CI', 'HR', 'CY', 'CZ', 'DK', 'TD', 'DJ', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FO', 'FI', 'FR', 'EG', 'CF', 'CV', 'CM', 'AF', 'AX', 'AL', 'DZ', 'AD', 'AO', 'AM', 'AT', 'AZ', 'BH', 'BY', 'BE', 'BJ', 'BA', 'BW', 'BV', 'BG', 'BF', 'BI', 'GA', 'GM', 'GE', 'DE', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MK', 'MG', 'MW', 'ML', 'MT', 'MR', 'MU', 'YT', 'MD', 'MC', 'ME', 'MA', 'MZ', 'ZM', 'NL', 'LV', 'KE', 'GH', 'GI', 'GR', 'GL', 'GG', 'GN', 'GW', 'VA', 'HU', 'IS', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JE', 'JO', 'KZ', 'KW', 'ZW')
GROUP BY date;
-- NA
SELECT date, COUNT(*) AS count FROM account_date_session
LEFT JOIN account on account.account_id=account_date_session.account_id
WHERE account.country_code IN ('CA', 'US')
GROUP BY date;
-- LATAM
SELECT date, COUNT(*) AS count FROM account_date_session
LEFT JOIN account on account.account_id=account_date_session.account_id
WHERE account.country_code IN ('PY', 'PE', 'KY', 'TT', 'CL', 'PR', 'CO', 'BL', 'CR', 'JM', 'CU', 'CW', 'KN', 'TC', 'LC', 'PM', 'DM', 'DO', 'EC', 'VC', 'SV', 'SR', 'HN', 'HT', 'GY', 'GF', 'GT', 'GP', 'GD', 'MF', 'PA', 'SX', 'BR', 'NI', 'VI', 'VG', 'MS', 'AI', 'AG', 'AR', 'VE', 'AW', 'BS', 'BB', 'MX', 'BZ', 'UY', 'BQ', 'BO', 'MQ', 'BM')
GROUP BY date;

-----------------
-- REVENUE
-----------------

-- NUMBER OF USERS PER REGION
SELECT v.column2 as region, COUNT(account_id) AS users FROM account
JOIN (VALUES ('PY', 'LATAM'),('PE', 'LATAM'),('CA', 'NA'),('KY', 'LATAM'),('TT', 'LATAM'),('CL', 'LATAM'),('PR', 'LATAM'),('CO', 'LATAM'),('BL', 'LATAM'),('CR', 'LATAM'),('JM', 'LATAM'),('CU', 'LATAM'),('CW', 'LATAM'),('KN', 'LATAM'),('TC', 'LATAM'),('LC', 'LATAM'),('PM', 'LATAM'),('DM', 'LATAM'),('DO', 'LATAM'),('EC', 'LATAM'),('VC', 'LATAM'),('SV', 'LATAM'),('SR', 'LATAM'),('HN', 'LATAM'),('HT', 'LATAM'),('GY', 'LATAM'),('GF', 'LATAM'),('GT', 'LATAM'),('GP', 'LATAM'),('GD', 'LATAM'),('MF', 'LATAM'),('PA', 'LATAM'),('SX', 'LATAM'),('BR', 'LATAM'),('NI', 'LATAM'),('VI', 'LATAM'),('VG', 'LATAM'),('MS', 'LATAM'),('AI', 'LATAM'),('AG', 'LATAM'),('AR', 'LATAM'),('VE', 'LATAM'),('AW', 'LATAM'),('BS', 'LATAM'),('BB', 'LATAM'),('US', 'NA'),('MX', 'LATAM'),('BZ', 'LATAM'),('UY', 'LATAM'),('BQ', 'LATAM'),('BO', 'LATAM'),('MQ', 'LATAM'),('BM', 'LATAM'),('MH', 'APAC'),('IN', 'APAC'),('HK', 'APAC'),('MO', 'APAC'),('HM', 'APAC'),('PW', 'APAC'),('MM', 'APAC'),('MV', 'APAC'),('PG', 'APAC'),('GU', 'APAC'),('NR', 'APAC'),('NP', 'APAC'),('ID', 'APAC'),('WS', 'APAC'),('KR', 'APAC'),('KG', 'APAC'),('SG', 'APAC'),('MN', 'APAC'),('NF', 'APAC'),('MP', 'APAC'),('PN', 'APAC'),('MY', 'APAC'),('FM', 'APAC'),('JP', 'APAC'),('PK', 'APAC'),('LA', 'APAC'),('KI', 'APAC'),('KV', 'APAC'),('NU', 'APAC'),('PH', 'APAC'),('TF', 'APAC'),('CC', 'APAC'),('CK', 'APAC'),('TL', 'APAC'),('TK', 'APAC'),('CX', 'APAC'),('CN', 'APAC'),('TO', 'APAC'),('KH', 'APAC'),('TM', 'APAC'),('TV', 'APAC'),('BN', 'APAC'),('IO', 'APAC'),('BT', 'APAC'),('UM', 'APAC'),('BD', 'APAC'),('UZ', 'APAC'),('VU', 'APAC'),('AU', 'APAC'),('AQ', 'APAC'),('VN', 'APAC'),('AS', 'APAC'),('WF', 'APAC'),('TH', 'APAC'),('TJ', 'APAC'),('NC', 'APAC'),('FJ', 'APAC'),('LK', 'APAC'),('PF', 'APAC'),('NZ', 'APAC'),('TW', 'APAC'),('SB', 'APAC'),('NE', 'EMEA'),('UG', 'EMEA'),('YE', 'EMEA'),('PS', 'EMEA'),('UA', 'EMEA'),('AE', 'EMEA'),('GS', 'EMEA'),('GB', 'EMEA'),('OM', 'EMEA'),('NO', 'EMEA'),('SN', 'EMEA'),('SS', 'EMEA'),('SC', 'EMEA'),('EH', 'EMEA'),('ZA', 'EMEA'),('SO', 'EMEA'),('NG', 'EMEA'),('SL', 'EMEA'),('RS', 'EMEA'),('SY', 'EMEA'),('ES', 'EMEA'),('TZ', 'EMEA'),('CH', 'EMEA'),('SH', 'EMEA'),('SE', 'EMEA'),('RW', 'EMEA'),('RU', 'EMEA'),('SZ', 'EMEA'),('TG', 'EMEA'),('SJ', 'EMEA'),('SA', 'EMEA'),('RO', 'EMEA'),('SD', 'EMEA'),('RE', 'EMEA'),('QA', 'EMEA'),('SM', 'EMEA'),('PT', 'EMEA'),('PL', 'EMEA'),('ST', 'EMEA'),('TN', 'EMEA'),('TR', 'EMEA'),('SK', 'EMEA'),('SI', 'EMEA'),('LB', 'EMEA'),('nan', 'EMEA'),('KM', 'EMEA'),('CD', 'EMEA'),('CG', 'EMEA'),('CI', 'EMEA'),('HR', 'EMEA'),('CY', 'EMEA'),('CZ', 'EMEA'),('DK', 'EMEA'),('TD', 'EMEA'),('DJ', 'EMEA'),('GQ', 'EMEA'),('ER', 'EMEA'),('EE', 'EMEA'),('ET', 'EMEA'),('FK', 'EMEA'),('FO', 'EMEA'),('FI', 'EMEA'),('FR', 'EMEA'),('EG', 'EMEA'),('CF', 'EMEA'),('CV', 'EMEA'),('CM', 'EMEA'),('AF', 'EMEA'),('AX', 'EMEA'),('AL', 'EMEA'),('DZ', 'EMEA'),('AD', 'EMEA'),('AO', 'EMEA'),('AM', 'EMEA'),('AT', 'EMEA'),('AZ', 'EMEA'),('BH', 'EMEA'),('BY', 'EMEA'),('BE', 'EMEA'),('BJ', 'EMEA'),('BA', 'EMEA'),('BW', 'EMEA'),('BV', 'EMEA'),('BG', 'EMEA'),('BF', 'EMEA'),('BI', 'EMEA'),('GA', 'EMEA'),('GM', 'EMEA'),('GE', 'EMEA'),('DE', 'EMEA'),('LS', 'EMEA'),('LR', 'EMEA'),('LY', 'EMEA'),('LI', 'EMEA'),('LT', 'EMEA'),('LU', 'EMEA'),('MK', 'EMEA'),('MG', 'EMEA'),('MW', 'EMEA'),('ML', 'EMEA'),('MT', 'EMEA'),('MR', 'EMEA'),('MU', 'EMEA'),('YT', 'EMEA'),('MD', 'EMEA'),('MC', 'EMEA'),('ME', 'EMEA'),('MA', 'EMEA'),('MZ', 'EMEA'),('ZM', 'EMEA'),('NL', 'EMEA'),('LV', 'EMEA'),('KE', 'EMEA'),('GH', 'EMEA'),('GI', 'EMEA'),('GR', 'EMEA'),('GL', 'EMEA'),('GG', 'EMEA'),('GN', 'EMEA'),('GW', 'EMEA'),('VA', 'EMEA'),('HU', 'EMEA'),('IS', 'EMEA'),('IR', 'EMEA'),('IQ', 'EMEA'),('IE', 'EMEA'),('IM', 'EMEA'),('IL', 'EMEA'),('IT', 'EMEA'),('JE', 'EMEA'),('JO', 'EMEA'),('KZ', 'EMEA'),('KW', 'EMEA'),('ZW', 'EMEA'))
v on account.country_code=v.column1
GROUP BY region ORDER BY region;

-- ABSOLUTE REVENUE PER REGION
SELECT t2.region,  ROUND(SUM(t1.sum) / 100, 0) AS income FROM
(SELECT account_id, SUM(iap_price_usd_cents) + 0.0 as sum FROM iap_purchase GROUP BY account_id) t1
JOIN
(SELECT account_id, v.column2 as region FROM account
JOIN (VALUES ('PY', 'LATAM'),('PE', 'LATAM'),('CA', 'NA'),('KY', 'LATAM'),('TT', 'LATAM'),('CL', 'LATAM'),('PR', 'LATAM'),('CO', 'LATAM'),('BL', 'LATAM'),('CR', 'LATAM'),('JM', 'LATAM'),('CU', 'LATAM'),('CW', 'LATAM'),('KN', 'LATAM'),('TC', 'LATAM'),('LC', 'LATAM'),('PM', 'LATAM'),('DM', 'LATAM'),('DO', 'LATAM'),('EC', 'LATAM'),('VC', 'LATAM'),('SV', 'LATAM'),('SR', 'LATAM'),('HN', 'LATAM'),('HT', 'LATAM'),('GY', 'LATAM'),('GF', 'LATAM'),('GT', 'LATAM'),('GP', 'LATAM'),('GD', 'LATAM'),('MF', 'LATAM'),('PA', 'LATAM'),('SX', 'LATAM'),('BR', 'LATAM'),('NI', 'LATAM'),('VI', 'LATAM'),('VG', 'LATAM'),('MS', 'LATAM'),('AI', 'LATAM'),('AG', 'LATAM'),('AR', 'LATAM'),('VE', 'LATAM'),('AW', 'LATAM'),('BS', 'LATAM'),('BB', 'LATAM'),('US', 'NA'),('MX', 'LATAM'),('BZ', 'LATAM'),('UY', 'LATAM'),('BQ', 'LATAM'),('BO', 'LATAM'),('MQ', 'LATAM'),('BM', 'LATAM'),('MH', 'APAC'),('IN', 'APAC'),('HK', 'APAC'),('MO', 'APAC'),('HM', 'APAC'),('PW', 'APAC'),('MM', 'APAC'),('MV', 'APAC'),('PG', 'APAC'),('GU', 'APAC'),('NR', 'APAC'),('NP', 'APAC'),('ID', 'APAC'),('WS', 'APAC'),('KR', 'APAC'),('KG', 'APAC'),('SG', 'APAC'),('MN', 'APAC'),('NF', 'APAC'),('MP', 'APAC'),('PN', 'APAC'),('MY', 'APAC'),('FM', 'APAC'),('JP', 'APAC'),('PK', 'APAC'),('LA', 'APAC'),('KI', 'APAC'),('KV', 'APAC'),('NU', 'APAC'),('PH', 'APAC'),('TF', 'APAC'),('CC', 'APAC'),('CK', 'APAC'),('TL', 'APAC'),('TK', 'APAC'),('CX', 'APAC'),('CN', 'APAC'),('TO', 'APAC'),('KH', 'APAC'),('TM', 'APAC'),('TV', 'APAC'),('BN', 'APAC'),('IO', 'APAC'),('BT', 'APAC'),('UM', 'APAC'),('BD', 'APAC'),('UZ', 'APAC'),('VU', 'APAC'),('AU', 'APAC'),('AQ', 'APAC'),('VN', 'APAC'),('AS', 'APAC'),('WF', 'APAC'),('TH', 'APAC'),('TJ', 'APAC'),('NC', 'APAC'),('FJ', 'APAC'),('LK', 'APAC'),('PF', 'APAC'),('NZ', 'APAC'),('TW', 'APAC'),('SB', 'APAC'),('NE', 'EMEA'),('UG', 'EMEA'),('YE', 'EMEA'),('PS', 'EMEA'),('UA', 'EMEA'),('AE', 'EMEA'),('GS', 'EMEA'),('GB', 'EMEA'),('OM', 'EMEA'),('NO', 'EMEA'),('SN', 'EMEA'),('SS', 'EMEA'),('SC', 'EMEA'),('EH', 'EMEA'),('ZA', 'EMEA'),('SO', 'EMEA'),('NG', 'EMEA'),('SL', 'EMEA'),('RS', 'EMEA'),('SY', 'EMEA'),('ES', 'EMEA'),('TZ', 'EMEA'),('CH', 'EMEA'),('SH', 'EMEA'),('SE', 'EMEA'),('RW', 'EMEA'),('RU', 'EMEA'),('SZ', 'EMEA'),('TG', 'EMEA'),('SJ', 'EMEA'),('SA', 'EMEA'),('RO', 'EMEA'),('SD', 'EMEA'),('RE', 'EMEA'),('QA', 'EMEA'),('SM', 'EMEA'),('PT', 'EMEA'),('PL', 'EMEA'),('ST', 'EMEA'),('TN', 'EMEA'),('TR', 'EMEA'),('SK', 'EMEA'),('SI', 'EMEA'),('LB', 'EMEA'),('nan', 'EMEA'),('KM', 'EMEA'),('CD', 'EMEA'),('CG', 'EMEA'),('CI', 'EMEA'),('HR', 'EMEA'),('CY', 'EMEA'),('CZ', 'EMEA'),('DK', 'EMEA'),('TD', 'EMEA'),('DJ', 'EMEA'),('GQ', 'EMEA'),('ER', 'EMEA'),('EE', 'EMEA'),('ET', 'EMEA'),('FK', 'EMEA'),('FO', 'EMEA'),('FI', 'EMEA'),('FR', 'EMEA'),('EG', 'EMEA'),('CF', 'EMEA'),('CV', 'EMEA'),('CM', 'EMEA'),('AF', 'EMEA'),('AX', 'EMEA'),('AL', 'EMEA'),('DZ', 'EMEA'),('AD', 'EMEA'),('AO', 'EMEA'),('AM', 'EMEA'),('AT', 'EMEA'),('AZ', 'EMEA'),('BH', 'EMEA'),('BY', 'EMEA'),('BE', 'EMEA'),('BJ', 'EMEA'),('BA', 'EMEA'),('BW', 'EMEA'),('BV', 'EMEA'),('BG', 'EMEA'),('BF', 'EMEA'),('BI', 'EMEA'),('GA', 'EMEA'),('GM', 'EMEA'),('GE', 'EMEA'),('DE', 'EMEA'),('LS', 'EMEA'),('LR', 'EMEA'),('LY', 'EMEA'),('LI', 'EMEA'),('LT', 'EMEA'),('LU', 'EMEA'),('MK', 'EMEA'),('MG', 'EMEA'),('MW', 'EMEA'),('ML', 'EMEA'),('MT', 'EMEA'),('MR', 'EMEA'),('MU', 'EMEA'),('YT', 'EMEA'),('MD', 'EMEA'),('MC', 'EMEA'),('ME', 'EMEA'),('MA', 'EMEA'),('MZ', 'EMEA'),('ZM', 'EMEA'),('NL', 'EMEA'),('LV', 'EMEA'),('KE', 'EMEA'),('GH', 'EMEA'),('GI', 'EMEA'),('GR', 'EMEA'),('GL', 'EMEA'),('GG', 'EMEA'),('GN', 'EMEA'),('GW', 'EMEA'),('VA', 'EMEA'),('HU', 'EMEA'),('IS', 'EMEA'),('IR', 'EMEA'),('IQ', 'EMEA'),('IE', 'EMEA'),('IM', 'EMEA'),('IL', 'EMEA'),('IT', 'EMEA'),('JE', 'EMEA'),('JO', 'EMEA'),('KZ', 'EMEA'),('KW', 'EMEA'),('ZW', 'EMEA'))
v on account.country_code=v.column1) t2
ON t1.account_id = t2.account_id
GROUP BY t2.region ORDER BY region;

-- AVERAGE REVENUE PER REGION
SELECT t3.region as region, ROUND(t3.income / t4.users, 0) AS per_user FROM
(SELECT t2.region, SUM(t1.sum) + 0.0 AS income FROM
(SELECT account_id, SUM(iap_price_usd_cents) as sum FROM iap_purchase GROUP BY account_id) t1
JOIN
(SELECT account_id, v.column2 as region FROM account
JOIN (VALUES ('PY', 'LATAM'),('PE', 'LATAM'),('CA', 'NA'),('KY', 'LATAM'),('TT', 'LATAM'),('CL', 'LATAM'),('PR', 'LATAM'),('CO', 'LATAM'),('BL', 'LATAM'),('CR', 'LATAM'),('JM', 'LATAM'),('CU', 'LATAM'),('CW', 'LATAM'),('KN', 'LATAM'),('TC', 'LATAM'),('LC', 'LATAM'),('PM', 'LATAM'),('DM', 'LATAM'),('DO', 'LATAM'),('EC', 'LATAM'),('VC', 'LATAM'),('SV', 'LATAM'),('SR', 'LATAM'),('HN', 'LATAM'),('HT', 'LATAM'),('GY', 'LATAM'),('GF', 'LATAM'),('GT', 'LATAM'),('GP', 'LATAM'),('GD', 'LATAM'),('MF', 'LATAM'),('PA', 'LATAM'),('SX', 'LATAM'),('BR', 'LATAM'),('NI', 'LATAM'),('VI', 'LATAM'),('VG', 'LATAM'),('MS', 'LATAM'),('AI', 'LATAM'),('AG', 'LATAM'),('AR', 'LATAM'),('VE', 'LATAM'),('AW', 'LATAM'),('BS', 'LATAM'),('BB', 'LATAM'),('US', 'NA'),('MX', 'LATAM'),('BZ', 'LATAM'),('UY', 'LATAM'),('BQ', 'LATAM'),('BO', 'LATAM'),('MQ', 'LATAM'),('BM', 'LATAM'),('MH', 'APAC'),('IN', 'APAC'),('HK', 'APAC'),('MO', 'APAC'),('HM', 'APAC'),('PW', 'APAC'),('MM', 'APAC'),('MV', 'APAC'),('PG', 'APAC'),('GU', 'APAC'),('NR', 'APAC'),('NP', 'APAC'),('ID', 'APAC'),('WS', 'APAC'),('KR', 'APAC'),('KG', 'APAC'),('SG', 'APAC'),('MN', 'APAC'),('NF', 'APAC'),('MP', 'APAC'),('PN', 'APAC'),('MY', 'APAC'),('FM', 'APAC'),('JP', 'APAC'),('PK', 'APAC'),('LA', 'APAC'),('KI', 'APAC'),('KV', 'APAC'),('NU', 'APAC'),('PH', 'APAC'),('TF', 'APAC'),('CC', 'APAC'),('CK', 'APAC'),('TL', 'APAC'),('TK', 'APAC'),('CX', 'APAC'),('CN', 'APAC'),('TO', 'APAC'),('KH', 'APAC'),('TM', 'APAC'),('TV', 'APAC'),('BN', 'APAC'),('IO', 'APAC'),('BT', 'APAC'),('UM', 'APAC'),('BD', 'APAC'),('UZ', 'APAC'),('VU', 'APAC'),('AU', 'APAC'),('AQ', 'APAC'),('VN', 'APAC'),('AS', 'APAC'),('WF', 'APAC'),('TH', 'APAC'),('TJ', 'APAC'),('NC', 'APAC'),('FJ', 'APAC'),('LK', 'APAC'),('PF', 'APAC'),('NZ', 'APAC'),('TW', 'APAC'),('SB', 'APAC'),('NE', 'EMEA'),('UG', 'EMEA'),('YE', 'EMEA'),('PS', 'EMEA'),('UA', 'EMEA'),('AE', 'EMEA'),('GS', 'EMEA'),('GB', 'EMEA'),('OM', 'EMEA'),('NO', 'EMEA'),('SN', 'EMEA'),('SS', 'EMEA'),('SC', 'EMEA'),('EH', 'EMEA'),('ZA', 'EMEA'),('SO', 'EMEA'),('NG', 'EMEA'),('SL', 'EMEA'),('RS', 'EMEA'),('SY', 'EMEA'),('ES', 'EMEA'),('TZ', 'EMEA'),('CH', 'EMEA'),('SH', 'EMEA'),('SE', 'EMEA'),('RW', 'EMEA'),('RU', 'EMEA'),('SZ', 'EMEA'),('TG', 'EMEA'),('SJ', 'EMEA'),('SA', 'EMEA'),('RO', 'EMEA'),('SD', 'EMEA'),('RE', 'EMEA'),('QA', 'EMEA'),('SM', 'EMEA'),('PT', 'EMEA'),('PL', 'EMEA'),('ST', 'EMEA'),('TN', 'EMEA'),('TR', 'EMEA'),('SK', 'EMEA'),('SI', 'EMEA'),('LB', 'EMEA'),('nan', 'EMEA'),('KM', 'EMEA'),('CD', 'EMEA'),('CG', 'EMEA'),('CI', 'EMEA'),('HR', 'EMEA'),('CY', 'EMEA'),('CZ', 'EMEA'),('DK', 'EMEA'),('TD', 'EMEA'),('DJ', 'EMEA'),('GQ', 'EMEA'),('ER', 'EMEA'),('EE', 'EMEA'),('ET', 'EMEA'),('FK', 'EMEA'),('FO', 'EMEA'),('FI', 'EMEA'),('FR', 'EMEA'),('EG', 'EMEA'),('CF', 'EMEA'),('CV', 'EMEA'),('CM', 'EMEA'),('AF', 'EMEA'),('AX', 'EMEA'),('AL', 'EMEA'),('DZ', 'EMEA'),('AD', 'EMEA'),('AO', 'EMEA'),('AM', 'EMEA'),('AT', 'EMEA'),('AZ', 'EMEA'),('BH', 'EMEA'),('BY', 'EMEA'),('BE', 'EMEA'),('BJ', 'EMEA'),('BA', 'EMEA'),('BW', 'EMEA'),('BV', 'EMEA'),('BG', 'EMEA'),('BF', 'EMEA'),('BI', 'EMEA'),('GA', 'EMEA'),('GM', 'EMEA'),('GE', 'EMEA'),('DE', 'EMEA'),('LS', 'EMEA'),('LR', 'EMEA'),('LY', 'EMEA'),('LI', 'EMEA'),('LT', 'EMEA'),('LU', 'EMEA'),('MK', 'EMEA'),('MG', 'EMEA'),('MW', 'EMEA'),('ML', 'EMEA'),('MT', 'EMEA'),('MR', 'EMEA'),('MU', 'EMEA'),('YT', 'EMEA'),('MD', 'EMEA'),('MC', 'EMEA'),('ME', 'EMEA'),('MA', 'EMEA'),('MZ', 'EMEA'),('ZM', 'EMEA'),('NL', 'EMEA'),('LV', 'EMEA'),('KE', 'EMEA'),('GH', 'EMEA'),('GI', 'EMEA'),('GR', 'EMEA'),('GL', 'EMEA'),('GG', 'EMEA'),('GN', 'EMEA'),('GW', 'EMEA'),('VA', 'EMEA'),('HU', 'EMEA'),('IS', 'EMEA'),('IR', 'EMEA'),('IQ', 'EMEA'),('IE', 'EMEA'),('IM', 'EMEA'),('IL', 'EMEA'),('IT', 'EMEA'),('JE', 'EMEA'),('JO', 'EMEA'),('KZ', 'EMEA'),('KW', 'EMEA'),('ZW', 'EMEA'))
v on account.country_code=v.column1) t2
ON t1.account_id = t2.account_id
GROUP BY t2.region) t3
JOIN
(SELECT v.column2 as region, COUNT(account_id) AS users FROM account
JOIN (VALUES ('PY', 'LATAM'),('PE', 'LATAM'),('CA', 'NA'),('KY', 'LATAM'),('TT', 'LATAM'),('CL', 'LATAM'),('PR', 'LATAM'),('CO', 'LATAM'),('BL', 'LATAM'),('CR', 'LATAM'),('JM', 'LATAM'),('CU', 'LATAM'),('CW', 'LATAM'),('KN', 'LATAM'),('TC', 'LATAM'),('LC', 'LATAM'),('PM', 'LATAM'),('DM', 'LATAM'),('DO', 'LATAM'),('EC', 'LATAM'),('VC', 'LATAM'),('SV', 'LATAM'),('SR', 'LATAM'),('HN', 'LATAM'),('HT', 'LATAM'),('GY', 'LATAM'),('GF', 'LATAM'),('GT', 'LATAM'),('GP', 'LATAM'),('GD', 'LATAM'),('MF', 'LATAM'),('PA', 'LATAM'),('SX', 'LATAM'),('BR', 'LATAM'),('NI', 'LATAM'),('VI', 'LATAM'),('VG', 'LATAM'),('MS', 'LATAM'),('AI', 'LATAM'),('AG', 'LATAM'),('AR', 'LATAM'),('VE', 'LATAM'),('AW', 'LATAM'),('BS', 'LATAM'),('BB', 'LATAM'),('US', 'NA'),('MX', 'LATAM'),('BZ', 'LATAM'),('UY', 'LATAM'),('BQ', 'LATAM'),('BO', 'LATAM'),('MQ', 'LATAM'),('BM', 'LATAM'),('MH', 'APAC'),('IN', 'APAC'),('HK', 'APAC'),('MO', 'APAC'),('HM', 'APAC'),('PW', 'APAC'),('MM', 'APAC'),('MV', 'APAC'),('PG', 'APAC'),('GU', 'APAC'),('NR', 'APAC'),('NP', 'APAC'),('ID', 'APAC'),('WS', 'APAC'),('KR', 'APAC'),('KG', 'APAC'),('SG', 'APAC'),('MN', 'APAC'),('NF', 'APAC'),('MP', 'APAC'),('PN', 'APAC'),('MY', 'APAC'),('FM', 'APAC'),('JP', 'APAC'),('PK', 'APAC'),('LA', 'APAC'),('KI', 'APAC'),('KV', 'APAC'),('NU', 'APAC'),('PH', 'APAC'),('TF', 'APAC'),('CC', 'APAC'),('CK', 'APAC'),('TL', 'APAC'),('TK', 'APAC'),('CX', 'APAC'),('CN', 'APAC'),('TO', 'APAC'),('KH', 'APAC'),('TM', 'APAC'),('TV', 'APAC'),('BN', 'APAC'),('IO', 'APAC'),('BT', 'APAC'),('UM', 'APAC'),('BD', 'APAC'),('UZ', 'APAC'),('VU', 'APAC'),('AU', 'APAC'),('AQ', 'APAC'),('VN', 'APAC'),('AS', 'APAC'),('WF', 'APAC'),('TH', 'APAC'),('TJ', 'APAC'),('NC', 'APAC'),('FJ', 'APAC'),('LK', 'APAC'),('PF', 'APAC'),('NZ', 'APAC'),('TW', 'APAC'),('SB', 'APAC'),('NE', 'EMEA'),('UG', 'EMEA'),('YE', 'EMEA'),('PS', 'EMEA'),('UA', 'EMEA'),('AE', 'EMEA'),('GS', 'EMEA'),('GB', 'EMEA'),('OM', 'EMEA'),('NO', 'EMEA'),('SN', 'EMEA'),('SS', 'EMEA'),('SC', 'EMEA'),('EH', 'EMEA'),('ZA', 'EMEA'),('SO', 'EMEA'),('NG', 'EMEA'),('SL', 'EMEA'),('RS', 'EMEA'),('SY', 'EMEA'),('ES', 'EMEA'),('TZ', 'EMEA'),('CH', 'EMEA'),('SH', 'EMEA'),('SE', 'EMEA'),('RW', 'EMEA'),('RU', 'EMEA'),('SZ', 'EMEA'),('TG', 'EMEA'),('SJ', 'EMEA'),('SA', 'EMEA'),('RO', 'EMEA'),('SD', 'EMEA'),('RE', 'EMEA'),('QA', 'EMEA'),('SM', 'EMEA'),('PT', 'EMEA'),('PL', 'EMEA'),('ST', 'EMEA'),('TN', 'EMEA'),('TR', 'EMEA'),('SK', 'EMEA'),('SI', 'EMEA'),('LB', 'EMEA'),('nan', 'EMEA'),('KM', 'EMEA'),('CD', 'EMEA'),('CG', 'EMEA'),('CI', 'EMEA'),('HR', 'EMEA'),('CY', 'EMEA'),('CZ', 'EMEA'),('DK', 'EMEA'),('TD', 'EMEA'),('DJ', 'EMEA'),('GQ', 'EMEA'),('ER', 'EMEA'),('EE', 'EMEA'),('ET', 'EMEA'),('FK', 'EMEA'),('FO', 'EMEA'),('FI', 'EMEA'),('FR', 'EMEA'),('EG', 'EMEA'),('CF', 'EMEA'),('CV', 'EMEA'),('CM', 'EMEA'),('AF', 'EMEA'),('AX', 'EMEA'),('AL', 'EMEA'),('DZ', 'EMEA'),('AD', 'EMEA'),('AO', 'EMEA'),('AM', 'EMEA'),('AT', 'EMEA'),('AZ', 'EMEA'),('BH', 'EMEA'),('BY', 'EMEA'),('BE', 'EMEA'),('BJ', 'EMEA'),('BA', 'EMEA'),('BW', 'EMEA'),('BV', 'EMEA'),('BG', 'EMEA'),('BF', 'EMEA'),('BI', 'EMEA'),('GA', 'EMEA'),('GM', 'EMEA'),('GE', 'EMEA'),('DE', 'EMEA'),('LS', 'EMEA'),('LR', 'EMEA'),('LY', 'EMEA'),('LI', 'EMEA'),('LT', 'EMEA'),('LU', 'EMEA'),('MK', 'EMEA'),('MG', 'EMEA'),('MW', 'EMEA'),('ML', 'EMEA'),('MT', 'EMEA'),('MR', 'EMEA'),('MU', 'EMEA'),('YT', 'EMEA'),('MD', 'EMEA'),('MC', 'EMEA'),('ME', 'EMEA'),('MA', 'EMEA'),('MZ', 'EMEA'),('ZM', 'EMEA'),('NL', 'EMEA'),('LV', 'EMEA'),('KE', 'EMEA'),('GH', 'EMEA'),('GI', 'EMEA'),('GR', 'EMEA'),('GL', 'EMEA'),('GG', 'EMEA'),('GN', 'EMEA'),('GW', 'EMEA'),('VA', 'EMEA'),('HU', 'EMEA'),('IS', 'EMEA'),('IR', 'EMEA'),('IQ', 'EMEA'),('IE', 'EMEA'),('IM', 'EMEA'),('IL', 'EMEA'),('IT', 'EMEA'),('JE', 'EMEA'),('JO', 'EMEA'),('KZ', 'EMEA'),('KW', 'EMEA'),('ZW', 'EMEA'))
v on account.country_code=v.column1
 GROUP BY region) t4
ON t3.region=t4.region ORDER BY region;

-- STORES INCOME
SELECT app_store_id, SUM(iap_price_usd_cents + 0.0) / 100 AS income
FROM iap_purchase GROUP BY app_store_id ORDER BY income;

-- NUMBER OF USERS PER COUNTRY
WITH top_countries AS (SELECT ROW_NUMBER() OVER (ORDER BY account_number DESC) AS place, country_code, account_number
FROM (SELECT country_code, COUNT(account_id) AS account_number FROM account GROUP BY country_code ORDER BY account_number DESC))
SELECT country_code, account_number FROM top_countries WHERE place < 30
UNION ALL
SELECT 'Other', SUM(account_number) FROM top_countries WHERE place >= 30
ORDER BY account_number;

-- REVENUE PER COUNTRY
WITH top_countries AS (SELECT ROW_NUMBER() OVER (ORDER BY total DESC) AS place, country_code, total
FROM (SELECT a.country_code, ROUND(SUM(ip.income) / 100, 0) as total FROM (SELECT country_code, account_id FROM account) a
LEFT JOIN  (SELECT account_id, SUM(iap_price_usd_cents) + 0.0 as income FROM iap_purchase GROUP BY account_id) ip
ON a.account_id=ip.account_id
GROUP BY country_code ORDER BY total DESC))
SELECT country_code, total FROM top_countries WHERE place < 20
UNION ALL
SELECT 'Other', SUM(total) FROM top_countries WHERE place >= 20
ORDER BY total;

-- REVENUE TRENDS
SELECT STRFTIME("%Y-%m-%d", created_time) as date, ROUND(SUM(iap_price_usd_cents + 0.0) / 100, 2) as count FROM iap_purchase GROUP BY STRFTIME(\"%Y-%m-%d\", created_time) ORDER BY date;

-----------------
-- STORE ANALYSES
-----------------

-- NUMBER OF USERS PER STORE WITH PLATFORM
SELECT created_app_store_id AS store, GROUP_CONCAT(DISTINCT created_platform) AS platforms, COUNT(*) AS count
FROM account GROUP BY store ORDER BY count DESC;

-- TRANSACTIONS PER STORE (WITH CAPACITY)
SELECT app_store_id AS store, COUNT(*) AS `number of transactions`, ROUND(SUM(iap_price_usd_cents) / 100., 2) AS `total amount`
FROM iap_purchase GROUP BY store ORDER BY `total amount` DESC;

-- CHINESE PLAYERS DISTRIBUTION BY STORES
SELECT created_app_store_id AS store, COUNT(CASE WHEN country_code = 'CN' THEN 1 END) AS `Chinese accounts`, COUNT(CASE WHEN country_code <> 'CN' THEN 1 END) AS `non-Chinese accounts`
FROM account GROUP BY store;

-- MI STORE DEVISES CHECK
SELECT
  ROUND(CAST(COUNT(
    CASE WHEN created_device
      REGEXP 'MI.*|HM.*|Redmi.*|Mi.*|2013...|2014...'
    THEN 1 END
  ) AS REAL) / COUNT(*), 2) AS 'Xiaomi share'
FROM account WHERE created_app_store_id = 6;

-- OPPO STORE DEVISES CHECK
SELECT
  ROUND(CAST(COUNT(
    CASE WHEN created_device
      REGEXP 'OPPO.*|A11.*|A31.*|A51.*|1105|1107|R[0-9].*|N[0-9].*'
    THEN 1 END
  ) AS REAL) / COUNT(*), 2) AS 'OPPO share'
FROM account WHERE created_app_store_id = 7;

-- HUAWEI STORE DEVISES CHECK
SELECT
  ROUND(CAST(COUNT(
    CASE WHEN created_device
      REGEXP 'HUAWEI.*|CHE-.*|Che.*|SCL-.*|KIW-.*
        |CHM-.*|PLK-.*|H60-.*|ALE-.*|PE-.*'
    THEN 1 END
  ) AS REAL) / COUNT(*), 2) AS 'Huawei share'
FROM account WHERE created_app_store_id = 8;

-- LENOVO LESTORE STORE DEVISES CHECK
SELECT
  ROUND(CAST(COUNT(
    CASE WHEN created_device
      REGEXP 'Lenovo.*|ZUK.*|YOGA.*|XT.*'
    THEN 1 END
  ) AS REAL) / COUNT(*), 2) AS 'Lenovo and Motorola share'
FROM account WHERE created_app_store_id = 11;

-- VIVO STORE DEVISES CHECK
SELECT
  ROUND(CAST(COUNT(
    CASE WHEN created_device
      REGEXP 'vivo.*'
    THEN 1 END
  ) AS REAL) / COUNT(*), 2) AS 'VIVO share'
FROM account WHERE created_app_store_id = 16;

-- STORE EARLIEST AND LATEST TRANSACTION DATE
SELECT
  app_store_id AS store,
  DATE(MIN(created_time)) AS earliest_purchase,
  DATE(MAX(created_time)) AS latest_purchase
FROM iap_purchase GROUP BY app_store_id ORDER BY earliest_purchase;

-- EARLIEST AND LATEST TRANSACTION DATE BY PACKAGE
SELECT
  package_id_hash AS package,
  DATE(MIN(created_time)) AS earliest_purchase,
  DATE(MAX(created_time)) AS latest_purchase
FROM iap_purchase GROUP BY package_id_hash ORDER BY earliest_purchase;

