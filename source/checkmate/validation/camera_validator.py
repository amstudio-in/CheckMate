import bpy
from .validation_result import ValidationResult
from .severity import Severity

class CameraValidator:
    """Validates camera configuration."""

    def run(self):
        results = []

        if bpy.context.scene.camera is None:
            results.append(
                ValidationResult(
                    severity=Severity.ERROR,
                    title="Missing Active Camera",
                    message="No active camera is assigned to the scene."
                )
            )

        return results