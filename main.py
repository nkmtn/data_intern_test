import sqlite3
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import datetime
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from palettable.scientific.diverging import Vik_15
from palettable.scientific.diverging import Vik_4
import numpy as np


def connect():
    return sqlite3.connect("sample.sqlite")


def dau_plot(con, query, ycoords, name):
    res = con.cursor().execute(query)
    x, y = [], []
    for day, count in res:
        x.append(matplotlib.dates.date2num(datetime.strptime(day, '%Y-%m-%d')))
        y.append(count)

    plt.figure().set_figwidth(20)
    base_template(pd.Series(y, index=x), ycoords, '', "img/dau_%s.png" % name)


# https://python-graph-gallery.com/web-stacked-line-chart-with-labels/
def stacked_line_chart(con, query, filename):
    df = pd.read_sql_query(
        query,
        con,
        parse_dates={'date': '%Y-%m-%d'}
    )

    pivot_df = df.pivot(index='date', columns='store', values='count')
    pivot_df = pivot_df.cumsum()

    plt.figure(figsize=(6, 6))
    plt.stackplot(pivot_df.index,
                  pivot_df.values.T,
                  labels=pivot_df.columns,
                  colors=Vik_15.hex_colors)
    plt.legend(loc='upper left')
    plt.savefig(filename)


def dotted_cross(ycoords):
    dotted_vertical()
    dotted_horizontal(ycoords)


def dotted_horizontal(ycoords):
    for yc in ycoords:
        plt.axhline(y=yc, color='black', linestyle='dotted')


def dotted_vertical(xcoords=None):
    if xcoords is None:
        xcoords = generate_timeline()
    for xc in xcoords:
        plt.axvline(x=xc, color='black', linestyle='dotted')


def base_template(df, ycoords, style, name):
    ax = plt.gca()
    ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator())
    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%b'))
    plt.yticks(fontsize=16)
    plt.xticks(fontsize=16)

    df.plot(style=style, linewidth=3)

    # dotted_cross(ycoords)
    dotted_horizontal(ycoords)

    xcoords = generate_timeline()
    print(xcoords)
    for xc in xcoords:
        plt.axvline(x=xc, color='black', linestyle='dotted')

    plt.xlabel('')
    plt.savefig(name)
    plt.show()


def find_trend(con, query, name, yticks):
    data_orig = pd.read_sql_query(query, con, parse_dates={'date': '%Y-%m-%d'})
    data_orig.set_index('date', inplace=True)

    analysis = data_orig[['count']].copy()

    decompose_result_mult = seasonal_decompose(analysis, model="multiplicative")

    plt.figure().set_figwidth(30)
    base_template(decompose_result_mult.trend, yticks[0], '', "img/trend_%s.png" % name)
    # base_template(decompose_result_mult.seasonal, yticks[1], '', "img/seasonal_%s.png" % name)
    # base_template(decompose_result_mult.resid, yticks[2], '.', "img/resid_%s.png" % name)


def donut_plot(con, query, items_name, name):
    res = con.cursor().execute(query)

    names, size_of_groups = [], []
    for n, i in res:
        names.append("%s: %s%d %s" % (n, items_name[0], i, items_name[1]))
        size_of_groups.append(i)

    plt.figure(figsize=(20, 20))
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["axes.labelweight"] = "bold"
    plt.pie(
        size_of_groups,
        labels=names,
        colors=Vik_4.hex_colors,
        wedgeprops={'linewidth': 3, 'edgecolor': 'white'},
        labeldistance=1.15,
        textprops={'fontsize': 20}
    )

    # make the pie into a donut
    plt.gcf().gca().add_artist(plt.Circle((0, 0), 0.7, color='white'))
    plt.savefig("img/donut_%s.png" % name)
    plt.show()


def horizontal_barplot(con, query, name, label, xtick):
    res = con.cursor().execute(query)

    names, size_of_groups = [], []
    for n, i in res:
        names.append(n)
        size_of_groups.append(i)

    y_pos = np.arange(len(names))

    plt.figure(figsize=(20, 20))
    plt.rcParams['font.size'] = '18'
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["axes.labelweight"] = "bold"

    for index, value in enumerate(size_of_groups):
        plt.text(value, index, "   %s%d" % (label, value))

    plt.barh(y_pos, size_of_groups)
    plt.yticks(y_pos, names)
    plt.xticks(xtick)

    dotted_vertical(xtick)
    plt.savefig("img/horiz_barplot_%s.png" % name)
    plt.show()


