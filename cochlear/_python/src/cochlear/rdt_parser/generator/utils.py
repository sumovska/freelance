'''
Created on Nov 27, 2012

@author: pawelp
'''

import keyword

RDT_RESERVED_NAMES = ["value",
                      "address",
                      "cobject",
                      "get_memory",
                      "is_const",
                      "is_placed",
                      "is_pool",
                      "is_constant_address",
                      "get_device",
                      "get_ctype",
                      "get_align",
                      "place",
                      "remove",
                      "update",
                      "retrieve",
                      "pointer",
                      "place_pointed",
                      "create_pointed_variable",
                      "get_pointed_address",
                      "is_code"]


def keywordfix(name):
    if name in keyword.kwlist:
        name = "".join([name, "_"])
    return name


def ctypesaccess_fix(name):
    if name in RDT_RESERVED_NAMES:
        name = "".join([name, "_"])
    return name
