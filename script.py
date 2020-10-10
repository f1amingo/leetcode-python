from collections import Counter

output = ['abbcd', 'abbdc', 'abcbd', 'abcdb', 'abdcb', 'abdbc', 'acbbd', 'acbdb', 'acdbb', 'adbcb', 'adbbc', 'adcbb',
          'babcd', 'babdc', 'bacbd', 'bacdb', 'badcb', 'badbc', 'bbacd', 'bbadc', 'bbcad', 'bbcda', 'bbdca', 'bbdac',
          'bcbad', 'bcbda', 'bcabd', 'bcadb', 'bcdab', 'bcdba', 'bdbca', 'bdbac', 'bdcba', 'bdcab', 'bdacb', 'bdabc',
          'cbbad', 'cbbda', 'cbabd', 'cbadb', 'cbdab', 'cbdba', 'cabbd', 'cabdb', 'cadbb', 'cdbab', 'cdbba', 'cdabb',
          'dbbca', 'dbbac', 'dbcba', 'dbcab', 'dbacb', 'dbabc', 'dcbba', 'dcbab', 'dcabb', 'dabcb', 'dabbc', 'dacbb']

expected = ["abbcd", "abbdc", "abcbd", "abcdb", "abdbc", "abdcb", "acbbd", "acbdb", "acdbb", "adbbc", "adbcb", "adcbb",
            "babcd", "babdc", "bacbd", "bacdb", "badbc", "badcb", "bbacd", "bbadc", "bbcad", "bbcda", "bbdac", "bbdca",
            "bcabd", "bcadb", "bcbad", "bcbda", "bcdab", "bcdba", "bdabc", "bdacb", "bdbac", "bdbca", "bdcab", "bdcba",
            "cabbd", "cabdb", "cadbb", "cbabd", "cbadb", "cbbad", "cbbda", "cbdab", "cbdba", "cdabb", "cdbab", "cdbba",
            "dabbc", "dabcb", "dacbb", "dbabc", "dbacb", "dbbac", "dbbca", "dbcab", "dbcba", "dcabb", "dcbab", "dcbba"]

print(Counter(output))
