import inspect
import os


def dum_decor(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return wrapper


def unit_decor(func):
    def wrapper(*args, **kwargs):
        filename = os.path.basename(__file__)
        with open('unit_log_'+filename+'.txt', 'a') as f:
            str_to_record = ''

            actual_result = func(*args, **kwargs)
            str_func_with_param = get_param_list_in_string(*args, **kwargs)

            str_to_record += '\nexpectedResult = ' + str(actual_result)
            str_to_record += '\nactualResult = ' \
                + str(func.__name__) + str_func_with_param
            str_to_record += '\nself.assertEqual(expectedResult, actualResult)'
            str_to_record += '\n'

            f.write(str_to_record)
        return actual_result
    return wrapper


def get_param_list_in_string(*args, **kwargs):
    ret_str = '('

    if len(args) > 0:
        for x in args:
            ret_str += str(x)
            ret_str += ', '
        ret_str = ret_str[:-2]

    if len(kwargs) > 0:
        if len(args) > 0:
            ret_str += ', '

        for k, v in kwargs.items():
            ret_str += k + '=' + str(v)
            ret_str += ', '
        ret_str = ret_str[:-2]

    ret_str += ')'
    return ret_str
