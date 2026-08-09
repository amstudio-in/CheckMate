import bpy
import os
from .validation_result import ValidationResult
from .severity import Severity

class TextureValidator:
    """Validates texture files."""

    def run(self):
        results = []

        results.extend(self._check_missing_texture_files())
        results.extend(self._check_unused_images())

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

    def _check_unused_images(self):
        results = []

        for image in bpy.data.images:

            if image.source != "FILE":
                continue

            if image.users > 0:
                continue

            if image.use_fake_user:
                continue

            results.append(
                ValidationResult(
                    severity=Severity.INFO,
                    title="Unused Image",
                    message=f"'{image.name}'",
                    details=image.name,
                )
            )

        return results