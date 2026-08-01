from ..validation.camera_validator import CameraValidator
from ..validation.material_validator import MaterialValidator
from ..validation.texture_validator import TextureValidator
from ..validation.geometry_validator import GeometryValidator

class ValidationEngine:
    """Coordinates all project validation checks."""

    def run(self):
        print("[CheckMate] Validation Engine Started")

        results = []

        validators = [
            CameraValidator(),
            MaterialValidator(),
            TextureValidator(),
            GeometryValidator(),
        ]

        for validator in validators:
            try:
                results.extend(validator.run())
            except Exception as error:
                print(
                    f"[CheckMate]"
                    f"{validator.__class__.__name__} failed: {error}"
                )

        return results