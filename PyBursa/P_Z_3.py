import datetime
from datetime import datetime, timedelta

tr_d = '2016-10-20'
print(datetime.strptime('-'.join(tr_d.split('-')),"%Y-%m-%d").date())
print(datetime.strptime('-'.join(tr_d.split('-')),"%Y-%m-%d"))
print(datetime(tr_d).date())