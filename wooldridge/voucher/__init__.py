def load():
    """name of dataset: voucher
    no of variables: 19
    no of observations: 990

    +------------+----------------------------------------------+
    | variable   | label                                        |
    +------------+----------------------------------------------+
    | studyid    | student identifier                           |
    | black      | = 1 if African-American                      |
    | hispanic   | = 1 if Hispanic                              |
    | female     | = 1 if female                                |
    | appyear    | year of first application: 90 to 93          |
    | mnce       | math NCE test score, 1994                    |
    | select     | = 1 if ever selected to attend choice school |
    | choice     | = 1 if attending choice school, 1994         |
    | selectyrs  | years selected to attend choice school       |
    | choiceyrs  | years attended choice school                 |
    | mnce90     | mnce in 1990                                 |
    | selectyrs1 | = 1 if selectyrs == 1                        |
    | selectyrs2 | = 1 if selectyrs == 2                        |
    | selectyrs3 | = 1 if selectyrs == 3                        |
    | selectyrs4 | = 1 if selectyrs == 4                        |
    | choiceyrs1 | = 1 if choiceyrs == 1                        |
    | choiceyrs2 | = 1 if choiceyrs == 2                        |
    | choiceyrs3 | = 1 if choiceyrs == 3                        |
    | choiceyrs4 | = 1 if choiceyrs == 4                        |
    +------------+----------------------------------------------+

    Rouse, C.E. (1998), “Private School Vouchers and Student Achievement:
    An Evaluation of the Milwaukee Parental Choice Program,” Quarterly
    Journal of Economics 113, 553-602. Professor Rouse kindly provided the
    original data set from her paper."""

    import wooldridge
    return wooldridge.load(__file__, "voucher.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()