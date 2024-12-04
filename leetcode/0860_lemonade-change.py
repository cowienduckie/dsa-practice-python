from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveDollars = 0
        tenDollars = 0

        for bill in bills:
            match bill:
                case 5:
                    fiveDollars += 1
                case 10:
                    if fiveDollars == 0:
                        return False
                    fiveDollars -= 1
                    tenDollars += 1
                case 20:
                    if tenDollars > 0 and fiveDollars > 0:
                        fiveDollars -= 1
                        tenDollars -= 1
                    elif fiveDollars >= 3:
                        fiveDollars -= 3
                    else:
                        return False
        return True
