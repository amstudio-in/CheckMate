import bpy

from .panel import CHECKMATE_PT_MainPanel

classes = (
    CHECKMATE_PT_MainPanel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)