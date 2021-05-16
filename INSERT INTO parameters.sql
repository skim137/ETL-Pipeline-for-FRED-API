/*
Desc: Sample API parameter values for new users

Last updated: 2021-05-16
Author: http://www.github.com/skim137
*/

INSERT INTO parameters (series_desc, series_id, observation_start, units, frequency, aggregation_method)
VALUES
    ('CPI Index_yoy', 'CPIAUCSL', '2020-01-01', 'pc1', NULL, NULL),
    ('Real GDP', 'A191RL1Q225SBEA', '2020-01-01', NULL, NULL, NULL),
    ('Industrial Prod', 'INDPRO', '2020-01-01', 'pch', NULL, NULL),
    ('UST 10Y_mavg', 'DGS10', '2020-01-01', NULL, 'm', 'avg'),
    ('EURUSD_mavg', 'DEXUSEU', '2020-01-01', NULL, 'm', 'avg'),
    ('Unemployment Rate', 'UNRATE', '2020-01-01', NULL, NULL, NULL),
    ('Nonfarm Payroll', 'PAYEMS', '2020-01-01', 'chg', NULL, NULL),
    ('Initial Claims', 'ICSA', '2020-01-01', NULL, NULL, NULL)