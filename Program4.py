# SQL Join Query Builder and Validator

table1 = input("Enter first table name: ")
table2 = input("Enter second table name: ")

column1 = input("Enter join column from first table: ")
column2 = input("Enter join column from second table: ")

join_type = input("Enter join type (INNER/LEFT/RIGHT/FULL): ").upper()

valid_joins = ["INNER", "LEFT", "RIGHT", "FULL"]

if join_type not in valid_joins:
    print("Invalid JOIN type!")
else:
    query = f"""
SELECT *
FROM {table1}
{join_type} JOIN {table2}
ON {table1}.{column1} = {table2}.{column2};
"""

    print("\nValid SQL Query:")
    print(query)