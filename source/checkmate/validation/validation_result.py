class ValidationResult:
    """Represents the result of a single validation check."""

    def __init__(self, severity, title, message, details=None,):
        self.severity = severity
        self.title = title
        self.message = message
        self.details = details