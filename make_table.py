def make_table(nested_list, col_labels):

    # currently, this assumes that the rows aren't labeled
    # obviously that needs to be fixed

    tabular_heading = "\\begin{tabular}{"
    for col_label in col_labels[:-1]:
        tabular_heading += "c|"
    tabular_heading += "c}\n"
    print(tabular_heading)

    header_row = ""
    for col_label in col_labels:
        header_row += str(col_label) + " & "
    header_row = header_row[:-3] + " \\\\\n"
    print(header_row)

    row_strings = []
    for row_list in nested_list:
        row_string = ""
        for row_entry in row_list:
            row_string += str(row_entry) + " & "
        row_string = row_string[:-3] + " \\\\\n"
        row_strings.append(row_string)
    row_strings[-1] = row_strings[-1][:-3] + "\n"

    f = open("table.txt", "a")

    f.write(tabular_heading)
    f.write(header_row)
    for row_string in row_strings:
        f.write(row_string)
    f.write("\\end{tabular}")
    f.close()
