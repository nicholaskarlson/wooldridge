def load():
    """name of dataset: pntsprd
    no of variables: 12
    no of observations: 553

    +----------+------------------------------+
    | variable | label                        |
    +----------+------------------------------+
    | favscr   | favored team's score         |
    | undscr   | underdog's score             |
    | spread   | las vegas spread             |
    | favhome  | =1 if favored team at home   |
    | neutral  | =1 if neutral site           |
    | fav25    | =1 if favored team in top 25 |
    | und25    | =1 if underdog in top 25     |
    | fregion  | favorite's region of country |
    | uregion  | underdog's region of country |
    | scrdiff  | favscr - undscr              |
    | sprdcvr  | =1 if spread covered         |
    | favwin   | =1 if favored team wins      |
    +----------+------------------------------+

    Collected by Scott Resnick, a former MSU undergraduate, from various
    newspaper sources."""

    import wooldridge
    return wooldridge.load(__file__, "pntsprd.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()