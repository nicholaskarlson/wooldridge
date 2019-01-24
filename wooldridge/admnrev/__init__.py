def load():
    """name of dataset: admnrev
    no of variables: 5
    no of observations: 153

    +----------+--------------------------------+
    | variable | label                          |
    +----------+--------------------------------+
    | state    | state postal code              |
    | year     | 85, 90, or 95                  |
    | admnrev  | =1 if admin. revoc. law        |
    | daysfrst | days suspended, first offense  |
    | daysscnd | days suspended, second offense |
    +----------+--------------------------------+

    Data from the National Highway Traffic Safety Administration: “A
    Digest of State Alcohol-Highway Safety Related Legislation,” U.S.
    Department of Transportation, NHTSA. I used the third (1985), eighth
    (1990), and 13th (1995) editions."""

    import wooldridge
    return wooldridge.load(__file__, "admnrev.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()