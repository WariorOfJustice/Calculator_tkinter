from tkinter import *
import Label_Frame_Button as Lfb


root = Tk()
root.title('Calculator')

result = Lfb.NewLabel(root)
active_expression = Lfb.NewLabel(root)


# lines - lines operations. first == lowest line.
first = Lfb.NewFrameLine(root)
second = Lfb.NewFrameLine(root)
third = Lfb.NewFrameLine(root)
fourth = Lfb.NewFrameLine(root)
fifth = Lfb.NewFrameLine(root)
sixth = Lfb.NewFrameLine(root)


# buttons for first_line
plus_mines_button = Lfb.NegateButton(first.line, '±', my_command=lambda: plus_mines_button.add_to_calculate(active_expression))
zero_button = Lfb.ZeroButton(first.line, '0', my_command=lambda: zero_button.add_to_calculate(active_expression))
dot_button = Lfb.DotButton(first.line, '.', my_command=lambda: dot_button.add_to_calculate(active_expression))
equal_button = Lfb.EqualButton(first.line, '=', my_command=lambda: equal_button.calculated(active_expression, result))


# buttons for second_line
one_button = Lfb.NumberButton(second.line, '1', my_command=lambda: one_button.add_to_calculate(active_expression))
two_button = Lfb.NumberButton(second.line, '2', my_command=lambda: two_button.add_to_calculate(active_expression))
three_button = Lfb.NumberButton(second.line, '3', my_command=lambda: three_button.add_to_calculate(active_expression))
plus_button = Lfb.OperationButton(second.line, '+', my_command=lambda: plus_button.add_to_calculate(active_expression))


# buttons for third_line
four_button = Lfb.NumberButton(third.line, '4', my_command=lambda: four_button.add_to_calculate(active_expression))
five_button = Lfb.NumberButton(third.line, '5', my_command=lambda: five_button.add_to_calculate(active_expression))
six_button = Lfb.NumberButton(third.line, '6', my_command=lambda: six_button.add_to_calculate(active_expression))
mines_button = Lfb.OperationButton(third.line, '-', my_command=lambda: mines_button.add_to_calculate(active_expression))


# buttons for fourth_line
seven_button = Lfb.NumberButton(fourth.line, '7', my_command=lambda: seven_button.add_to_calculate(active_expression))
eight_button = Lfb.NumberButton(fourth.line, '8', my_command=lambda: eight_button.add_to_calculate(active_expression))
nine_button = Lfb.NumberButton(fourth.line, '9', my_command=lambda: nine_button.add_to_calculate(active_expression))
multiplication_button = Lfb.OperationButton(fourth.line, '×', my_command=lambda: multiplication_button.add_to_calculate(active_expression))


# buttons for fifth_line
exponentiation_square_button = Lfb.ExponentiationButton(fifth.line, 'x²', my_command=lambda: exponentiation_square_button.calculate_exponentiation(active_expression, result, 2))
exponentiation_cube_button = Lfb.ExponentiationButton(fifth.line, 'x³', my_command=lambda: exponentiation_cube_button.calculate_exponentiation(active_expression, result, 3))
percent_button = Lfb.OperationButton(fifth.line, '%', my_command=lambda: percent_button.add_to_calculate(active_expression))
division_button = Lfb.OperationButton(fifth.line, '÷', my_command=lambda: division_button.add_to_calculate(active_expression))


# buttons for sixth_line
left_parenthesis_button = Lfb.LeftParenthesisButton(sixth.line, '(', my_command=lambda: left_parenthesis_button.add_to_calculate(active_expression))
right_parenthesis_button = Lfb.RightParenthesisButton(sixth.line, ')', my_command=lambda: right_parenthesis_button.add_to_calculate(active_expression))
delete_symbol_button = Lfb.DeleteLastOneButton(sixth.line, '⟵', my_command=lambda: delete_symbol_button.delete_last(active_expression))
delete_all_button = Lfb.DeleteAllButton(sixth.line, 'С', my_command=lambda: delete_all_button.delete_all(active_expression, result))


# binds
one_button.bind(root, active_expression)
two_button.bind(root, active_expression)
three_button.bind(root, active_expression)
four_button.bind(root, active_expression)
five_button.bind(root, active_expression)
six_button.bind(root, active_expression)
seven_button.bind(root, active_expression)
eight_button.bind(root, active_expression)
nine_button.bind(root, active_expression)
zero_button.bind(root, active_expression)
equal_button.bind(root, active_expression, result)
dot_button.bind(root, active_expression)
plus_button.bind(root, active_expression)
multiplication_button.bind(root, active_expression, True, '<KeyPress-*>')
division_button.bind(root, active_expression, True, '<KeyPress-/>')
left_parenthesis_button.bind(root, active_expression)
right_parenthesis_button.bind(root, active_expression)
percent_button.bind(root, active_expression)
delete_all_button.bind(root, active_expression, result)
delete_symbol_button.bind(root, active_expression)

def bind_enter(unnecessary_argv):
    equal_button.calculated(active_expression, result)
root.bind('<Return>', bind_enter)

# i cant bind '-', because python does not recognize the following text: <KeyPress--> like the "-".
def bind_mines(event):
    if event.keycode == 109:
        mines_button.add_to_calculate(active_expression)
root.bind('<KeyPress>', bind_mines)


root.mainloop()
