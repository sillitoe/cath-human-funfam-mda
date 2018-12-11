# Retrieve Human CATH FunFam sequences

This contains a script that retrieves the FunFam entries in human for a given release of CATH and outputs the data in tab-separated format.

## Requirements

 * local access to CATH Oracle database
 * `python3`
 * `cx_Oracle` (guide to installing can be found [here](https://gist.github.com/kimus/10012910))

## Usage

Defaults should do something sensible:

```
./script/cath-human-funfam-mda.py > output.tsv
```

Run on a different version of CATH (requires this database to exist...):

```
./script/cath-human-funfam-mda.py --dbname cath_v4_3_0
```

## Changes

This script essentially just provides a wrapper around SQL located in the file:

[`sql/cath-human-funfam-mda.sql`](sql/cath-human-funfam-mda.sql)

Making changes to this file should do pretty much what you expect.
