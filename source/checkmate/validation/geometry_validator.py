import bpy
import bmesh
from .validation_result import ValidationResult
from .severity import Severity


class GeometryValidator:
    """Validates mesh geometry."""

    def run(self):
        results = []

        results.extend(self._check_non_manifold())

        return results

    def _check_non_manifold(self):
        results = []

        for obj in bpy.data.objects:

            if obj.type != "MESH":
                continue

            bm = bmesh.new()
            bm.from_mesh(obj.data)

            has_non_manifold = any(
                not edge.is_manifold
                for edge in bm.edges
            )

            bm.free()

            if has_non_manifold:

                results.append(
                    ValidationResult(
                        severity=Severity.WARNING,
                        title="Non-Manifold Geometry",
                        message=f"'{obj.name}'",
                        details=obj.name,
                    )
                )

        return results