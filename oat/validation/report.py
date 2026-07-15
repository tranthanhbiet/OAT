class ValidationIssue:
    """
    Represents one validation issue.
    """

    def __init__(
        self,
        level="INFO",
        message="",
        feature=None,
    ):
        self.level = level
        self.message = message
        self.feature = feature

    def __repr__(self):
        return (
            f"ValidationIssue("
            f"level='{self.level}', "
            f"message='{self.message}')"
        )


class ValidationReport:
    """
    Stores validation results.
    """

    def __init__(self):

        self.issues = []

    def add(self, level, message, feature=None):

        self.issues.append(
            ValidationIssue(
                level=level,
                message=message,
                feature=feature,
            )
        )

    @property
    def errors(self):

        return [
            i for i in self.issues
            if i.level == "ERROR"
        ]

    @property
    def warnings(self):

        return [
            i for i in self.issues
            if i.level == "WARNING"
        ]

    @property
    def infos(self):

        return [
            i for i in self.issues
            if i.level == "INFO"
        ]

    def __repr__(self):

        return (
            f"ValidationReport("
            f"errors={len(self.errors)}, "
            f"warnings={len(self.warnings)}, "
            f"infos={len(self.infos)})"
        )