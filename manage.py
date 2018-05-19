import os
import runpy
import sys
from shutil import copyfile


class TwoWay:
    def __init__(self, f):
        self.file = f

    def write(self, *args, **kwargs):
        self.file.write(*args, **kwargs)
        sys.__stdout__.write(*args, **kwargs)

    def flush(self, *args, **kwargs):
        sys.__stdout__.flush(*args, **kwargs)


class Command:
    def run(self, name):
        for inf in os.listdir(name):
            if not inf.endswith('.in'):
                continue
            print("test file:", inf)
            inf = os.path.join(name, inf)
            outf = os.path.splitext(inf)[0]+'.out'
            with open(inf) as f_in:
                with open(outf, 'w') as f_out:
                    sys.stdin = f_in
                    sys.stdout = TwoWay(f_out)
                    runpy.run_path(name, run_name="__main__")
                    sys.stdin = sys.__stdin__
                    sys.stdout = sys.__stdout__

    def create(self, name):
        if os.path.isdir(name):
            print("exist path : ", name)
            return

        os.mkdir(name)
        skeleton = '_skeleton'
        for f in os.listdir(skeleton):
            copyfile(
                os.path.join(skeleton, f),
                os.path.join(name, f)
            )


if __name__ == "__main__":
    command = Command()

    if len(sys.argv) < 2:
        print(__name__, "{command}", "additional argv...")

    else:
        getattr(command, sys.argv[1])(*sys.argv[2:])


