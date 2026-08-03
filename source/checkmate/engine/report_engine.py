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