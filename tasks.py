import os
from invoke import task

HERE = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(HERE, 'mysite')


@task
def test_all(ctx):
    flake(ctx)
    test_app(ctx)
    # TODO: add more as they become available

# PYTHON


@task(aliases=['flake8'])
def flake(ctx, echo=True):
    # Ignore too long lines with E501 because
    # it throws and error on every migration file
    ctx.run('flake8 {} {}'.format(APP,
                                  "--ignore=E501"), echo=echo)


@task
def app_server(ctx):
    ctx.run('python {}/manage.py runserver'.format(APP), echo=True)


@task
def test_app(ctx):
    ctx.run(
        'python {}/manage.py test {}'.format(APP, APP), echo=True, pty=True)
