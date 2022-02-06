""" Декораторы """

import logging
import sys


if sys.argv[0].find('client') == -1:
    # если не клиент
    LOGGER = logging.getLogger('server')
else:
    LOGGER = logging.getLogger('client')


def log(func_to_log):
    """ Функция-декоратор """
    def log_saver(*args, **kwargs):
        ret = func_to_log(*args, **kwargs)
        LOGGER.debug(f'Была вызвана функция {func_to_log.__name__} с параметрами {args}, {kwargs}. '
                     f'Вызов из модуля {func_to_log.__module__} ')
        return ret
    return log_saver
