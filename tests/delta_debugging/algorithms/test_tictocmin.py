import doctest

from delta_debugging import Configuration, Debugger, Outcome, TicTocMin


def oracle(config: Configuration) -> Outcome:
    s: str = "".join(config)
    print(s, end=" ")
    for i in range(10):
        if str(i) not in s:
            print("Pass")
            return Outcome.PASS
    print("Fail")
    return Outcome.FAIL


def test_tictocmin() -> None:
    debugger: Debugger = Debugger(TicTocMin(), oracle)
    debugger.debug(
        list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHI")
    )
    assert "".join(debugger.result) == "1234567890"


def test_docstring() -> None:
    import delta_debugging.algorithms.tictocmin

    results: doctest.TestResults = doctest.testmod(
        delta_debugging.algorithms.tictocmin, verbose=True
    )
    assert results.failed == 0
