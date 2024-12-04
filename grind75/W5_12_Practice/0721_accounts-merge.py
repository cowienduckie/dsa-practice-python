from typing import List, Set


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Create a dictionary to store email and its linked accounts
        email_users = dict()
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in email_users:
                    email_users[email] = set()
                email_users[email].add(i)

        # Use DFS to find all connected accounts position in original array
        visited = [False] * len(accounts)

        def dfs(pos: int) -> Set[int]:
            # Check if the current account has been visited
            if visited[pos]:
                return set()
            visited[pos] = True

            # Add current account to linked_users
            connected = set([pos])
            for email in accounts[pos][1:]:
                for next in email_users[email]:
                    connected |= dfs(next)

            return connected

        # Merge connected accounts to a single account and append to ans
        ans = []
        for i, account in enumerate(accounts):
            if visited[i]:
                continue
            # Find all connected accounts and their emails
            connected = dfs(i)
            emails = set()
            for pos in connected:
                emails |= set(accounts[pos][1:])

            # Append connected accounts as a single account
            ans.append([account[0]] + sorted(emails))

        return ans


accounts = [
    ["David", "David0@m.co", "David1@m.co"],
    ["David", "David3@m.co", "David4@m.co"],
    ["David", "David4@m.co", "David5@m.co"],
    ["David", "David2@m.co", "David3@m.co"],
    ["David", "David1@m.co", "David2@m.co"],
]
print(Solution().accountsMerge(accounts))
