class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = [int(version) for version in version1.split('.')]
        version2 = [int(version) for version in version2.split('.')]
        

        for v1, v2 in zip(version1, version2):
            if v1 > v2: return 1
            if v2 > v1: return -1

        if len(version1) > len(version2):
            if any(version1[len(version2):]): return 1 
        if len(version1) < len(version2):
            if any(version2[len(version1):]): return -1
        return 0

        
