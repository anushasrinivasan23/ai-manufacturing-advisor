import ezdxf
import matplotlib.pyplot as plt
import tempfile

def plot_dxf_2d(filepath):
    doc = ezdxf.readfile(filepath)
    msp = doc.modelspace()

    fig, ax = plt.subplots()
    for e in msp:
        if e.dxftype() == 'LINE':
            start, end = e.dxf.start, e.dxf.end
            ax.plot([start[0], end[0]], [start[1], end[1]], color='black')
    ax.axis('equal')
    ax.axis('off')

    temp_png = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    plt.savefig(temp_png.name, bbox_inches='tight', pad_inches=0)
    plt.close()
    return temp_png.name
