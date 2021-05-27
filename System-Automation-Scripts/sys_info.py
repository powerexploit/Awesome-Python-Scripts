#!/usr/bin/env python3

import platform

info = {
    # System/OS
    'System Type': platform.system(),
    'Host Name': platform.uname()[1],
    'Release': platform.release(),
    'Version': platform.version(),
    'Python Version': platform.python_version(),

}


def main():
    print(
        "\n"
        "============System Information============\n"
    )
    for sys_key, sys_val in info.items():
        print(sys_key, ":", sys_val)


if __name__ == '__main__':
    main()