def generate_timeline():
    timeline = []
    for a in range(1, 14):
        if a == 13:
            timeline.append(datetime.strptime('2017-01-01', '%Y-%m-%d'))
            continue
        if a > 9:
            timeline.append(datetime.strptime('2016-%d-01' % a, '%Y-%m-%d'))
            continue
        timeline.append(datetime.strptime('2016-0%d-01' % a, '%Y-%m-%d'))
    return timeline


con = connect()


def revenue_per_store_plot(con, all=None):
    res = con.cursor().execute("SELECT DISTINCT created_app_store_id FROM account GROUP BY created_app_store_id;")
    stores = [r[0] for r in res]

    lines = []
    for i in stores:
        query = """SELECT STRFTIME("%m-%Y", created_time) AS created_time, ROUND(SUM(iap_price_usd_cents + 0.0) / 100)
                as income from iap_purchase WHERE app_store_id = '""" \
                + str(i) \
                + """' GROUP BY STRFTIME("%m-%Y", created_time);"""

        res = con.cursor().execute(query)

        days, size_of_groups = [], []
        for day, s in res:
            days.append(matplotlib.dates.date2num(datetime.strptime(day, '%m-%Y')))
            size_of_groups.append(s)
        lines.append([days, size_of_groups])

    plt.figure(figsize=(20, 20)) if all is None else plt.figure(figsize=(20, 10))
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["axes.labelweight"] = "bold"
    plt.rcParams["font.size"] = 16
    ax = plt.gca()
    ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator())
    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%b'))

    start = 1 if all is None else 0
    for i in range(start, len(stores)):
        plt.plot(lines[i][0], lines[i][1], label="store #%d" % stores[i], marker='o')

    plt.legend(loc='upper right')

    yticks = np.arange(0, 1_600, 200) if all is None else np.arange(0, 6_000, 1000)
    dotted_horizontal(yticks)

    dotted_vertical(lines[1][0]) if all is None else dotted_vertical()
    name = "img/revenue_per_store_without_0.png" if all is None else "img/revenue_per_store_all.png"
    plt.savefig(name)
    plt.show()


def revenue_plot(con, query, ycoords):
    res = con.cursor().execute(query)
    x, y = [], []
    for day, count in res:
        x.append(matplotlib.dates.date2num(datetime.strptime(day, '%Y-%m-%d')))
        y.append(count)

    plt.figure(figsize=(20, 10))
    base_template(pd.Series(y, index=x), ycoords, '', "img/store_revenue.png")


########## TRENDS ##########


# General
find_trend(
    con,
    """SELECT date, COUNT(*) AS count FROM account_date_session
     LEFT JOIN account ON account.account_id=account_date_session.account_id
     GROUP BY date;""",
    "general",
    [np.arange(1_500, 5_500, 500), np.arange(0.97, 1.05, 0.01), np.arange(0.92, 1.075, 0.02)]
)

# APAC
find_trend(
    con,
    """SELECT date, COUNT(*) AS count FROM account_date_session
     LEFT JOIN account on account.account_id=account_date_session.account_id
     WHERE account.country_code IN ('MH', 'IN', 'HK', 'MO', 'HM', 'PW', 'MM', 'MV', 'PG', 'GU', 'NR', 'NP', 'ID', 'WS', 'KR', 'KG', 'SG', 'MN', 'NF', 'MP', 'PN', 'MY', 'FM', 'JP', 'PK', 'LA', 'KI', 'KV', 'NU', 'PH', 'TF', 'CC', 'CK', 'TL', 'TK', 'CX', 'CN', 'TO', 'KH', 'TM', 'TV', 'BN', 'IO', 'BT', 'UM', 'BD', 'UZ', 'VU', 'AU', 'AQ', 'VN', 'AS', 'WF', 'TH', 'TJ', 'NC', 'FJ', 'LK', 'PF', 'NZ', 'TW', 'SB')
     GROUP BY date;""",
    "APAC",
    [np.arange(500, 4_000, 500), np.arange(0.96, 1.07, 0.02), np.arange(0.9, 1.2, 0.05)]
)

