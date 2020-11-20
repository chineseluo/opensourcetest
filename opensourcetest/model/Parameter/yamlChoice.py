#!/user/bin/env python
# -*- coding: utf-8 -*-
from opensourcetest.builtin.autoParamInjection import AutoInjection


class Login(AutoInjection):
    def __init__(self):
        super(Login, self).__init__(self.__class__.__name__)


if __name__ == '__main__':
    ...
