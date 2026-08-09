bl_info = {
    "name": "CheckMate",
    "author": "AM Studio",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar",
    "description": "Validate Blender projects before rendering or exporting.",
    "category": "3D View",
}

from .registration import register, unregister


if __name__ == "__main__":
    register()