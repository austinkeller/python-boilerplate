from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from python_boilerplate import commands


def main(args=None):
    args = commands.parser.parse_args(args)
    try:
        func = args.func
    except AttributeError:
        pass
    else:
        func(args)

if __name__ == '__main__':
    main()