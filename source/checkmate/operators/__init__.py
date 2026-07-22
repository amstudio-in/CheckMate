import bpy

from .scan_operator import CHECKMATE_OT_RunScan

classes = (
    CHECKMATE_OT_RunScan,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)