from ..validation.severity import Severity

class ScoringEngine:
    """Calculates project health score and readiness."""

    MAX_SCORE = 100
    MIN_SCORE = 0

    ERROR_PENALTY = 20
    WARNING_PENALTY = 5
    INFO_PENALTY = 0

    def calculate(self, validation_results):
        score = self.MAX_SCORE

        for result in validation_results:

            if result.severity == Severity.ERROR:
                score -= self.ERROR_PENALTY

            elif result.severity == Severity.WARNING:
                score -= self.WARNING_PENALTY

            elif result.severity == Severity.INFO:
                score -= self.INFO_PENALTY

        score = max(self.MIN_SCORE, score)

        return score

    def get_readiness_status(self, score, validation_results):

        has_error = any(
            result.severity == Severity.ERROR
            for result in validation_results
        )

        if has_error:
            return "Not Ready"

        if score >= 90:
            return "Ready"

        if score >= 70:
            return "Needs Review"

        return "Not Ready"

    def get_score_summary(self, validation_results):

        errors = sum(
            1 for result in validation_results
            if result.severity == Severity.ERROR
        )

        warnings = sum(
            1 for result in validation_results
            if result.severity == Severity.WARNING
        )

        infos = sum(
            1 for result in validation_results
            if result.severity == Severity.INFO
        )

        if errors == 0 and warnings == 0 and infos == 0:
            return "No validation issues found."

        return (
            f"{errors} Error(s) • "
            f"{warnings} Warning(s) • "
            f"{infos} Info(s)"
        )