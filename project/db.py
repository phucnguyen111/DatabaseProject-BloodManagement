import aiopg.sa
import psycopg2

#__all__ = ['Donor', 'Blood', 'Hospital', 'BloodBank', 'Donor_Donate_Blood',
#           'Blood_Belongs_To_BloodBank', 'BloodBank_ManageInfo_Donor', 'BloodBank_DistributeBlood_Hospital']

async def init_pg(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database = conf['database'],
        user = conf['user'],
        password = conf['password'],
        host = conf['host'],
        port = conf['port'],
        minsize = conf['minsize'],
        maxsize = conf['maxsize']
    )
    app['db'] = engine

async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()
