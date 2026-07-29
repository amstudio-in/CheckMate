from ..validation.camera_validator import CameraValidator

class ValidationEngine:
    """Coordinates all project validation checks."""

    def run(self):
        print("[CheckMate] Validation Engine Started")

        results = []

        camera_validator = CameraValidator()
        results.extend(camera_validator.run())

        return results