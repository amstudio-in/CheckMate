import bpy
import os
from .validation_result import ValidationResult
from .severity import Severity

class TextureValidator:
    """Validates texture files."""

    def run(self):
        results = []

        results.extend(self._check_missing_texture_files())

        return results

    def _check_missing_texture_files(self):
        results = []

        checked = set()

        for image in bpy.data.images:

            if image.source != "FILE":
                continue

            filepath = bpy.path.abspath(image.filepath)

            if filepath in checked:
                continue

            checked.add(filepath)

            if not os.path.exists(filepath):

                filename = os.path.basename(filepath)

                results.append(
                    ValidationResult(
                        severity=Severity.ERROR,
                        title="Missing Texture File",
                        message=f"Texture '{filename}' could not be found.",
                        recommendation="Relink missing textures",
                    )
                )

        return results