import bpy
from .validation_result import ValidationResult
from .severity import Severity

class RenderValidator:
    """Validates render configuration."""

    def run(self):
        results = []

        results.extend(self._check_output_path())

        return results

    def _check_output_path(self):
        results = []

        scene = bpy.context.scene
        output_path = scene.render.filepath

        if output_path in {"", "//"}:
            results.append(
                ValidationResult(
                    severity=Severity.WARNING,
                    title="Output Path Not Configured",
                    message=("Render output path is not configured."),
                    recommendation="Set a render output path.",
                )
            )

        return results