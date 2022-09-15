from rich.panel import Panel
from termux_toolkit import *

class CustomBan(Fonts):
    def std(self,choices_st_ : Optional[int] = 0)-> int:
        self.scanp = ".banner/"
        self.choices_st_ = choices_st_

        self.dirp = os.listdir(
                "{}".format(self.scanp)
                )
        startp = self.dirp[self.choices_st_]
        sub = self.subget(
                "cat '{}{}'".format(self.scanp,startp)
        )
        print(Panel(sub))

if __name__ == "__main__":
    st = CustomBan()
