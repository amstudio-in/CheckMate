import bpy
from math import isclose
from .validation_result import ValidationResult
from .severity import Severity

class ObjectValidator:
    """Validates object transforms."""

    def run(self):
        results = []

        results.extend(self._check_unapplied_rotation())
        results.extend(self._check_unapplied_scale())

        return results

    def _check_unapplied_rotation(self):
        results = []

        for obj in bpy.data.objects:

            if obj.type != "MESH":
                continue

            if not (
                isclose(obj.rotation_euler.x, 0.0, abs_tol=1e-6)
                and isclose(obj.rotation_euler.y, 0.0, abs_tol=1e-6)
                and isclose(obj.rotation_euler.z, 0.0, abs_tol=1e-6)
            ):
                results.append(
                    ValidationResult(
                        severity=Severity.WARNING,
                        title="Unapplied Rotation",
                        message=f"Object '{obj.name}' has unapplied rotation."
                    )
                )

        return results

    def _check_unapplied_scale(self):
        results = []

        for obj in bpy.data.objects:

            if obj.type != "MESH":
                continue

            if not (
                isclose(obj.scale.x, 1.0, abs_tol=1e-6)
                and isclose(obj.scale.y, 1.0, abs_tol=1e-6)
                and isclose(obj.scale.z, 1.0, abs_tol=1e-6)
            ):
                results.append(
                    ValidationResult(
                        severity=Severity.WARNING,
                        title="Unapplied Scale",
                        message=f"Object '{obj.name}' has unapplied scale."
                    )
                )

        return results