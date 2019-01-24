def load():
    """name of dataset: vote2
    no of variables: 26
    no of observations: 186

    +----------+---------------------------------+
    | variable | label                           |
    +----------+---------------------------------+
    | state    | state postal code               |
    | district | U.S. Congressional district     |
    | democ    | =1 if incumbent democrat        |
    | vote90   | inc. share two-party vote, 1990 |
    | vote88   | inc. share two-party vote, 1988 |
    | inexp90  | inc. camp. expends., 1990       |
    | chexp90  | chl. camp. expends., 1990       |
    | inexp88  | inc. camp. expends., 1988       |
    | chexp88  | chl. camp. expends., 1988       |
    | prtystr  | % vote pres., same party, 1988  |
    | rptchall | =1 if a repeat challenger       |
    | tenure   | years in H.R.                   |
    | lawyer   | =1 if law degree                |
    | linexp90 | log(inexp90)                    |
    | lchexp90 | log(chexp90)                    |
    | linexp88 | log(inexp88)                    |
    | lchexp88 | log(chexp88)                    |
    | incshr90 | 100*(inexp90/(inexp90+chexp90)) |
    | incshr88 | 100*(inexp88/(inexp88+chexp88)) |
    | cvote    | vote90 - vote88                 |
    | clinexp  | linexp90 - linexp88             |
    | clchexp  | lchexp90 - lchexp88             |
    | cincshr  | incshr90 - incshr88             |
    | win88    | =1 by definition                |
    | win90    | =1 if inc. wins, 1990           |
    | cwin     | win90 - win88                   |
    +----------+---------------------------------+

    See VOTE1.RAW"""

    import wooldridge
    return wooldridge.load(__file__, "vote2.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()