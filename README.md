# MyTable
A program which is used to generate tables/menus for terminal/cli programs. Easy to use, and easy to setup


for use, (atm) Download source code, place files in CWD, and import MyTable

how to instantiate:
T = MyTables.Table(list, number_of_columns)
T.style("|", "-", "+")
T.colour(border=blue, number="grey", text="red")
T.show_table()
