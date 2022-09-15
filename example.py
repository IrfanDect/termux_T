from termux_toolkit import Fonts
from termux_toolkit import banner

term = Fonts()
term = banner()

#// contoh -> 1
term.show_table(dari_=0,sampai_=3,show_lines_=True)

#// contoh -> 2
term.list_colors()

#// contoh -> 3
term.list_font() 

#// contoh -> 4
#term.use_colors(choice_color=0) # -> choices list

#// contoh -> 5
#term.use_font(choice_font=6)

#// contoh -> 6
asd = term.use_font_inq(choicesF=True)

term.create_banner(choice_banner_=1)
