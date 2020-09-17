from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(p: str) -> str:
            if parent[p] != p:
                parent[p] = find(parent[p])
            return parent[p]

        def union(p: str, q: str):
            pRoot, qRoot = find(p), find(q)
            parent[qRoot] = pRoot

        parent, username = {}, {}
        for emails in accounts:
            name, first_email = emails[0], emails[1]
            if first_email not in parent:
                parent[first_email] = first_email
                username[first_email] = name
            for email in emails[2:]:
                if email not in parent:
                    parent[email] = email
                    username[email] = name
                union(first_email, email)

        res_map = {}
        for k, v in parent.items():
            v = find(v)
            if v in res_map:
                res_map[v].append(k)
            else:
                res_map[v] = [k]
        res = []
        for k, v in res_map.items():
            v.sort()
            res.append([username[k]] + v)
        return res


# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
#             ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
accounts = [["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"],
            ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"],
            ["David", "David1@m.co", "David2@m.co"]]

print(Solution().accountsMerge(accounts))
