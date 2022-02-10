import nox

hello_list = "hello-pure", "hello-cpp", "hello-pybind11", "hello-cython"
long_hello_list = hello_list + ("pen2-cython",)


@nox.session
@nox.parametrize("module", long_hello_list, ids=long_hello_list)
def dist(session: nox.Session, module: str) -> None:
    session.cd(f"projects/{module}")
    session.install("build")

    # Builds SDist and wheel
    session.run("pyproject-build")


@nox.session
@nox.parametrize("module", hello_list, ids=hello_list)
def test(session: nox.Session, module: str) -> None:
    session.cd(f"projects/{module}")
    session.install("pytest", "pytest-cov")

    session.install(".")
    session.run("pytest")
