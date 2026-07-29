from ..validation.camera_validator import CameraValidator

class ValidationEngine:
    """Coordinates all project validation checks."""

    def run(self):
        print("[CheckMate] Validation Engine Started")

        results = []

        camera_validator = CameraValidator()

        try:
            results.extend(camera_validator.run())
        except Exception as error:
            print(f"[CheckMate] CameraValidator failed: {error}")

        return results