# EMEA
find_trend(
    con,
    """SELECT date, COUNT(*) AS count FROM account_date_session
     LEFT JOIN account on account.account_id=account_date_session.account_id
     WHERE account.country_code IN ('NE', 'UG', 'YE', 'PS', 'UA', 'AE', 'GS', 'GB', 'OM', 'NO', 'SN', 'SS', 'SC', 'EH', 'ZA', 'SO', 'NG', 'SL', 'RS', 'SY', 'ES', 'TZ', 'CH', 'SH', 'SE', 'RW', 'RU', 'SZ', 'TG', 'SJ', 'SA', 'RO', 'SD', 'RE', 'QA', 'SM', 'PT', 'PL', 'ST', 'TN', 'TR', 'SK', 'SI', 'LB', 'KM', 'CD', 'CG', 'CI', 'HR', 'CY', 'CZ', 'DK', 'TD', 'DJ', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FO', 'FI', 'FR', 'EG', 'CF', 'CV', 'CM', 'AF', 'AX', 'AL', 'DZ', 'AD', 'AO', 'AM', 'AT', 'AZ', 'BH', 'BY', 'BE', 'BJ', 'BA', 'BW', 'BV', 'BG', 'BF', 'BI', 'GA', 'GM', 'GE', 'DE', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MK', 'MG', 'MW', 'ML', 'MT', 'MR', 'MU', 'YT', 'MD', 'MC', 'ME', 'MA', 'MZ', 'ZM', 'NL', 'LV', 'KE', 'GH', 'GI', 'GR', 'GL', 'GG', 'GN', 'GW', 'VA', 'HU', 'IS', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JE', 'JO', 'KZ', 'KW', 'ZW')
     GROUP BY date;""",
    "EMEA",
    [np.arange(800, 1_700, 200), np.arange(0.97, 1.04, 0.01), np.arange(0.9, 1.2, 0.05)]
)

# NA
find_trend(
    con,
    """SELECT date, COUNT(*) AS count FROM account_date_session
     LEFT JOIN account on account.account_id=account_date_session.account_id
     WHERE account.country_code IN ('CA', 'US')
    GROUP BY date;""",
    "NA",
    [np.arange(300, 700, 50), np.arange(0.97, 1.04, 0.01), np.arange(0.9, 1.2, 0.05)]
)

# LATAM
find_trend(
    con,
    """SELECT date, COUNT(*) AS count FROM account_date_session
     LEFT JOIN account on account.account_id=account_date_session.account_id
     WHERE account.country_code IN ('PY', 'PE', 'KY', 'TT', 'CL', 'PR', 'CO', 'BL', 'CR', 'JM', 'CU', 'CW', 'KN', 'TC', 'LC', 'PM', 'DM', 'DO', 'EC', 'VC', 'SV', 'SR', 'HN', 'HT', 'GY', 'GF', 'GT', 'GP', 'GD', 'MF', 'PA', 'SX', 'BR', 'NI', 'VI', 'VG', 'MS', 'AI', 'AG', 'AR', 'VE', 'AW', 'BS', 'BB', 'MX', 'BZ', 'UY', 'BQ', 'BO', 'MQ', 'BM')
    GROUP BY date;""",
    "LATAM",
    [np.arange(200, 325, 25), np.arange(0.98, 1.02, 0.005), np.arange(0.9, 1.2, 0.05)]
)

# Revenue trends
find_trend(
    connect(),
    "SELECT STRFTIME(\"%Y-%m-%d\", created_time) as date, ROUND(SUM(iap_price_usd_cents + 0.0) / 100, 2) as count FROM iap_purchase GROUP BY STRFTIME(\"%Y-%m-%d\", created_time) ORDER BY date;",
    'revenue',
    [np.arange(100, 600, 100)],
)

######### DAU ##########

# General
dau_plot(
    con,
    "SELECT date, COUNT(*) FROM account_date_session GROUP BY date;",
    np.arange(1000, 6000, 1000),
    "general"
)

