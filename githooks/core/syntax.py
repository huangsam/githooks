from flake8.main import application


def check_flake8(params=None):
    app = application.Application()
    app.run(params)
