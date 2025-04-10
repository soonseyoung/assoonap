def rep_char(c, n):
    print(c * n)


def draw_line_string(s):
    rep_char('-', len(s))
    print(s)
    rep_char('-', len(s))


name = input("Input his/her name: ")

msg1 = f"Hello {name},"
msg2 = "Welcome to Seoul."

nstr = len(msg1) if len(msg1) > len(msg2) else len(msg2)

rep_char('-', nstr)
print(msg1)
print(msg2)
rep_char('-', nstr)
