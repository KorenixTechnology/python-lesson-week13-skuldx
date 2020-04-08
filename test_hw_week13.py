import io, sys
import textwrap

try:
    from hw_week13 import hw_week13
except ImportError:
    from hw_week13_solution import hw_week13

class Test:
    def test_function(self, capsys):
        expected_output = """\
        3
        10
        5
        16
        8
        4
        2
        1
        """

        hw_week13(6)
        captured = capsys.readouterr()
        assert captured.out == textwrap.dedent(expected_output)

    def test_invalid_input(self, capsys):
        expected_output = """\
        Please enter an positive integer.
        """

        hw_week13('Hello')
        captured = capsys.readouterr()
        assert captured.out == textwrap.dedent(expected_output)

    def setup_method(self):
        self.orig_stdin = sys.stdin

    def teardown_method(self):
        sys.stdin = self.orig_stdin
