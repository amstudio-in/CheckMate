import bpy
from .. import state
from ..validation.severity import Severity

class CHECKMATE_PT_MainPanel(bpy.types.Panel):
    """Main CheckMate panel"""

    bl_label = "CheckMate"
    bl_idname = "CHECKMATE_PT_main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "CheckMate"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Project Validation Assistant")
        layout.separator()

        section = layout.box()
        section.label(text="Health Score",icon="INFO",)
        row = section.row()
        split = row.split(factor=0.20)
        split.label(text="Score:")
        value_box = split.box()
        if state.UIState.is_scanning:
            value_box.label(text="Calculating...")
        else:
            value_box.label(text=state.UIState.health_score)

        section = layout.box()
        section.label(text="Readiness Status", icon="CHECKMARK",)
        row = section.row()
        split = row.split(factor=0.20)
        split.label(text="Status:")
        status_box = split.box()
        if state.UIState.is_scanning:
            status_box.label(text="Scanning...")
        else:
            status_box.label(text=state.UIState.readiness_status)
        
        issue_box = layout.box()
        issue_box.label(text="Issue Summary", icon="ERROR")
        if state.UIState.is_scanning:
            issue_box.label(text="Analyzing...")
        else:
            issue_box.label(text=state.UIState.issue_summary)

        layout.separator()

        if state.UIState.is_scanning:
            row = layout.row()
            row.enabled = False
            row.operator(
                "checkmate.run_scan",
                text="Scanning...",
                icon="TIME"
            )
        else:
            layout.operator(
                "checkmate.run_scan",
                text="Run Scan",
                icon="PLAY"
            )

        layout.separator()

        if (
            not state.UIState.is_scanning
            and state.UIState.scan_completed
        ):

            has_results = any(
                state.UIState.validation_report.values()
            )

            if has_results:
                layout.label(
                    text="Validation Results:",
                    icon="TEXT"
                )
                results_box = layout.box()

                severity_order = [
                    Severity.ERROR,
                    Severity.WARNING,
                    Severity.INFO,
                ]

                severity_icons = {
                    Severity.ERROR: "ERROR",
                    Severity.WARNING: "QUESTION",
                    Severity.INFO: "INFO",
                }

                for severity in severity_order:

                    for group in state.UIState.validation_report.get(severity, []):

                        row = results_box.row(align=True)

                        icon = severity_icons[severity]

                        title = group["title"]
                        if group["count"] == 1:
                            title = (
                                f"{group['title']} : "
                                f"{group['message']}"
                            )
                        else:
                            title = (
                                f"{group['title']} "
                                f"({group['count']})"
                            )
                        expanded = False

                        if group["expandable"]:

                            expanded = (
                                group["title"]
                                in state.UIState.expanded_groups
                            )

                            op = row.operator(
                                "checkmate.toggle_report_group",
                                text="",
                                emboss=False,
                                icon=(
                                    "DOWNARROW_HLT"
                                    if expanded
                                    else "PLAY"
                                ),
                            )

                            op.group_title = group["title"]

                        row.label(
                            text=title,
                            icon=icon,
                        )

                        if expanded:

                            details_box = results_box.box()

                            for detail in group["details"]:

                                details_box.label(
                                    text=detail,
                                    icon="DOT"
                                )

        if (
            not state.UIState.is_scanning
            and state.UIState.scan_completed
            and state.UIState.recommendation_report
        ):

            layout.label(
                text="Recommendations:",
                icon="LIGHT"
            )
            recommendations_box = layout.box()

            for recommendation in state.UIState.recommendation_report:

                row = recommendations_box.row(align=True)

                if recommendation["expandable"]:

                    expanded = (
                        recommendation["recommendation"]
                        in state.UIState.expanded_groups
                    )

                    op = row.operator(
                        "checkmate.toggle_report_group",
                        text="",
                        emboss=False,
                        icon=(
                            "DOWNARROW_HLT"
                            if expanded
                            else "PLAY"
                        ),
                    )

                    op.group_title = recommendation["recommendation"]

                row.label(
                    text=recommendation["text"],
                    icon="DOT",
                )

                if recommendation["expandable"] and expanded:

                    details_box = recommendations_box.box()

                    for detail in recommendation["details"]:

                        details_box.label(
                            text=detail,
                            icon="DOT"
                        )