# Daily active APAC users 2016
dau_plot(
    con,
    """SELECT date, COUNT(*) FROM account_date_session
    LEFT JOIN account on account.account_id=account_date_session.account_id
    WHERE account.country_code IN ('MH', 'IN', 'HK', 'MO', 'HM', 'PW', 'MM', 'MV', 'PG', 'GU', 'NR', 'NP', 'ID', 'WS', 'KR', 'KG', 'SG', 'MN', 'NF', 'MP', 'PN', 'MY', 'FM', 'JP', 'PK', 'LA', 'KI', 'KV', 'NU', 'PH', 'TF', 'CC', 'CK', 'TL', 'TK', 'CX', 'CN', 'TO', 'KH', 'TM', 'TV', 'BN', 'IO', 'BT', 'UM', 'BD', 'UZ', 'VU', 'AU', 'AQ', 'VN', 'AS', 'WF', 'TH', 'TJ', 'NC', 'FJ', 'LK', 'PF', 'NZ', 'TW', 'SB')
    GROUP BY date;""",
    np.arange(500, 3500, 500),
    "APAC"
)

# Daily active EMEA users 2016
dau_plot(
    con,
    """SELECT date, COUNT(*) FROM account_date_session
    LEFT JOIN account on account.account_id=account_date_session.account_id
    WHERE account.country_code IN ('NE', 'UG', 'YE', 'PS', 'UA', 'AE', 'GS', 'GB', 'OM', 'NO', 'SN', 'SS', 'SC', 'EH', 'ZA', 'SO', 'NG', 'SL', 'RS', 'SY', 'ES', 'TZ', 'CH', 'SH', 'SE', 'RW', 'RU', 'SZ', 'TG', 'SJ', 'SA', 'RO', 'SD', 'RE', 'QA', 'SM', 'PT', 'PL', 'ST', 'TN', 'TR', 'SK', 'SI', 'LB', 'KM', 'CD', 'CG', 'CI', 'HR', 'CY', 'CZ', 'DK', 'TD', 'DJ', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FO', 'FI', 'FR', 'EG', 'CF', 'CV', 'CM', 'AF', 'AX', 'AL', 'DZ', 'AD', 'AO', 'AM', 'AT', 'AZ', 'BH', 'BY', 'BE', 'BJ', 'BA', 'BW', 'BV', 'BG', 'BF', 'BI', 'GA', 'GM', 'GE', 'DE', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MK', 'MG', 'MW', 'ML', 'MT', 'MR', 'MU', 'YT', 'MD', 'MC', 'ME', 'MA', 'MZ', 'ZM', 'NL', 'LV', 'KE', 'GH', 'GI', 'GR', 'GL', 'GG', 'GN', 'GW', 'VA', 'HU', 'IS', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JE', 'JO', 'KZ', 'KW', 'ZW')
    GROUP BY date;""",
    np.arange(400, 1_900, 200),
    "EMEA"
)

# Daily active NA users 2016
dau_plot(
    con,
    """SELECT date, COUNT(*) FROM account_date_session
    LEFT JOIN account on account.account_id=account_date_session.account_id
    WHERE account.country_code IN ('CA', 'US')
    GROUP BY date;""",
    np.arange(100, 800, 100),
    "NA"
)

# Daily active LATAM users 2016
dau_plot(
    con,
    """SELECT date, COUNT(*) FROM account_date_session
    LEFT JOIN account on account.account_id=account_date_session.account_id
    WHERE account.country_code IN ('PY', 'PE', 'KY', 'TT', 'CL', 'PR', 'CO', 'BL', 'CR', 'JM', 'CU', 'CW', 'KN', 'TC', 'LC', 'PM', 'DM', 'DO', 'EC', 'VC', 'SV', 'SR', 'HN', 'HT', 'GY', 'GF', 'GT', 'GP', 'GD', 'MF', 'PA', 'SX', 'BR', 'NI', 'VI', 'VG', 'MS', 'AI', 'AG', 'AR', 'VE', 'AW', 'BS', 'BB', 'MX', 'BZ', 'UY', 'BQ', 'BO', 'MQ', 'BM')
    GROUP BY date;""",
    np.arange(100, 300, 50),
    "LATAM"
)

########## DONUT PLOT ##########

