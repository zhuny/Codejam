import os
import runpy
import sys
import time
from shutil import copyfile


class TwoWay:
    def __init__(self, f_in, f_out):
        self.stdin_file = f_in
        self.stdout_file = f_out

    def __enter__(self):
        sys.stdin = self.stdin_file
        sys.stdout = self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

    def write(self, *args, **kwargs):
        self.stdout_file.write(*args, **kwargs)
        sys.__stdout__.write(*args, **kwargs)

    def flush(self, *args, **kwargs):
        sys.__stdout__.flush(*args, **kwargs)


class Timer:
    def __init__(self):
        self.time = 0

    def __enter__(self):
        self.time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time()-self.time
        print("Running time : {duration:.06}".format(duration=duration))


class Command:
    def run(self, name):
        """
        Create New Codejam Problem
        code < *.in > *.out
        @name: Name of Problem
        """
        for inf in os.listdir(name):
            if not inf.endswith('.in'):
                continue
            print("test file:", inf)
            inf = os.path.join(name, inf)
            outf = os.path.splitext(inf)[0]+'.out'
            with open(inf) as f_in:
                with open(outf, 'w') as f_out:
                    with Timer():
                        with TwoWay(f_in, f_out):
                            runpy.run_path(name, run_name="__main__")

    def create(self, name):
        """
        Create New Codejam Problem
        @name: Name of Problem
        """
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

    def version(self):
        """
        you should run this on python35
        """
        assert (
            sys.version_info.major == 3 and
            sys.version_info.minor == 5
        ), "python35 is required"

    def help(self):
        """
        Show this message.
        List of valid commands.
        """
        print(__name__, "{command}", "additional argv...")
        print()

        for name in dir(self):
            if not name.startswith('_'):
                func = getattr(self, name)
                print(name, '-')
                print(func.__doc__)
                print()


if __name__ == "__main__":
    command = Command()

    if len(sys.argv) < 2:
        func = "help"
        argv = ()
    else:
        command.version()
        func = sys.argv[1]
        argv = sys.argv[2:]

    getattr(command, func)(*argv)


