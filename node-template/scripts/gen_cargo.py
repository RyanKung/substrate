#! python3

import toml
import re
from functools import partial
import sys

def find_package_data(path: str) -> (str, str):
    data = toml.load("%s/Cargo.toml" % path)
    return (data['package']['name'], data['package']['version'])


def transfer(dep: dict) -> dict:
    if isinstance(dep, str) or "path" not in dep.keys():
        return dep
    path = dep['path']
    if not ".." in path:
        return dep
    dep.pop('path')
    dep['git'] = "https://github.com/ryankung/substrate.git"
    name, version = find_package_data(path)
    dep['package'] = name
    dep['version'] = version
    return dep


def parser() -> ():
    data = toml.load("Cargo.toml")
    deps = {k: transfer(v) for k, v in data['dependencies'].items()}
    data["dependencies"] = deps
    with open("Cargo.toml", "w+") as d:
        toml.dump(data, d)

if __name__ == '__main__':
    parser()
