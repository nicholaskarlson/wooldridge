def load():
    """name of dataset: benefits
    no of variables: 18
    no of observations: 1848

    +------------+----------------------------------------+
    | variable   | label                                  |
    +------------+----------------------------------------+
    | distid     | district identifier                    |
    | schid      | school identifier                      |
    | lunch      | percent eligible, free lunch           |
    | enroll     | school enrollment                      |
    | staff      | staff per 1000 students                |
    | exppp      | expenditures per pupil                 |
    | avgsal     | average teacher salary, $              |
    | avgben     | average teacher non-salary benefits, $ |
    | math4      | percent passing 4th grade math test    |
    | story4     | percent passing 4th grade reading test |
    | bs         | avgben/avgsal                          |
    | lavgsal    | log(avgsal)                            |
    | lenroll    | log(enroll)                            |
    | lstaff     | log(staff)                             |
    | bsbar      | within-district avg of bs              |
    | lunchbar   | within-district avg of lunch           |
    | lenrollbar | within-district avg of lenroll         |
    | lstaffbar  | within-district avg of lstaff          |
    +------------+----------------------------------------+

-"""

    import wooldridge
    return wooldridge.load(__file__, "benefits.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()