import pandas as pd
from beSDScraper import *


# engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
#    .format(host=hostname, db=dbname, user=uname, pw=pwd,  use_unicode=True, charset="utf8"))

# sql = "SELECT * FROM v_source_list_agg"
# sql = "Select * from v_data_granular where Indicator_id = 'PRA003'"
# data = pd.read_sql(sql, engine)
# data.to_csv('sbData_pra003.csv')


def main():
    params = getDBConf()
    hostname = params[0]
    dbname = params[1]
    uname = params[2]
    pwd = params[3]
    print(uname)
    return 0


if __name__ == '__main__':
    main()
