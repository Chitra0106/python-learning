from lb_pretty_table import PrettyTable

table = PrettyTable()
print(table)
print(PrettyTable.__module__)
table.add_column("Pokemon Name",["Pikachu,Squirtle","Charmeleon"])
table.add_column("Type",["Electric","Water","fIRE"])