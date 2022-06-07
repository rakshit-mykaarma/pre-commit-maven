import argparse
import os.path
from pre_commit_maven.utils import generic_main

CWD = os.getcwd()


def main(cwd=CWD, print_fn=print, execute_fn=generic_main.execute) -> int:
    return execute_fn(["checkstyle:check -DincludesFiles=$(git diff --cached --name-only --diff-filter=A | tr '\n' , | rev | cut -c 2- | rev)"], cwd)


if __name__ == "__main__":
    exit(main())
