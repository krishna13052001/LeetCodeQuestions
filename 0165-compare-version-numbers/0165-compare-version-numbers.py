class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split(".")
        ver2 = version2.split(".")
        idx = 0
        while idx < len(ver1) and idx < len(ver2):
            print(int(ver1[idx]), int(ver2[idx]), int(ver1[idx]) > int(ver2[idx]))
            if int(ver1[idx]) < int(ver2[idx]):
                return -1
            elif int(ver1[idx]) > int(ver2[idx]):
                return 1
            else:
                idx += 1
        while idx < len(ver1):
            if int(ver1[idx]):
                return 1
            idx += 1
        while idx < len(ver2):
            if int(ver2[idx]):
                return -1
            idx += 1
        return 0