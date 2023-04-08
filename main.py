import unittest
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.table import Table

from src.testcases.Test_Authentication import AuthTest
from src.testcases.Test_Registration import Registration_Test
from src.testcases.Test_MainPage import MainPageTest
from src.testcases.Test_ProfilePage import ProfilePage_Test

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
        case "authentication":
            suite = unittest.TestLoader().loadTestsFromTestCase(AuthTest)        
        case "registration":
            suite = unittest.TestLoader().loadTestsFromTestCase(Registration_Test)        
        case "profile":
            suite = unittest.TestLoader().loadTestsFromTestCase(ProfilePage_Test)        
        case "main":
            suite = unittest.TestLoader().loadTestsFromTestCase(MainPageTest)
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
    suite_choices = ["regression", "smoke", "authetication", "registration", 'profile', 'main']
    
    console.print("[bold] please select one of the suites to run the test [/bold]")
    console.print("\n".join([f"[bold] {i+1}. {option} [/bold]" for i, option in enumerate(suite_choices)]))
    suite_name = Prompt.ask()
    
    console.print(f"[bold]You selected the '{suite_choices[int(suite_name)-1]}' test suite.[/bold]")
    Prompt.ask(f"[bold]Press enter to start the '{suite_choices[int(suite_name)-1]}' test suite[/bold]")
    run_tests(suite_choices[int(suite_name)-1])
    console.print(table)