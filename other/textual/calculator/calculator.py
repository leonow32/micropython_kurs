from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Button, Digits, Footer, Header

# Dziedziczy z App i zwraca None
class CalculatorApp(App[None]):
    CSS_PATH = "calculator.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Digits("1234567890", id="display")
        with Grid():
            yield Button("AC",  classes="top-button")
            yield Button("+/-", classes="top-button")
            yield Button("%",   classes="top-button")
            yield Button.warning("/")

            yield Button("7")
            yield Button("8")
            yield Button("9")
            yield Button.warning("*")

            yield Button("4")
            yield Button("5")
            yield Button("6")
            yield Button.warning("-")

            yield Button("1")
            yield Button("2")
            yield Button("3")
            yield Button.warning("+")

            yield Button("0", id="number-0")
            yield Button(".")
            yield Button.warning("=")

        yield Footer()

if __name__ == "__main__":
    CalculatorApp().run()