# Counts of users per region
donut_plot(
    con,
    """SELECT v.column2 as region, COUNT(account_id) AS users FROM account
    JOIN (VALUES ('PY', 'LATAM'),('PE', 'LATAM'),('CA', 'NA'),('KY', 'LATAM'),('TT', 'LATAM'),('CL', 'LATAM'),('PR', 'LATAM'),('CO', 'LATAM'),('BL', 'LATAM'),('CR', 'LATAM'),('JM', 'LATAM'),('CU', 'LATAM'),('CW', 'LATAM'),('KN', 'LATAM'),('TC', 'LATAM'),('LC', 'LATAM'),('PM', 'LATAM'),('DM', 'LATAM'),('DO', 'LATAM'),('EC', 'LATAM'),('VC', 'LATAM'),('SV', 'LATAM'),('SR', 'LATAM'),('HN', 'LATAM'),('HT', 'LATAM'),('GY', 'LATAM'),('GF', 'LATAM'),('GT', 'LATAM'),('GP', 'LATAM'),('GD', 'LATAM'),('MF', 'LATAM'),('PA', 'LATAM'),('SX', 'LATAM'),('BR', 'LATAM'),('NI', 'LATAM'),('VI', 'LATAM'),('VG', 'LATAM'),('MS', 'LATAM'),('AI', 'LATAM'),('AG', 'LATAM'),('AR', 'LATAM'),('VE', 'LATAM'),('AW', 'LATAM'),('BS', 'LATAM'),('BB', 'LATAM'),('US', 'NA'),('MX', 'LATAM'),('BZ', 'LATAM'),('UY', 'LATAM'),('BQ', 'LATAM'),('BO', 'LATAM'),('MQ', 'LATAM'),('BM', 'LATAM'),('MH', 'APAC'),('IN', 'APAC'),('HK', 'APAC'),('MO', 'APAC'),('HM', 'APAC'),('PW', 'APAC'),('MM', 'APAC'),('MV', 'APAC'),('PG', 'APAC'),('GU', 'APAC'),('NR', 'APAC'),('NP', 'APAC'),('ID', 'APAC'),('WS', 'APAC'),('KR', 'APAC'),('KG', 'APAC'),('SG', 'APAC'),('MN', 'APAC'),('NF', 'APAC'),('MP', 'APAC'),('PN', 'APAC'),('MY', 'APAC'),('FM', 'APAC'),('JP', 'APAC'),('PK', 'APAC'),('LA', 'APAC'),('KI', 'APAC'),('KV', 'APAC'),('NU', 'APAC'),('PH', 'APAC'),('TF', 'APAC'),('CC', 'APAC'),('CK', 'APAC'),('TL', 'APAC'),('TK', 'APAC'),('CX', 'APAC'),('CN', 'APAC'),('TO', 'APAC'),('KH', 'APAC'),('TM', 'APAC'),('TV', 'APAC'),('BN', 'APAC'),('IO', 'APAC'),('BT', 'APAC'),('UM', 'APAC'),('BD', 'APAC'),('UZ', 'APAC'),('VU', 'APAC'),('AU', 'APAC'),('AQ', 'APAC'),('VN', 'APAC'),('AS', 'APAC'),('WF', 'APAC'),('TH', 'APAC'),('TJ', 'APAC'),('NC', 'APAC'),('FJ', 'APAC'),('LK', 'APAC'),('PF', 'APAC'),('NZ', 'APAC'),('TW', 'APAC'),('SB', 'APAC'),('NE', 'EMEA'),('UG', 'EMEA'),('YE', 'EMEA'),('PS', 'EMEA'),('UA', 'EMEA'),('AE', 'EMEA'),('GS', 'EMEA'),('GB', 'EMEA'),('OM', 'EMEA'),('NO', 'EMEA'),('SN', 'EMEA'),('SS', 'EMEA'),('SC', 'EMEA'),('EH', 'EMEA'),('ZA', 'EMEA'),('SO', 'EMEA'),('NG', 'EMEA'),('SL', 'EMEA'),('RS', 'EMEA'),('SY', 'EMEA'),('ES', 'EMEA'),('TZ', 'EMEA'),('CH', 'EMEA'),('SH', 'EMEA'),('SE', 'EMEA'),('RW', 'EMEA'),('RU', 'EMEA'),('SZ', 'EMEA'),('TG', 'EMEA'),('SJ', 'EMEA'),('SA', 'EMEA'),('RO', 'EMEA'),('SD', 'EMEA'),('RE', 'EMEA'),('QA', 'EMEA'),('SM', 'EMEA'),('PT', 'EMEA'),('PL', 'EMEA'),('ST', 'EMEA'),('TN', 'EMEA'),('TR', 'EMEA'),('SK', 'EMEA'),('SI', 'EMEA'),('LB', 'EMEA'),('nan', 'EMEA'),('KM', 'EMEA'),('CD', 'EMEA'),('CG', 'EMEA'),('CI', 'EMEA'),('HR', 'EMEA'),('CY', 'EMEA'),('CZ', 'EMEA'),('DK', 'EMEA'),('TD', 'EMEA'),('DJ', 'EMEA'),('GQ', 'EMEA'),('ER', 'EMEA'),('EE', 'EMEA'),('ET', 'EMEA'),('FK', 'EMEA'),('FO', 'EMEA'),('FI', 'EMEA'),('FR', 'EMEA'),('EG', 'EMEA'),('CF', 'EMEA'),('CV', 'EMEA'),('CM', 'EMEA'),('AF', 'EMEA'),('AX', 'EMEA'),('AL', 'EMEA'),('DZ', 'EMEA'),('AD', 'EMEA'),('AO', 'EMEA'),('AM', 'EMEA'),('AT', 'EMEA'),('AZ', 'EMEA'),('BH', 'EMEA'),('BY', 'EMEA'),('BE', 'EMEA'),('BJ', 'EMEA'),('BA', 'EMEA'),('BW', 'EMEA'),('BV', 'EMEA'),('BG', 'EMEA'),('BF', 'EMEA'),('BI', 'EMEA'),('GA', 'EMEA'),('GM', 'EMEA'),('GE', 'EMEA'),('DE', 'EMEA'),('LS', 'EMEA'),('LR', 'EMEA'),('LY', 'EMEA'),('LI', 'EMEA'),('LT', 'EMEA'),('LU', 'EMEA'),('MK', 'EMEA'),('MG', 'EMEA'),('MW', 'EMEA'),('ML', 'EMEA'),('MT', 'EMEA'),('MR', 'EMEA'),('MU', 'EMEA'),('YT', 'EMEA'),('MD', 'EMEA'),('MC', 'EMEA'),('ME', 'EMEA'),('MA', 'EMEA'),('MZ', 'EMEA'),('ZM', 'EMEA'),('NL', 'EMEA'),('LV', 'EMEA'),('KE', 'EMEA'),('GH', 'EMEA'),('GI', 'EMEA'),('GR', 'EMEA'),('GL', 'EMEA'),('GG', 'EMEA'),('GN', 'EMEA'),('GW', 'EMEA'),('VA', 'EMEA'),('HU', 'EMEA'),('IS', 'EMEA'),('IR', 'EMEA'),('IQ', 'EMEA'),('IE', 'EMEA'),('IM', 'EMEA'),('IL', 'EMEA'),('IT', 'EMEA'),('JE', 'EMEA'),('JO', 'EMEA'),('KZ', 'EMEA'),('KW', 'EMEA'),('ZW', 'EMEA'))
    v on account.country_code=v.column1
    GROUP BY region ORDER BY region;""",
    ["", "users"],
    "count_users_in_region"
)

