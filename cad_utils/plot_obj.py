import trimesh
import plotly.graph_objects as go

def plot_obj_3d(filepath):
    mesh = trimesh.load(filepath)
    fig = go.Figure(data=[go.Mesh3d(
        x=mesh.vertices[:, 0],
        y=mesh.vertices[:, 1],
        z=mesh.vertices[:, 2],
        i=mesh.faces[:, 0],
        j=mesh.faces[:, 1],
        k=mesh.faces[:, 2],
        opacity=0.5
    )])
    fig.update_layout(scene=dict(xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False)))
    return fig
