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

    def __str__(self):
        """
        Human-readable validation report.
        """

        lines = []

        lines.append("Validation Report")
        lines.append("=================")
        lines.append("")

        status = "PASS"

        if self.errors:
            status = "FAIL"
        elif self.warnings:
            status = "WARNING"

        lines.append(f"Status : {status}")
        lines.append("")

        lines.append(f"Errors   : {len(self.errors)}")
        lines.append(f"Warnings : {len(self.warnings)}")
        lines.append(f"Infos    : {len(self.infos)}")

        if not self.issues:
            lines.append("")
            lines.append("No issues found.")
            return "\n".join(lines)

        def add_section(title, issues):
            if not issues:
                return

            lines.append("")
            lines.append(title)
            lines.append("-" * len(title))

            for issue in issues:
                lines.append(f"- {issue.message}")

        add_section("Errors", self.errors)
        add_section("Warnings", self.warnings)
        add_section("Information", self.infos)

        return "\n".join(lines)