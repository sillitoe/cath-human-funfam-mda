# Retrieve Human CATH FunFam sequences (including MDA info)

This contains a script that retrieves the FunFam entries in human for a given release of CATH.

## Requirements

 * local access to CATH Oracle database
 * `python3`
 * `cx_Oracle` (useful guide to installing this [here](https://gist.github.com/kimus/10012910))

## Usage

Defaults should do something sensible:

```
./script/cath-human-funfam-mda.py > output.tsv
```

Run on a different version of CATH:

```
./script/cath-human-funfam-mda.py --dbname cath_v4_2_0
```

Note: this script essentially just provides a wrapper around SQL located in the file:

[`sql/cath-human-funfam-mda.sql`](sql/cath-human-funfam-mda.sql)

Making changes to this file should do pretty much what you expect.
