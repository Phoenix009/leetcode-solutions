class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        store = {}

        def add_subdomain_count(store, count, subdomain):
            if not subdomain: return
            sub = subdomain.pop()

            if sub not in store:
                store[sub] = {"count": 0, "child": {}}

            store[sub]['count'] += count
            add_subdomain_count(store[sub]['child'], count, subdomain)

        def get_counts(store, postfix):
            for sub in store:
                yield f"{store[sub]['count']} {sub}{postfix}"
                yield from get_counts(store[sub]['child'], f".{sub}{postfix}")
            

        for cpdomain in cpdomains:
            count, domain = cpdomain.split()

            count = int(count)
            subdomains = domain.split(".")

            add_subdomain_count(store, count, subdomains)

        return get_counts(store, postfix="")

