#! python3

import toml
import re
from functools import partial
import sys


def find_package_name(path: str) -> str:
    with open("%s/Cargo.toml" % path, "r") as f:
        return next(filter(bool, map(partial(re.match, 'name = \"(.*)\"'), f.readlines()))).group(1)


def transfer(dep: dict) -> dict:
    if isinstance(dep, str) or "path" not in dep.keys():
        return dep
    path = dep['path']
    dep.pop('path')
    dep['git'] = "https://github.com/ryankung/substrate.git"
    dep['package'] = find_package_name(path)
    return dep


def parser() -> ():
    data = toml.load("Cargo.toml")
    deps = {k: transfer(v) for k, v in data['dependencies'].items()}
    data["dependencies"] = deps
    with open("Cargo.toml", "w+") as d:
        toml.dump(data, d)

if __name__ == '__main__':
    parser()