# Absolute revenue per region
donut_plot(
    con,
    """SELECT t2.region,  ROUND(SUM(t1.sum) / 100, 0) AS income FROM
    (SELECT account_id, SUM(iap_price_usd_cents) + 0.0 as sum FROM iap_purchase GROUP BY account_id) t1
    JOIN
    (SELECT account_id, v.column2 as region FROM account
    JOIN (VALUES ('PY', 'LATAM'),('PE', 'LATAM'),('CA', 'NA'),('KY', 'LATAM'),('TT', 'LATAM'),('CL', 'LATAM'),('PR', 'LATAM'),('CO', 'LATAM'),('BL', 'LATAM'),('CR', 'LATAM'),('JM', 'LATAM'),('CU', 'LATAM'),('CW', 'LATAM'),('KN', 'LATAM'),('TC', 'LATAM'),('LC', 'LATAM'),('PM', 'LATAM'),('DM', 'LATAM'),('DO', 'LATAM'),('EC', 'LATAM'),('VC', 'LATAM'),('SV', 'LATAM'),('SR', 'LATAM'),('HN', 'LATAM'),('HT', 'LATAM'),('GY', 'LATAM'),('GF', 'LATAM'),('GT', 'LATAM'),('GP', 'LATAM'),('GD', 'LATAM'),('MF', 'LATAM'),('PA', 'LATAM'),('SX', 'LATAM'),('BR', 'LATAM'),('NI', 'LATAM'),('VI', 'LATAM'),('VG', 'LATAM'),('MS', 'LATAM'),('AI', 'LATAM'),('AG', 'LATAM'),('AR', 'LATAM'),('VE', 'LATAM'),('AW', 'LATAM'),('BS', 'LATAM'),('BB', 'LATAM'),('US', 'NA'),('MX', 'LATAM'),('BZ', 'LATAM'),('UY', 'LATAM'),('BQ', 'LATAM'),('BO', 'LATAM'),('MQ', 'LATAM'),('BM', 'LATAM'),('MH', 'APAC'),('IN', 'APAC'),('HK', 'APAC'),('MO', 'APAC'),('HM', 'APAC'),('PW', 'APAC'),('MM', 'APAC'),('MV', 'APAC'),('PG', 'APAC'),('GU', 'APAC'),('NR', 'APAC'),('NP', 'APAC'),('ID', 'APAC'),('WS', 'APAC'),('KR', 'APAC'),('KG', 'APAC'),('SG', 'APAC'),('MN', 'APAC'),('NF', 'APAC'),('MP', 'APAC'),('PN', 'APAC'),('MY', 'APAC'),('FM', 'APAC'),('JP', 'APAC'),('PK', 'APAC'),('LA', 'APAC'),('KI', 'APAC'),('KV', 'APAC'),('NU', 'APAC'),('PH', 'APAC'),('TF', 'APAC'),('CC', 'APAC'),('CK', 'APAC'),('TL', 'APAC'),('TK', 'APAC'),('CX', 'APAC'),('CN', 'APAC'),('TO', 'APAC'),('KH', 'APAC'),('TM', 'APAC'),('TV', 'APAC'),('BN', 'APAC'),('IO', 'APAC'),('BT', 'APAC'),('UM', 'APAC'),('BD', 'APAC'),('UZ', 'APAC'),('VU', 'APAC'),('AU', 'APAC'),('AQ', 'APAC'),('VN', 'APAC'),('AS', 'APAC'),('WF', 'APAC'),('TH', 'APAC'),('TJ', 'APAC'),('NC', 'APAC'),('FJ', 'APAC'),('LK', 'APAC'),('PF', 'APAC'),('NZ', 'APAC'),('TW', 'APAC'),('SB', 'APAC'),('NE', 'EMEA'),('UG', 'EMEA'),('YE', 'EMEA'),('PS', 'EMEA'),('UA', 'EMEA'),('AE', 'EMEA'),('GS', 'EMEA'),('GB', 'EMEA'),('OM', 'EMEA'),('NO', 'EMEA'),('SN', 'EMEA'),('SS', 'EMEA'),('SC', 'EMEA'),('EH', 'EMEA'),('ZA', 'EMEA'),('SO', 'EMEA'),('NG', 'EMEA'),('SL', 'EMEA'),('RS', 'EMEA'),('SY', 'EMEA'),('ES', 'EMEA'),('TZ', 'EMEA'),('CH', 'EMEA'),('SH', 'EMEA'),('SE', 'EMEA'),('RW', 'EMEA'),('RU', 'EMEA'),('SZ', 'EMEA'),('TG', 'EMEA'),('SJ', 'EMEA'),('SA', 'EMEA'),('RO', 'EMEA'),('SD', 'EMEA'),('RE', 'EMEA'),('QA', 'EMEA'),('SM', 'EMEA'),('PT', 'EMEA'),('PL', 'EMEA'),('ST', 'EMEA'),('TN', 'EMEA'),('TR', 'EMEA'),('SK', 'EMEA'),('SI', 'EMEA'),('LB', 'EMEA'),('nan', 'EMEA'),('KM', 'EMEA'),('CD', 'EMEA'),('CG', 'EMEA'),('CI', 'EMEA'),('HR', 'EMEA'),('CY', 'EMEA'),('CZ', 'EMEA'),('DK', 'EMEA'),('TD', 'EMEA'),('DJ', 'EMEA'),('GQ', 'EMEA'),('ER', 'EMEA'),('EE', 'EMEA'),('ET', 'EMEA'),('FK', 'EMEA'),('FO', 'EMEA'),('FI', 'EMEA'),('FR', 'EMEA'),('EG', 'EMEA'),('CF', 'EMEA'),('CV', 'EMEA'),('CM', 'EMEA'),('AF', 'EMEA'),('AX', 'EMEA'),('AL', 'EMEA'),('DZ', 'EMEA'),('AD', 'EMEA'),('AO', 'EMEA'),('AM', 'EMEA'),('AT', 'EMEA'),('AZ', 'EMEA'),('BH', 'EMEA'),('BY', 'EMEA'),('BE', 'EMEA'),('BJ', 'EMEA'),('BA', 'EMEA'),('BW', 'EMEA'),('BV', 'EMEA'),('BG', 'EMEA'),('BF', 'EMEA'),('BI', 'EMEA'),('GA', 'EMEA'),('GM', 'EMEA'),('GE', 'EMEA'),('DE', 'EMEA'),('LS', 'EMEA'),('LR', 'EMEA'),('LY', 'EMEA'),('LI', 'EMEA'),('LT', 'EMEA'),('LU', 'EMEA'),('MK', 'EMEA'),('MG', 'EMEA'),('MW', 'EMEA'),('ML', 'EMEA'),('MT', 'EMEA'),('MR', 'EMEA'),('MU', 'EMEA'),('YT', 'EMEA'),('MD', 'EMEA'),('MC', 'EMEA'),('ME', 'EMEA'),('MA', 'EMEA'),('MZ', 'EMEA'),('ZM', 'EMEA'),('NL', 'EMEA'),('LV', 'EMEA'),('KE', 'EMEA'),('GH', 'EMEA'),('GI', 'EMEA'),('GR', 'EMEA'),('GL', 'EMEA'),('GG', 'EMEA'),('GN', 'EMEA'),('GW', 'EMEA'),('VA', 'EMEA'),('HU', 'EMEA'),('IS', 'EMEA'),('IR', 'EMEA'),('IQ', 'EMEA'),('IE', 'EMEA'),('IM', 'EMEA'),('IL', 'EMEA'),('IT', 'EMEA'),('JE', 'EMEA'),('JO', 'EMEA'),('KZ', 'EMEA'),('KW', 'EMEA'),('ZW', 'EMEA'))
    v on account.country_code=v.column1) t2
    ON t1.account_id = t2.account_id
    GROUP BY t2.region ORDER BY region""",
    ["$", ""],
    "absolute_revenue_per_region"
)

