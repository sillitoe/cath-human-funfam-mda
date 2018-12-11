#!/usr/bin/env python3

# core
import argparse
import logging
import os

# include
import db_conn

_mypath = os.path.abspath(os.path.dirname(__file__))
_sqlfile = os.path.join(_mypath, "../sql/cath-human-funfam-mda.sql")

parser = argparse.ArgumentParser(
    description="Retrieve human entries of CATH FunFams (including MDA)")

parser.add_argument('--dbname', type=str, default='cath_v4_2_0', dest='tablespace',
    help='database name')

parser.add_argument('--verbose', '-v', required=False, action='count', default=0,
    help='more verbose logging')

parser.add_argument('--sql', default=_sqlfile, dest='sqlfile',
    help='override default sql file')

def format_tsv(flds):
    return "\t".join(['"{}"'.format(f or "NULL") for f in flds]) + "\n"

if __name__ == '__main__':
    args = parser.parse_args()

    loglevel = logging.DEBUG if args.verbose > 0 else logging.INFO
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%y %H:%M:%S', level=loglevel)
    logger = logging.getLogger(__name__)

    with open(args.sqlfile) as f:
        sql = f.read()
        sql = sql.format(tablespace=args.tablespace)

    db = db_conn.connect()
    cur = db.cursor()
    cur.execute(sql)

    hdrs = [h[0] for h in cur.description]

    print(format_tsv([h.upper() for h in hdrs]))
    for row in cur:
        print(format_tsv(row))
