def load():
    """name of dataset: beveridge
    no of variables: 8
    no of observations: 135

    +----------+----------------------------+
    | variable | label                      |
    +----------+----------------------------+
    | month    | dec 200 through feb 2012   |
    | urate    | unemployment rate, percent |
    | vrate    | vacancy rate, percent      |
    | t        | linear time trend          |
    | urate_1  | L.urate                    |
    | vrate_1  | L.vrate                    |
    | curate   | D.urate                    |
    | cvrate   | D.vrate                    |
    +----------+----------------------------+

-"""

    import wooldridge
    return wooldridge.load(__file__, "beveridge.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()