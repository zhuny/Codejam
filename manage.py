import os
import runpy
import subprocess
import sys
import time
from pathlib import Path
from shutil import copyfile


class TwoWay:
    def __init__(self, f_in, f_out):
        self.stdin_file = f_in
        self.stdout_file = f_out

    def __enter__(self):
        sys.stdin = self
        sys.stdout = self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

    def write_(self, *args, **kwargs):
        sys.__stdout__.write(*args, **kwargs)
        self.stdout_file.write(*args, **kwargs)

    def write(self, b):
        sys.__stdout__.write(b)
        if 'b' in self.stdout_file.mode:
            b = b.encode()
        self.stdout_file.write(b)

    def flush(self, *args, **kwargs):
        sys.__stdout__.flush(*args, **kwargs)
        self.stdout_file.flush()

    def readline(self):
        result = self.stdin_file.readline()
        if isinstance(result, bytes):
            result = result.decode()
        sys.__stdout__.write("< "+result)
        return result


class Timer:
    def __init__(self):
        self.time = 0

    def __enter__(self):
        self.time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time()-self.time
        print("Running time : {duration:.06}".format(duration=duration))


class Command:
    def __init__(self):
        self.base = Path(".")

    def run(self, name):
        """
        Create New Codejam Problem
        code < *.in > *.out
        @name: Name of Problem
        """
        for inf in os.listdir(name):
            finf = os.path.join(name, inf)
            basename, ext = os.path.splitext(inf)
            if ext == '.in':
                self._run_in(name, finf, os.path.join(name, basename)+'.out')

    def _run_in(self, name, inf, outf):
        print("test file:", inf)
        with open(inf) as f_in:
            with open(outf, 'w') as f_out:
                with Timer():
                    with TwoWay(f_in, f_out):
                        runpy.run_path(name, run_name="__main__")

    def _get_folder(self, name) -> Path:
        return self.base / name

    def _get_skeleton_folder(self) -> Path:
        return self.base / "_skeleton"

    def create(self, name):
        """
        Create New Codejam Problem
        @name: Name of Problem
        """
        f_folder = self._get_folder(name)
        if f_folder.exists():
            print("exist path : ", name)
            return

        f_folder.mkdir(parents=True, exist_ok=True)
        for temp_file in self._get_skeleton_folder().glob("*"):
            copyfile(temp_file, f_folder / temp_file.name)

    def version(self):
        """
        you should run this on python37
        """
        assert (
            sys.version_info.major == 3 and
            sys.version_info.minor == 7
        ), "python37 is required"

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

    def inter(self, name):
        """
        execute as interactive mode
        """
        inter = subprocess.Popen(
            ["python", os.path.join(name, "testing_tool.py"), "2"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
        with Timer():
            with TwoWay(inter.stdout, inter.stdin):
                runpy.run_path(name, run_name="__main__")


def run():
    command = Command()

    if len(sys.argv) < 2:
        func = "help"
        argv = ()
    else:
        command.version()
        func = sys.argv[1]
        argv = sys.argv[2:]

    getattr(command, func)(*argv)


if __name__ == "__main__":
    run()
