import bpy
from ..gizmos.gizmo_group import update_gizmos
from ..components import components_registry


def add_component(obj, component_name):
    item = obj.hubs_component_list.items.add()
    item.name = component_name

    component_class = components_registry.get_component_by_name(component_name)
    if component_class:
        for dep_id in component_class.get_deps():
            dep_class = components_registry.get_component_by_id(dep_id)
            if dep_class:
                add_component(obj, dep_class.get_name())
            else:
                print("Dependecy '%s' from module '%s' not registered" %
                      (dep_id, component_name))


def remove_component(obj, component_name):
    items = obj.hubs_component_list.items
    items.remove(items.find(component_name))
    del obj[component_name]

    component_class = components_registry.get_component_by_name(component_name)
    if component_class:
        for dep_id in component_class.get_deps():
            dep_class = components_registry.get_component_by_id(dep_id)
            if dep_class:
                remove_component(obj, dep_class.get_name())
            else:
                print("Dependecy '%s' from module '%s' not registered" %
                      (dep_id, component_name))


def has_component(obj, component_name):
    items = obj.hubs_component_list.items
    return component_name in items


def has_components(obj, component_names):
    items = obj.hubs_component_list.items
    for name in component_names:
        if name not in items:
            return False
    return True


def add_gizmo(obj, gizmo_id):
    if not gizmo_id:
        return
    gizmo = obj.hubs_object_gizmos.add()
    gizmo.name = gizmo_id
    update_gizmos(None, bpy.context)


def remove_gizmo(obj, gizmo_id):
    gizmos = obj.hubs_object_gizmos
    gizmos.remove(gizmos.find(gizmo_id))
    update_gizmos(None, bpy.context)


def get_object_source(context, panel_type):
    if panel_type == "material":
        return context.material
    elif panel_type == "bone":
        return context.bone or context.edit_bone
    elif panel_type == "scene":
        return context.scene
    else:
        return context.object


def dash_to_title(s):
    return s.replace("-", " ").title()