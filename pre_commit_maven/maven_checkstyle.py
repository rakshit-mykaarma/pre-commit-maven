import argparse
import os.path
from pre_commit_maven.utils import generic_main

CWD = os.getcwd()


def main(cwd=CWD, print_fn=print, execute_fn=generic_main.execute) -> int:
    return execute_fn(["checkstyle:check -Dincludes='**\\'$(git diff --cached --name-only --diff-filter=A | xargs -n1 basename | tr '\n' ' '| rev | cut -c 2- | rev | sed 's/ /,**\\/g')"], cwd)


if __name__ == "__main__":
    exit(main())
