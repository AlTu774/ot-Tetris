from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

def lint(ctx):
    ctx.run("pylint src", pty=True)

def test(ctx):
    ctx.run("pytest src", pty=True)

