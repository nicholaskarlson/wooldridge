def load():
    """name of dataset: engin
    no of variables: 17
    no of observations: 403

    +----------+-----------------------------+
    | variable | label                       |
    +----------+-----------------------------+
    | male     | =1 if male                  |
    | educ     | highest grade completed     |
    | wage     | monthly salary, Thai baht   |
    | swage    | starting wage               |
    | exper    | years on current job        |
    | pexper   | previous experience         |
    | lwage    | log(wage)                   |
    | expersq  | exper^2                     |
    | highgrad | =1 if high school graduate  |
    | college  | =1 if college graduate      |
    | grad     | =1 if some graduate school  |
    | polytech | =1 if a polytech            |
    | highdrop | =1 if no high school degree |
    | lswage   | log(swage)                  |
    | pexpersq | pexper^2                    |
    | mleeduc  | male*educ                   |
    | mleeduc0 | male*(educ - 14)            |
    +----------+-----------------------------+

    Thada Chaisawangwong, a former graduate student at MSU, obtained these
    data for a term project in applied econometrics. They come from the
    Material Requirement Planning Survey carried out in Thailand during
    1998."""

    import wooldridge
    return wooldridge.load(__file__, "engin.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()