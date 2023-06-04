import json
from typing import List, Dict

from source.payroll_entry import PayrollEntry


class Report:
    def __init__(self, entries: List[PayrollEntry]):
        self.entries = entries

    def generate(self) -> str:
        output = ''
        for entry in self.entries:
            output += '\n'.join(f'{key}: {value}' for key, value in entry.to_dict().items())
            output += '\n' + '-' * 50 + '\n'
        return output


class JSONReport(Report):
    def generate(self) -> str:
        return json.dumps(self.entries)
