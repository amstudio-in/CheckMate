from collections import defaultdict
from ..validation.severity import Severity

class ReportEngine:
    """Builds grouped validation reports."""

    def build(self, validation_results):

        report = {
            Severity.ERROR: [],
            Severity.WARNING: [],
            Severity.INFO: [],
        }

        grouped = defaultdict(list)

        for result in validation_results:

            grouped[
                (
                    result.severity,
                    result.title,
                )
            ].append(result)

        for (severity, title), results in grouped.items():

            report[severity].append(
                {
                    "title": title,
                    "message": results[0].message,
                    "severity": severity,
                    "count": len(results),
                    "expandable": len(results) > 1,
                    "expanded": False,
                    "details": [
                        result.details
                        for result in results
                        if result.details
                    ],
                    "results": results,
                }
            )
                    
        report[Severity.ERROR].sort(key=lambda item: item["title"])
        report[Severity.WARNING].sort(key=lambda item: item["title"])
        report[Severity.INFO].sort(key=lambda item: item["title"])

        return report

    def build_recommendations(self, validation_results):
        """Builds grouped recommendation reports."""

        grouped = defaultdict(list)

        for result in validation_results:

            if not result.recommendation:
                continue

            grouped[result.recommendation].append(result)

        recommendations = []

        for recommendation, results in grouped.items():

            count = len(results)
            text = recommendation

            if count > 1:
                text = f"{recommendation} to {count} objects."

            recommendations.append(
                {
                    "title": results[0].title,
                    "severity": results[0].severity,
                    "text": text,
                    "recommendation": recommendation,
                    "count": count,
                    "expandable": count > 1,
                    "expanded": False,
                    "details": [
                        result.details
                        for result in results
                        if result.details
                    ],
                }
            )

        severity_order = {
            Severity.ERROR: 0,
            Severity.WARNING: 1,
            Severity.INFO: 2,
        }

        recommendations.sort(
            key=lambda item: (
                severity_order[item["severity"]],
                item["title"],
            )
        )

        return recommendations