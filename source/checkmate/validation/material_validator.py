import bpy
from .validation_result import ValidationResult
from .severity import Severity

class MaterialValidator:
    """Validates material assignments."""

    def run(self):
        results = []

        results.extend(self._check_missing_materials())
        results.extend(self._check_empty_material_slots())
        results.extend(self._check_unused_materials())

        return results

    def _check_missing_materials(self):
        results = []

        for obj in bpy.data.objects:

            if obj.type != "MESH":
                continue

            if not obj.material_slots:

                results.append(
                    ValidationResult(
                        severity=Severity.WARNING,
                        title="Object Has No Material",
                        message=f"'{obj.name}'",
                        details=obj.name,
                        recommendation="Assign materials",
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
                            message=f"'{obj.name}'",
                            details=obj.name,
                            recommendation="Assign material to the empty slot",
                        )
                    )

        return results

    def _check_unused_materials(self):
        results = []

        for material in bpy.data.materials:

            if material.users > 0:
                continue

            if material.use_fake_user:
                continue

            if material.is_grease_pencil:
                continue

            results.append(
                ValidationResult(
                    severity=Severity.INFO,
                    title="Unused Material",
                    message=f"'{material.name}'",
                    details=material.name,
                )
            )

        return results