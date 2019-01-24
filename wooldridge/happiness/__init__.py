def load():
    """name of dataset: happiness
    no of variables: 33
    no of observations: 17137

    +-------------+-----------------------------------------+
    | variable    | label                                   |
    +-------------+-----------------------------------------+
    | year        | gss year for this respondent            |
    | workstat    | work force status                       |
    | prestige    | occupational prestige score             |
    | divorce     | ever been divorced or separated         |
    | widowed     | ever been widowed                       |
    | educ        | highest year of school completed        |
    | reg16       | region of residence, age 16             |
    | babies      | household members less than 6 yrs old   |
    | preteen     | household members 6 thru 12 yrs old     |
    | teens       | household members 13 thru 17 yrs old    |
    | income      | total family income                     |
    | region      | region of interview                     |
    | attend      | how often r attends religious services  |
    | happy       | general happiness                       |
    | owngun      | =1 if own gun                           |
    | tvhours     | hours per day watching tv               |
    | vhappy      | =1 if 'very happy'                      |
    | mothfath16  | =1 if live with mother and father at 16 |
    | black       | =1 if black                             |
    | gwbush04    | =1 if voted for G.W. Bush in 2004       |
    | female      | =1 if female                            |
    | blackfemale | black*female                            |
    | gwbush00    | =1 if voted for G.W. Bush in 2000       |
    | occattend   | =1 if attend is 3, 4, or 5              |
    | regattend   | =1 if attend is 6, 7, or 8              |
    | y94         | =1 if year == 1994                      |
    | y96         |                                         |
    | y98         |                                         |
    | y00         |                                         |
    | y02         |                                         |
    | y04         |                                         |
    | y06         | =1 if year == 2006                      |
    | unem10      | =1 if unemployed in last 10 years       |
    +-------------+-----------------------------------------+

-"""

    import wooldridge
    return wooldridge.load(__file__, "happiness.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()