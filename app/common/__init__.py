import argparse
import logging
import os

__version__ = "0.1.0"
FORMAT = '%(asctime)-15s-[%(levelname)s]-%(module)s-%(filename)s:%(lineno)d-%(message)s'
_logger = logging.getLogger(__name__)
parser = argparse.ArgumentParser(parents=[])
parser.add_argument(
    '-H', '--host', dest='host', default=os.environ.get('HOST', 'localhost'),
    metavar='HOST', help='set database host and port, e.g., postgres.example.com:5432. default: localhost')
parser.add_argument(
    '-P', '--port', dest='port', default=os.environ.get('PORT', '5433'),
    metavar='PORT', help='set database host and port, e.g., postgres.example.com:5432. default: 5432')
parser.add_argument(
    '-u', '--user', dest='user', default=os.environ.get('USER', 'postgres'),
    metavar='USER', help='set database user, default: change-user')
parser.add_argument(
    '-p', '--password', dest='password', default=os.environ.get('PASSWORD', 'postgres'),
    metavar='PASSWORD', help='set database password, default: change-password')
parser.add_argument(
    '-d', '--database', dest='database', default=os.environ.get('DATABASE', 'esf'),
    metavar='DATABASE', help='set a database to store data, default: esf')

args = parser.parse_args()
print('----args --- ', args)
logging.basicConfig(level=logging.DEBUG, format=FORMAT)

