def load():
    """name of dataset: _401ksubs
    no of variables: 11
    no of observations: 9275

    +----------+------------------------------+
    | variable | label                        |
    +----------+------------------------------+
    | e401k    | =1 if eligble for 401(k)     |
    | inc      | annual income, $1000s        |
    | marr     | =1 if married                |
    | male     | =1 if male respondent        |
    | age      | in years                     |
    | fsize    | family size                  |
    | nettfa   | net total fin. assets, $1000 |
    | p401k    | =1 if participate in 401(k)  |
    | pira     | =1 if have IRA               |
    | incsq    | inc^2                        |
    | agesq    | age^2                        |
    +----------+------------------------------+

    A. Abadie (2003), “Semiparametric Instrumental Variable Estimation of
    Treatment Response Models,” Journal of Econometrics 113, 231-263.
    Professor Abadie kindly provided these data. He obtained them from the
    1991 Survey of Income and Program Participation (SIPP)."""

    import wooldridge
    return wooldridge.load(__file__, "_401ksubs.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()