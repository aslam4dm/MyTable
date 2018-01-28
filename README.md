# MyTable
A program which is used to generate tables/menus for terminal/cli programs. Easy to use, and easy to setup

how to instantiate:
T = MyTables.Table(list, number_of_columns)
T.menu("name of menu")
T.style1()
T.style2()
T.style3()

so on...

so far, styles 1-6 are numbered:
i.e. could look something like this (depending on chosen style)
+====================================================+
|  1. passive             ||  2. active              |
|  3. vulnerability       ||  4. exploitation        |
|  5. post-exploitation   ||  6. tools               |
+====================================================+ 
                                            (style2)
                                            
while style 6-8 are not numbered

More features will be added to this program, including more coloring options, tabular formatting and an increased ease of use
