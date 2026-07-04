from textual import on
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Input, Label, Switch


# class Name(Widget):
#     """Generates a greeting."""

#     who = reactive("name")

#     def render(self) -> str:
#         return f"Hello, {self.who}!"


class NameApp(App[None]):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter your name")
        yield Switch()
        yield Label("aaaa")
        # yield Name()

    @on(Input.Changed)
    def changed(self, event: Input.Changed) -> None:
        label = self.query_one(Label)
        label.update(f"Label changed: {event}")

    @on(Input.Submitted)
    def submitted(self, event: Input.Submitted) -> None:
        label = self.query_one(Label)
        label.update(f"Label submited: {event}")

    @on(Input.Blurred)
    def blurred(self, event: Input.Blurred) -> None:
        label = self.query_one(Label)
        label.update(f"Label submited: {event}")

if __name__ == "__main__":
    NameApp().run()