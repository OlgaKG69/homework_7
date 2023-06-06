def print_operation_table(operation, num_rows=6, num_columns=6):
    table = []

    for row in range(1, num_rows + 1):
        row_values = []

        for column in range(1, num_columns + 1):
            row_values.append(operation(row, column))

        table.append(row_values)

    for row in table:
        print(' '.join(str(x) for x in row))


print_operation_table(lambda x, y: x * y)
