from gizmo_info import GizmoInfo
from .hubs_gizmo import stock_gizmo_update

AUDIO_ZONE = GizmoInfo(
    name="Audio Zone",
    type="GIZMO_GT_cage_3d",
    styles=('BOX'),
    color = (0.0, 0.8, 0.0),
    color_highlight = (0.0, 1.0, 0.0),
    draw_options=[],
    update=stock_gizmo_update
)