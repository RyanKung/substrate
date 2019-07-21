#! python3

import re
from functools import partial


def find_package_name(path: str) -> str:
    with open("%s/Cargo.toml" % path, "r") as f:
        return next(filter(bool, map(partial(re.match, 'name = \"(.*)\"'), f.readlines()))).group(1)


def transfer(line: str) -> str:
    matched = re.match('(.*) = \{.* path = \"(.*)\"', line)
    if not matched: return line
    package = matched.group(1)
    path = matched.group(2)
    template = '%s = { git="https://github.com/RyanKung/substrate", package="%s" }\n'
    return template % (package, find_package_name(path))



def parser() -> ():
    with open("./Cargo.toml", "r+") as f, open("./Cargo.toml.bak", "w+") as bak:
        content = f.readlines()
        bak.writelines(content)
        f.writelines(map(transfer, content))


if __name__ == '__main__':
    parser()
