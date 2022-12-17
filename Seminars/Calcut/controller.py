import view
import model
import operant
import logg

def buttom_click():
    some_str = view.input_str()
    some_list = model.some_sign(some_str)
    if some_list[2] == '+':
        result = operant.sum(some_list[0], some_list[1])
    elif some_list[2] == '-':
        result = operant.diff(some_list[0], some_list[1])
    elif some_list[2] == '*':
        result = operant.mult(some_list[0], some_list[1])
    elif some_list[2] == '/':
        result = operant.div(some_list[0], some_list[1])
    view.output_data(result)
    logg.reset(some_str, result)