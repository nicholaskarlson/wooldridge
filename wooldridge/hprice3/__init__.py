def load():
    """name of dataset: hprice3
    no of variables: 19
    no of observations: 321

    +----------+---------------------------------+
    | variable | label                           |
    +----------+---------------------------------+
    | year     | 1978, 1981                      |
    | age      | age of house                    |
    | agesq    | age^2                           |
    | nbh      | neighborhood, 1-6               |
    | cbd      | dist. to cent. bus. dstrct, ft. |
    | inst     | dist. to interstate, ft.        |
    | linst    | log(inst)                       |
    | price    | selling price                   |
    | rooms    | # rooms in house                |
    | area     | square footage of house         |
    | land     | square footage lot              |
    | baths    | # bathrooms                     |
    | dist     | dist. from house to incin., ft. |
    | ldist    | log(dist)                       |
    | lprice   | log(price)                      |
    | y81      | =1 if year = 1981               |
    | larea    | log(area)                       |
    | lland    | log(land)                       |
    | linstsq  | linst^2                         |
    +----------+---------------------------------+

-"""

    import wooldridge
    return wooldridge.load(__file__, "hprice3.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()