def load():
    """name of dataset: murder
    no of variables: 13
    no of observations: 153

    +----------+--------------------------------+
    | variable | label                          |
    +----------+--------------------------------+
    | id       | state identifier               |
    | state    | postal code                    |
    | year     | 87, 90, or 93                  |
    | mrdrte   | murders per 100,000 people     |
    | exec     | total executions, past 3 years |
    | unem     | annual unem. rate              |
    | d90      | =1 if year == 90               |
    | d93      | =1 if year == 93               |
    | cmrdrte  | mrdrte - mrdrte[_n-1]          |
    | cexec    | exec - exec[_n-1]              |
    | cunem    | unem - unem[_n-1]              |
    | cexec_1  | cexec[_n-1]                    |
    | cunem_1  | cunem[_n-1]                    |
    +----------+--------------------------------+

    From the Statistical Abstract of the United States, 1995 (Tables 310
    and 357), 1992 (Table 289). The execution data originally come from
    the U.S. Bureau of Justice Statistics, Capital Punishment Annual."""

    import wooldridge
    return wooldridge.load(__file__, "murder.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()