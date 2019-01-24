def load():
    """name of dataset: fair
    no of variables: 28
    no of observations: 21

    +----------+--------------------------------+
    | variable | label                          |
    +----------+--------------------------------+
    | year     | 1916 to 1992, by 4             |
    | V        | prop. dem. vote                |
    | I        | =1 if demwh, -1 if repwh       |
    | DPER     | incumbent running              |
    | DUR      | duration                       |
    | g3       | avg ann grwth rte, prev 3 qrts |
    | p15      | avg ann inf rate, prev 15 qtrs |
    | n        | quarters of good news          |
    | g2       | avg ann grwth rte, prev 2 qrts |
    | gYR      | ann grwth rte, prev year       |
    | p8       | avg ann inf rate, prev 8 qtrs  |
    | p2YR     | inf rte over 2 yr period       |
    | Ig2      | I*g2                           |
    | Ip8      | I*p8                           |
    | demwins  | =1 if V > .5                   |
    | In       | I*n                            |
    | d        | =1 in 1920, 1944,1948          |
    | Id       | I*d                            |
    | Ig3      | I*g3                           |
    | Ip151md  | I*p15*(1-d)                    |
    | In1md    | I*n*(1-d)                      |
    +----------+--------------------------------+

    R.C. Fair (1996), “Econometrics and Presidential Elections,” Journal
    of Economic Perspectives 10, 89-102. The data set is provided in the
    article."""

    import wooldridge
    return wooldridge.load(__file__, "fair.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()