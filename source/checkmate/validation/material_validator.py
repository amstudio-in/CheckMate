import bpy
from .validation_result import ValidationResult
from .severity import Severity

class MaterialValidator:
    """Validates material assignments."""

    def run(self):
        results = []

        results.extend(self._check_missing_materials())
        results.extend(self._check_empty_material_slots())

        return results

    def _check_missing_materials(self):
        results = []

        for obj in bpy.data.objects:

            if obj.type != "MESH":
                continue

            if len(obj.material_slots) == 0:

                results.append(
                    ValidationResult(
                        severity=Severity.WARNING,
                        title="Object Has No Material",
                        message=f"Object '{obj.name}' has no material assigned."
                    )
                )

        return results

    def _check_empty_material_slots(self):
        results = []

        for obj in bpy.data.objects:

            if obj.type != "MESH":
                continue

            for slot in obj.material_slots:

                if slot.material is None:

                    results.append(
                        ValidationResult(
                            severity=Severity.WARNING,
                            title="Empty Material Slot",
                            message=(
                                f"Object '{obj.name}' contains "
                                "an empty material slot."
                            )
                        )
                    )

        return results