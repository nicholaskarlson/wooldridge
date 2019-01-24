def load():
    """name of dataset: alcohol
    no of variables: 33
    no of observations: 9822

    +------------+----------------------------------------------------+
    | variable   | label                                              |
    +------------+----------------------------------------------------+
    | abuse      | =1 if abuse alcohol                                |
    | status     | out of workforce = 1; unemployed = 2, employed = 3 |
    | unemrate   | state unemployment rate                            |
    | age        | age in years                                       |
    | educ       | years of schooling                                 |
    | married    | =1 if married                                      |
    | famsize    | family size                                        |
    | white      | =1 if white                                        |
    | exhealth   | =1 if in excellent health                          |
    | vghealth   | =1 if in very good health                          |
    | goodhealth | =1 if in good health                               |
    | fairhealth | =1 if in fair health                               |
    | northeast  | =1 if live in northeast                            |
    | midwest    | =1 if live in midwest                              |
    | south      | =1 if live in south                                |
    | centcity   | =1 if live in central city of MSA                  |
    | outercity  | =1 if in outer city of MSA                         |
    | qrt1       | =1 if interviewed in first quarter                 |
    | qrt2       | =1 if interviewed in second quarter                |
    | qrt3       | =1 if interviewed in third quarter                 |
    | beertax    | state excise tax, $ per gallon                     |
    | cigtax     | state cigarette tax, cents per pack                |
    | ethanol    | state per-capita ethanol consumption               |
    | mothalc    | =1 if mother an alcoholic                          |
    | fathalc    | =1 if father an alcoholic                          |
    | livealc    | =1 if lived with alcoholic                         |
    | inwf       | =1 if status > 1                                   |
    | employ     | =1 if employed                                     |
    | agesq      | age^2                                              |
    | beertaxsq  | beertax^2                                          |
    | cigtaxsq   | cigtax^2                                           |
    | ethanolsq  | ethanol^2                                          |
    | educsq     | educ^2                                             |
    +------------+----------------------------------------------------+

    Terza, J.V. (2002), “Alcohol Abuse and Employment: A Second Look,”
    Journal of Applied Econometrics 17, 393-404. I obtained these data
    from the Journal of Applied Econometrics data archive at
    http://qed.econ.queensu.ca/jae/."""

    import wooldridge
    return wooldridge.load(__file__, "alcohol.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()