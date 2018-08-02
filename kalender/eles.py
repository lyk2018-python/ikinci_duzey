import sys
import os
import pwd
import grp


def eles(*dirs, l=False, a=False):  # noqa: E741
    if not dirs:
        dirs = (".",)

    for f in dirs:
        print(*get_files(f, show_hidden=a, show_details=l), sep="\n")
        if len(dirs) > 1 and dirs[-1] != f:
            print("---")


def get_files(arg, show_hidden=False, show_details=False):
    files = []
    for f in os.listdir(arg):
        if not f.startswith(".") or show_hidden:
            if arg != ".":
                f = os.path.join(arg, f)

            files.append(f)

    if show_hidden:
        files = [".", ".."] + files
    data = []

    if show_details:
        for f in files:
            fmt = "{uname}\t{grp}\t{size}\t{fname}"
            datum = {
                "uname": pwd.getpwuid(os.stat(f).st_uid).pw_name,
                "grp": grp.getgrgid(os.stat(f).st_uid).gr_name,
                "size": os.path.getsize(f),
                "fname": f
            }
            data.append(fmt.format(**datum))
        files = data
    return files


if __name__ == '__main__':
    vars = sys.argv[1:]
    flag_l = False
    flag_a = False
    paths = []
    for arg in sys.argv[1:]:
        if "-l" in arg:
            flag_l = True
        elif "-a" in arg:
            flag_a = True
        else:
            paths.append(arg)
    eles(*paths, l=flag_l, a=flag_a)  # noqa: E741
