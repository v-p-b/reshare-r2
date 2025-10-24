#!/usr/bin/env python3

import argparse
import json

from reshare import *


def resh_address_to_address(resh_addr: ReshAddress) -> int:
    offset = int.from_bytes(bytes(resh_addr.bytes), byteorder="little", signed=False)
    return offset


def import_function(addr, name):
    print("s 0x%x" % (addr))
    print("af")
    print("afn %s" % (name))


parser = argparse.ArgumentParser()
parser.add_argument("json")

args = parser.parse_args()

reshare = Reshare.from_json_data(json.load(open(args.json, "r")))

RESH_TYPE_CACHE = {}

for T in reshare.data_types:
    RESH_TYPE_CACHE[T.name] = T

for sym in reshare.symbols:
    addr = resh_address_to_address(sym.address)
    if (
        sym.type is not None
        and RESH_TYPE_CACHE[sym.type.type_name].content.type == "FUNCTION"
    ):
        import_function(addr, sym.name)
