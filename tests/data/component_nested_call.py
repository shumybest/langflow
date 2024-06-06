from random import randint

from langflow.custom import Component
from langflow.template.field.base import Input, Output


class MultipleOutputsComponent(Component):
    inputs = [
        Input(display_name="Input", name="input", field_type=str),
        Input(display_name="Number", name="number", field_type=int),
    ]
    outputs = [
        Output(display_name="Certain Output", name="certain_output", method="certain_output"),
        Output(display_name="Other Output", name="other_output", method="other_output"),
    ]

    def certain_output(self) -> int:
        return randint(0, self.number)

    def other_output(self) -> int:
        return self.certain_output()
