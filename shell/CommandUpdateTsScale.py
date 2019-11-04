
# created by zhaoliyuan

# update ts_scale in trade database

import pandas as pd
import numpy as np
from sqlalchemy import *
from db import mofangFundInfos
from sqlhelper import database
from sqlhelper.tableToDataframe import toSQL, toDf


def update():

    # load data from fund_infos table in mofang database
    sql = toSQL('base')
    sql = sql.query(fund_infos.fi_code,fund_infos.fi_laste_raise)
    sql = sql.filter(fund_infos.fi_wind_id != '')
    sql = sql.statement
    
    dfNew = toDf(sql, 'base')

    # load data from ts_scale table in trade database
    sql = toSQL('trade')
    sql = sql.query()
    sql = sql.filter()
    sql = sql.statement

    dfOld = toDf(sql, 'trade')

    # update
    database.batch('trade', 'ts_scale', dfNew, dfOld, delete = False, timestamp = True)


if __name__ == '__main__':
    update()

