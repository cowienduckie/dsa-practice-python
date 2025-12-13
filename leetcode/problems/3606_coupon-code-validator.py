import re
from typing import List

validLines = {"electronics", "grocery", "pharmacy", "restaurant"}
codePattern = re.compile(r"^[A-Za-z0-9_]+$")


class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        return [
            cd
            for _, cd in sorted(
                [
                    (line, cd)
                    for cd, line, active, in zip(code, businessLine, isActive)
                    if active and line in validLines and bool(codePattern.fullmatch(cd))
                ]
            )
        ]
