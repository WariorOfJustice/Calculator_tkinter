from tkinter import *


class NewLabel:
    def __init__(self, root, height=3, width=40, **extras):
        self.result = Label(root, height=height, width=width, font=('Helvetica', 10), relief=GROOVE, **extras)
        self.var = StringVar()
        self.result.config(textvariable=self.var)
        self.result.pack(side=TOP, expand=YES, fill=X, anchor=N)

    def set_result(self, new):
        self.var.set(new)

    def get_result(self):
        return self.var.get()


class NewFrameLine:
    def __init__(self, root, **extras):
        self.line = Frame(root, **extras)
        self.line.pack(side=BOTTOM, expand=YES, fill=BOTH)


class NewButton:
    def __init__(self, frame, text, my_command, **extras):
        self.button = Button(frame, text=text, command=my_command, height=2, width=3, font=('Helvetica', 10), **extras)
        self.button.pack(side=LEFT, expand=YES, fill=BOTH)
        self.text = text


class BindButton:
    def add_to_calculate(self, need_label):
        pass

    def bind(self, root, need_label, add_setting=False, math_text=None):
        if add_setting is True:
            str_for_bind = math_text
        else:
            str_for_bind = '<KeyPress-%s>' % self.text

        def func_for_bind(unnecessary_argv):
            self.add_to_calculate(need_label)

        root.bind(str_for_bind, func_for_bind)


class EqualButton(NewButton):
    def calculated(self, need_label, answer_label):
        present_string = need_label.get_result()
        try:
            if len(present_string) != 0:
                if present_string.count('(') > present_string.count(')'):
                    present_string = present_string + ')' * (present_string.count('(') - present_string.count(')'))
                result = str(eval(present_string.replace('×', '*').replace('÷', '/')))
                if result[-2:] == '.0':
                    result = result[:-2]
                answer_label.set_result(present_string + self.text + result)
                need_label.set_result(result)
        except SyntaxError:
            answer_label.set_result('Finish the expression')

    def bind(self, root, need_label, answer_label):
        str_for_bind = '<KeyPress-=>'

        def func_for_bind(unnecessary_argv):
            self.calculated(need_label, answer_label)

        root.bind(str_for_bind, func_for_bind)


class NegateButton(NewButton):
    def add_to_calculate(self, need_label):
        present_string = need_label.get_result()
        if len(present_string) == 0 or present_string == '0' or present_string[-1] in '+-×÷)% ':
            pass
        elif present_string.replace('.', '').isdigit() is True:
            need_label.set_result('-' + present_string)
        elif present_string.replace('.', '')[1:].isdigit() is True:
            need_label.set_result(present_string[1:])
        elif present_string[-1] == '(':
            need_label.set_result(present_string + '-')


class ZeroButton(NewButton, BindButton):
    def add_to_calculate(self, need_label):
        present_string = need_label.get_result()
        if len(present_string) == 0 or present_string[-1] in '(+-×÷%':
            need_label.set_result(present_string + self.text)
        for i in reversed(present_string):
            if i in '()+-×÷%':
                break
            elif i in '.123456789':
                need_label.set_result(present_string + self.text)


class DotButton(NewButton, BindButton):
    def add_to_calculate(self, need_label):
        present_string = need_label.get_result()

        def possibility_check(string):
            if string[-1] in '()+-×÷%':
                return False
            for i in reversed(string):
                if i == '.':
                    return False
                elif i in '()+-×÷%':
                    return True
            return True

        if len(present_string) != 0:
            if possibility_check(present_string) is True:
                need_label.set_result(present_string + self.text)


class NumberButton(NewButton, BindButton):
    def add_to_calculate(self, need_label):
        present_string = need_label.get_result()
        if len(present_string) == 0:
            need_label.set_result(self.text)
        else:
            flag = True
            reversed_str = []
            for i in reversed(present_string):
                if i in '()%×÷-+':
                    break
                reversed_str.append(i)
            if present_string[-1] == ')':
                flag = False
            elif len(reversed_str) > 0 and reversed_str[-1] == '0' and '.' not in reversed_str:
                flag = False
            if flag is True:
                need_label.set_result(present_string + self.text)


class OperationButton(NewButton, BindButton):
    def add_to_calculate(self, need_label):
        present_string = need_label.get_result()
        if len(present_string) == 0:
            pass
        elif present_string[-1] in '(%×÷-+':
            pass
        else:
            need_label.set_result(present_string + self.text)


class ExponentiationButton(NewButton):
    def calculate_exponentiation(self, need_label, answer_label, exponentiation):
        present_string = need_label.get_result()
        number = []
        flag = False
        if len(present_string) != 0 and present_string[-1] not in '(%×÷-+':
            flag = True
            for i in reversed(present_string):
                if i in '(%×÷-+':
                    break
                number[0:0] = [i]
        if flag is True:
            number = ''.join(number)
            number_exponentiation = str(float(number) ** exponentiation)
            if number_exponentiation[-2:] == '.0':
                number_exponentiation = number_exponentiation[:-2]
            position_number = present_string.rfind(number)
            present_string = present_string[:position_number] + present_string[position_number:].replace(number, number_exponentiation)
            str_for_answer_label = present_string.replace(number_exponentiation, '')
            str_for_answer_label = str_for_answer_label + '(' + number + '×' + number + ')'
            if exponentiation == 3:
                str_for_answer_label = str_for_answer_label[:-1] + '×' + number + ')'
            answer_label.set_result(str_for_answer_label)
            need_label.set_result(present_string)


class LeftParenthesisButton(NewButton, BindButton):
    def add_to_calculate(self, need_label):
        present_string = need_label.get_result()
        try:
            if present_string[-1] in '(%×÷-+':
                need_label.set_result(present_string + self.text)
        except IndexError:
            need_label.set_result(present_string + self.text)


class RightParenthesisButton(NewButton, BindButton):
    def add_to_calculate(self, need_label):
        present_string = need_label.get_result()
        flag = False
        if present_string.count('(') > present_string.count(')'):
            flag = True
        if len(present_string) != 0 and present_string[-1] not in '(%×÷-+' and flag is True:
            need_label.set_result(present_string + self.text)


class DeleteAllButton(NewButton):
    def delete_all(self, need_label, answer_label):
        need_label.set_result('')
        answer_label.set_result('')

    def bind(self, root, need_label, answer_label):
        def func_for_bind(unnecessary_argv):
            self.delete_all(need_label, answer_label)

        root.bind('<Delete>', func_for_bind)


class DeleteLastOneButton(NewButton):
    def delete_last(self, need_label):
        present_string = need_label.get_result()
        need_label.set_result(present_string[:-1])

    def bind(self, root, need_label):
        def func_for_bind(unnecessary_argv):
            self.delete_last(need_label)

        root.bind('<BackSpace>', func_for_bind)
