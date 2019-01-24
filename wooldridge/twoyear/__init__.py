def load():
    """name of dataset: twoyear
    no of variables: 23
    no of observations: 6763

    +----------+---------------------------------+
    | variable | label                           |
    +----------+---------------------------------+
    | female   | =1 if female                    |
    | phsrank  | % high school rank; 100 = best  |
    | BA       | =1 if Bachelor's degree         |
    | AA       | =1 if Associate's degree        |
    | black    | =1 if African-American          |
    | hispanic | =1 if Hispanic                  |
    | id       | ID Number                       |
    | exper    | total (actual) work experience  |
    | jc       | total 2-year credits            |
    | univ     | total 4-year credits            |
    | lwage    | log hourly wage                 |
    | stotal   | total standardized test score   |
    | smcity   | =1 if small city, 1972          |
    | medcity  | =1 if med. city, 1972           |
    | submed   | =1 if suburb med. city, 1972    |
    | lgcity   | =1 if large city, 1972          |
    | sublg    | =1 if suburb large city, 1972   |
    | vlgcity  | =1 if very large city, 1972     |
    | subvlg   | =1 if sub. very lge. city, 1972 |
    | ne       | =1 if northeast                 |
    | nc       | =1 if north central             |
    | south    | =1 if south                     |
    | totcoll  | jc + univ                       |
    +----------+---------------------------------+

    T.J. Kane and C.E. Rouse (1995), "Labor-Market Returns to Two- and
    Four-Year Colleges," American Economic Review 85, 600-614. With
    Professor Rouse’s kind assistance, I obtained the data from her web
    site at Princeton University."""

    import wooldridge
    return wooldridge.load(__file__, "twoyear.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()