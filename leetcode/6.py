def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows

    current_row = 0

    going_down = False

    for char in s:
        rows[current_row] += char

        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down

        if going_down:
            current_row += 1
        else:
            current_row -= 1

    return ''.join(rows)


print(convert("PAYPALISHIRING", 3)) 