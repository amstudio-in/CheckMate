import bpy
from .validation_result import ValidationResult
from .severity import Severity

class CameraValidator:
    """Validates camera configuration."""

    def run(self):
        results = []
        scene = bpy.context.scene
        results.extend(self._check_active_camera(scene))

        return results

    def _check_active_camera(self, scene):
        results = []

        if bpy.context.scene.camera is None:
            results.append(
                ValidationResult(
                    severity=Severity.ERROR,
                    title="Missing Active Camera",
                    message="No active camera is assigned to the scene.",
                    recommendation="Add an active camera before rendering.",
                )
            )

        return results