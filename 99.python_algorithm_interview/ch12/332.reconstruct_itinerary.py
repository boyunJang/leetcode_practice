class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticket_dic = collections.defaultdict(list)
        visited_dic = collections.defaultdict(list)
        for dep, arr in sorted(tickets, key = lambda x:(x[0], x[1])):
            ticket_dic[dep].append(arr)
            visited_dic[dep].append(0)

        route_count = len(tickets) + 1

        def dfs(dep, route):
            print(dep, route)
            if len(route) == route_count:
                return route
            for idx, arr in enumerate(ticket_dic[dep]):
                if visited_dic[dep][idx] != 1:
                    visited_dic[dep][idx] = 1
                    answer = dfs(arr, route + [arr])
                    if len(answer) == route_count:
                        return answer
                    visited_dic[dep][idx] = 0
            return []

        result = []
        result = dfs("JFK", ["JFK"])

        return result