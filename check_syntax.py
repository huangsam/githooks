import sys

from flake8.main import application


def main(argv=None):
    app = application.Application()
    app.run(argv)
    app.exit()


if __name__ == '__main__':
    main(sys.argv[1:])
