import os
import boto3
import pymysql

rds = boto3.client('rds')
hostname = os.environ['RDS_HOSTNAME']
port = 3306
username = os.environ['RDS_USERNAME']
region = boto3.session.Session().region_name
sslCAFile = os.environ['RDS_SSL_CA_FILE']
dbname = os.environ['RDS_DBNAME']

theToken = rds.generate_db_auth_token(hostname,
                                      port,
                                      username,
                                      region)

print(theToken)

# connect, just to show
dbConn = pymysql.connect(auth_plugin_map={'mysql_cleartext_password':None},
                         user=username,
                         host=hostname,
                         password=theToken,
                         ssl={'ca':sslCAFile},
                         database=dbname)

# eof