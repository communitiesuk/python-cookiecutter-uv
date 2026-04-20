import nox

# Global options
nox.options.sessions = ("ruff", "{{ cookiecutter.typechecker }}", "bandit")
nox.options.reuse_existing_virtualenvs = True
nox.options.default_venv_backend = "uv|virtualenv"

SILENT_DEFAULT = True
SILENT_CODE_MODIFIERS = False

# Targets
PACKAGE_LOCATION = "."
CODE_LOCATIONS = PACKAGE_LOCATION
PYTHON_VERSIONS = ["3.12", "3.13"]
PYPY3_VERSION = "pypy3"
LATEST_PYTHON = PYTHON_VERSIONS[-1]


@nox.session(python=PYTHON_VERSIONS, tags=["lint", "format"])
def ruff(session: nox.Session) -> None:
    """Lint and format with ruff."""
    args = session.posargs or (PACKAGE_LOCATION,)
    _install(session, "ruff")
    _run(session, "ruff", "check", *args)
    _run_code_modifier(session, "ruff", "format", *args)

{% if cookiecutter.typechecker == 'mypy' %}
@nox.session(python=PYTHON_VERSIONS, tags=["typecheck"])
def mypy(session: nox.Session) -> None:
    """Verify types using mypy."""
    args = session.posargs or (PACKAGE_LOCATION,)
    _install(session, "mypy", "types-requests", "typing-extensions")
    _run(session, "mypy", *args)
{%- elif cookiecutter.typechecker == 'ty' %}
@nox.session(python=PYTHON_VERSIONS, tags=["typecheck"])
def ty(session: nox.Session) -> None:
    """Verify types using ty."""
    args = session.posargs or (PACKAGE_LOCATION,)
    _install(session, "ty")
    _run(session, "ty", "check", *args)
{%- elif cookiecutter.typechecker == 'pyrefly' %}
@nox.session(python=PYTHON_VERSIONS, tags=["typecheck"])
def pyrefly(session: nox.Session) -> None:
    """Verify types using pyrefly."""
    args = session.posargs or (PACKAGE_LOCATION,)
    _install(session, "pyrefly")
    _run(session, "pyrefly", "check", *args)
{%- endif %}


@nox.session(python=PYTHON_VERSIONS, tags=["security"])
def bandit(session: nox.Session) -> None:
    """Scan for common security issues with bandit."""
    args = session.posargs or (CODE_LOCATIONS,)
    _install(session, "bandit")
    _run(session, "bandit", *args)


def _install(session: nox.Session, *args: str) -> None:
    if args:
        session.install(*args)


def _run(
    session: nox.Session,
    target: str,
    *args: str,
    silent: bool = SILENT_DEFAULT,
) -> None:
    session.run(target, *args, external=True, silent=silent)


def _run_code_modifier(session: nox.Session, target: str, *args: str) -> None:
    _run(session, target, *args, silent=SILENT_CODE_MODIFIERS)
