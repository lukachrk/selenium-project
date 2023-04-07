import unittest
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.table import Table

from src.testcases.Test_Authentication import AuthTest
from src.testcases.Test_Registration import Registration_Test
from src.testcases.Test_MainPage import MainPageTest

table = Table()
table.add_column("Test Case")
table.add_column("Result")


def run_tests(suite_name):
    suite = None
    match suite_name:
        case "regression":
            suite = unittest.TestLoader().loadTestsFromTestCase(AuthTest)
        case "smoke":
            suite = unittest.TestLoader().loadTestsFromTestCase(Registration_Test)
        case _:
            raise ValueError(f"[bold red]Invalid test suite name:[/bold red] {suite_name}")

    console = Console()
    console.print(f"[bold green]Running test suite:[/bold green] {suite_name}")
    
    test_result = unittest.TestResult()
    suite.run(test_result)

    successful_tests = test_result.testsRun - len(test_result.errors) - len(test_result.failures)

    table.add_row("", f"Total tests: [bold]{test_result.testsRun}[/bold]")
    table.add_row("", f"Failed tests: [red]{len(test_result.failures) + len(test_result.errors)}[/red]")
    table.add_row("", f"Successful tests: [green]{successful_tests}[/green]", end_section=True)

    for test_case, error in test_result.failures + test_result.errors:
        test_case_name = str(test_case).split()[0]
        table.add_row(test_case_name, f"[red]❌ Fail[/red]\n{error}", end_section=True)


if __name__ == "__main__":
    console = Console()
    suite_choices = ["regression", "smoke"]
    suite_name = Prompt.ask("[bold]Please enter the test suite you want to run:[/bold] ", choices=suite_choices)
    console.print(f"[bold]You selected the '{suite_name}' test suite.[/bold]")

    Prompt.ask(f"[bold]Press enter to start the '{suite_name}' test suite[/bold]")
    run_tests(suite_name)
    console.print(table)