# Average revenue per region
donut_plot(
    con,
    """SELECT t3.region as region, ROUND(t3.income / t4.users, 0) AS per_user FROM
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
    ON t3.region=t4.region ORDER BY region;""",
    ["", "¢ per user"],
    "average_revenue_per_region"
)

########## HORIZONTAL BAR PLOT ##########


# store's income
horizontal_barplot(
    con,
    """SELECT app_store_id, SUM(iap_price_usd_cents + 0.0) / 100 AS income
    FROM iap_purchase GROUP BY app_store_id ORDER BY income;""",
    "income_per_store",
    "$",
    np.arange(0, 27_500, 2_500)
)

# users by country
horizontal_barplot(
    con,
    """WITH top_countries AS (SELECT ROW_NUMBER() OVER (ORDER BY account_number DESC) AS place, country_code, account_number
    FROM (SELECT country_code, COUNT(account_id) AS account_number FROM account GROUP BY country_code ORDER BY account_number DESC))
    SELECT country_code, account_number FROM top_countries WHERE place < 30
    UNION ALL
    SELECT 'Other', SUM(account_number) FROM top_countries WHERE place >= 30
    ORDER BY account_number;""",
    "users_country_location",
    "",
    np.arange(0, 45000, 2500)
)

# revenue per country
horizontal_barplot(
    con,
    """WITH top_countries AS (SELECT ROW_NUMBER() OVER (ORDER BY total DESC) AS place, country_code, total
    FROM (SELECT a.country_code, ROUND(SUM(ip.income) / 100, 0) as total FROM (SELECT country_code, account_id FROM account) a
    LEFT JOIN  (SELECT account_id, SUM(iap_price_usd_cents) + 0.0 as income FROM iap_purchase GROUP BY account_id) ip
    ON a.account_id=ip.account_id
    GROUP BY country_code ORDER BY total DESC))
    SELECT country_code, total FROM top_countries WHERE place < 20
    UNION ALL
    SELECT 'Other', SUM(total) FROM top_countries WHERE place >= 20
    ORDER BY total;""",
    "revenue_per_country",
    "$",
    np.arange(0, 17_500, 2_500)
)


########## REVENUE PER STORE ##########

# all stores
revenue_per_store_plot(con, True)

# without store number 0
revenue_per_store_plot(con)

