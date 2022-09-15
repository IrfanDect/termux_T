#!/usr/bin/python3
# created : irfanoid as irfandect

import os,sys,time
from rich import print, box
import subprocess
import inquirer 
from typing import (Optional,
        Callable,
        List,
        Tuple
        )
from rich.table import Table
from rich.live import Live
from rich.columns import Columns

tab = Table(box=box.SQUARE_DOUBLE_HEAD,
        border_style="gray27 bold",
        expand=True,
        highlight=True,
        )
    

class Fonts:
    def __init__(self):
        self.dirs = ".fonts/"
        self.to_dir = "$HOME/.termux/font.ttf"
        self.keys = "cp -r -v"
        self.dirc = ".colors/"
        self.to_dirc = "$HOME/.termux/colors.properties"
        self.banner = ".banner/"
        self.file_banner = ".bashrc"
        self.to_dirb = "$HOME/"
        self.subget = subprocess.getoutput
        self.tabc = tab.add_column
        self.tabr = tab.add_row

    def list_font(self):
        self.listfont = os.listdir('{}'.format(
            self.dirs
            )
        )
        self.tabc("no",
                header_style="blue bold",
            style='cyan'
        )
        self.tabc("list_fonts",
                header_style="blue bold",
            style='green bold'
        )
        try:
            for x , y in enumerate(self.listfont):
                self.tabr("{}".format( int(x)),
                    "{}".format(
                        str(y[:-4])
                    )
                )
            print(tab)
        except ValueError:print("pass")

    def use_font(self, choice_font : Optional[int] )-> int:
        try:
            self.choice_font = int(choice_font)
            self.l = os.listdir('{}'.format(
                self.dirs
                )
            )
            startfont = self.l[self.choice_font]
            self.ld = self.subget('{} {}{} {}'.format(
                self.keys,
                self.dirs,
                startfont,
                self.to_dir,
                )
            )
            time.sleep(1)
            return self.ld
        except ValueError:raise SystemExit(1)

    def show_table(self,
            file : Optional[list] = 'default.txt',
            dari_ : Optional[int] = 0, 
            sampai_: Optional[int] = 0,
            cookies_ : Optional[bool] = False,
            list_username_ : Optional[bool] = False,
            show_lines_ : Optional[bool] = False,
            ) -> None:
        self.file = file
        self.dari_ = int(dari_)
        self.sampai_ = int(sampai_)
        self.cookies_ = cookies_
        self.list_username_ = list_username_
        self.show_lines_ = show_lines_

        with open(
                '{}'.format(
                    self.file
                ),
            'r'
        )as fl:
            f = fl.read().splitlines()
    
        self.tabc('no',header_style="cyan bold")
        self.tabc('list_userid',
                style="cyan bold",
            )
        self.tabc(
                'list_username',
                style="green bold",
                no_wrap=self.list_username_
            )
        self.tabc(
                'cookies',
                style="#bb9af7 on #1a1b26",
                no_wrap=self.cookies_
            )

        for x , y in enumerate(f[self.dari_:self.sampai_]):
            a = y.split('|')
            time.sleep(0.001)
            self.tabr(
                "{}".format(x),
                "{}".format(a[0]),
                "{}".format(a[1].lower()),
                "{}".format(a[2]),
            end_section=self.show_lines_
        )
        print(tab)

    def list_colors(self):
        self.listcolors = os.listdir(
                "{}".format(
                    self.dirc
                )
            )
        self.tabc(
                'no'
            )
        self.tabc(
                'list_colors',
            )
        for x, y in enumerate(self.listcolors):
            self.tabr(
                    "{}".format(int(
                        x)
                    ),
                    "{}".format(
                    str(y)
                )
            )
        print(tab)
    
    def use_colors(self, choice_color : Optional[int] = 0) -> int:
        self.choice_color = choice_color
        self.lcolor = os.listdir(
                "{}".format(self.dirc
                    )
                )
        startcolor = self.lcolor[self.choice_color]
        self.lcol = self.subget(
                "{} {}{} {}".format(
                    self.keys,
                    self.dirc,
                    startcolor,
                    self.to_dirc,
                )
            )
        time.sleep(1)
        return self.lcol
    
    def use_font_inq(self, choicesF : Optional[bool]) -> []:
        self.choicesF = choicesF
        if self.choicesF == True:
            self.inqF = os.listdir(
                    "{}".format(
                        self.dirs
                    )
                )
            self.choicesF = self.inqF
            try:
                questi_font = [
                        inquirer.List(
                            'inqfont',
                            message="silahkan pilih ",
                            choices=self.choicesF,
                            )
                        ] 
                answF = inquirer.prompt(questi_font)
                self.startd = self.subget(
                        "{} {}{} {}".format(
                            self.keys,
                            self.dirs,
                            answF['inqfont'],
                            self.to_dir,
                            )
                        )
                return "{}".format(self.startd)
            except TypeError:
                raise SystemExit(1)
            finally:
                pass
        else:
            raise SystemExit(1)

    def On_start(self, jalanDari_ : Optional[str] ) -> None:
        self.jalanDari_ = jalanDari_
        print(self.jalanDari_)

class banner(Fonts): 
    def create_banner(self, choice_banner_ : Optional[str] ) -> None:
        self.choice_banner_ = choice_banner_
        self.lbanner = os.listdir(
                '{}'.format(
                    self.banner
                )
            )

        self.tabc(
                'no'
            )
        self.tabc(
                'list_banner'
            )
        for x, y in enumerate(
                self.lbanner
            ):
            self.tabr(
                    "{}".format(
                    int(x
                    )
                ),
                    "{}".format(
                    y)
                ) 
        with open(
                "{}".format(
                    self.file_banner
                ),"w+"
            )as field:
            field.write(
                "cat '/data/data/com.termux/files/home/{}'".format(
                    y)
                )
            field.close()

        startban = self.lbanner[self.choice_banner_]
        self.lban0 = self.subget(
                "{} {}{} {}".format(
                    self.keys,
                    self.banner,
                    startban,
                    self.to_dirb,
                    )
                )
        self.lban = self.subget(
                "{} {} {}".
                format(self.keys,
                    self.file_banner,
                    self.to_dirb,
                    )
                )
        print(
                "{}".format(
                    self.lban,
                    self.lban0
                )
            )

class terminal:
    def __init__(self):
        print('tahap pengembangan')

class auto_installPackges:
    def __init__(self):
        print('tahap pengembangan')

if __name__ == "__main__":
    pass

