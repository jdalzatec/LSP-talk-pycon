class PayrollError(Exception):
    """Base class for other exceptions."""


class NoEntriesError(PayrollError):
    """Raised when there are no entries to generate a report."""
