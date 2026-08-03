import bpy

from .. import state


class CHECKMATE_OT_ToggleReportGroup(bpy.types.Operator):
    """Expand or collapse a validation report group."""

    bl_idname = "checkmate.toggle_report_group"
    bl_label = "Toggle Report Group"

    group_title: bpy.props.StringProperty()

    def execute(self, context):

        expanded = state.UIState.expanded_groups

        if self.group_title in expanded:
            expanded.remove(self.group_title)
        else:
            expanded.add(self.group_title)

        for window in bpy.context.window_manager.windows:
            for area in window.screen.areas:
                area.tag_redraw()

        return {'FINISHED'}