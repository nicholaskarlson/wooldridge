def load():
    """name of dataset: countymurders
    no of variables: 20
    no of observations: 37349

    +-------------+------------------------------------------------+
    | variable    | label                                          |
    +-------------+------------------------------------------------+
    | arrests     | # of murder arrests                            |
    | countyid    | county identifier: 1000*statefips + countyfips |
    | density     | population density; per square mile            |
    | popul       | county population                              |
    | perc1019    | percent pop. age 10-19                         |
    | perc2029    | percent pop. age 20-29                         |
    | percblack   | percent population black                       |
    | percmale    | percent population male                        |
    | rpcincmaint | real per capita income maintenance             |
    | rpcpersinc  | real per capita personal income                |
    | rpcunemins  | real per capita unem insurance payments        |
    | year        | 1980-1996                                      |
    | murders     | # of murders                                   |
    | murdrate    | murders per 10000 people                       |
    | arrestrate  | murder arrests per 10000                       |
    | statefips   | state FIPS code                                |
    | countyfips  | county FIPS code                               |
    | execs       | # of executions                                |
    | lpopul      | log(popul)                                     |
    | execrate    | executions per 10000                           |
    +-------------+------------------------------------------------+

    Compiled by J. Monroe Gamble for a Summer Research Opportunities
    Program (SROP) at Michigan State University, Summer 2014. Monroe
    obtained data from the U.S. Census Bureau, the FBI Uniform Crime
    Reports, and the Death Penalty Information Center."""

    import wooldridge
    return wooldridge.load(__file__, "countymurders.csv.bz2")


def wooldridge():
    import wooldridge
    return wooldridge.dataset_list()