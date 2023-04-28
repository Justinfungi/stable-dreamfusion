import os
import numpy as np
import trimesh
import argparse
from pathlib import Path
from tqdm import tqdm

def generate_frames(anim_mesh, outfile_path, num_frames=100):

    print('Generating frames ...')
    for frame_num in tqdm(range(num_frames)):
        angle_deg = frame_num * 2 * np.pi / 100
        R = np.array([
            [np.cos(angle_deg), -np.sin(angle_deg), 0],
            [np.sin(angle_deg), np.cos(angle_deg), 0],
            [0, 0, 1]
        ])

        rotated_mesh = anim_mesh.copy()
        rotated_mesh.vertices = np.dot(rotated_mesh.vertices, R.T)

        outfile = os.path.join(out_dir,f'frame_{frame_num:05d}.obj')
        rotated_mesh.export(outfile)
    print("----> rotation done")


def render_video(in_path, out_path):

    print('Rendering video ...')
    cmd = f"ffmpeg -i {in_path} -vcodec libx264 -qscale:v 2 -b:v 1500k {out_path}"
    os.system(cmd)
    print(f'Video saved to {out_path}')

def generate_mesh(obj1,obj2,transform_vector):

    # Read 2 objects
    filename1 = obj1 # Central Object
    filename2 = obj2 # Surrounding Object
    mesh1 = trimesh.load_mesh(filename1)
    mesh2 = trimesh.load_mesh(filename2)

    extents1 = mesh1.extents
    extents2 = mesh1.extents
    
    radius1 = sum(extents1) / 3.0
    radius2 = sum(extents2) / 3.0

    center1 = mesh1.center_mass
    center2 = mesh2.center_mass

    # Move
    T1 = -center1
    new =[]
    for i in transform_vector:
        try:
            new.append(float(i))*radius1
        except:
            pass
    transform_vector = new
    print(T1, transform_vector, radius1)
    T2 = -center2 + transform_vector

    # Transform
    mesh1.apply_translation(T1)
    mesh2.apply_translation(T2)

    # merge mesh
    merged_mesh = trimesh.util.concatenate((mesh1, mesh2))

    # save mesh
    merged_mesh.export('merged_mesh.obj')
    print("----> merge mesh done")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate rotating mesh animation.')
    parser.add_argument('--center_obj', type=str, help='Input OBJ1 file.')
    parser.add_argument('--surround_obj', type=str, help='Input OBJ2 file.')
    parser.add_argument('--transform_vector', help='Transform_vector.')
    parser.add_argument('--output_file', type=str, default="result/Demo.mp4", help='Output MP4 file.')
    parser.add_argument('--num_frames', type=int, default=100, help='Number of frames to render.')
    args = parser.parse_args()
    
    #mesh = obj.Obj("wr.obj")
    generate_mesh(args.center_obj,args.surround_obj,args.transform_vector)

    input_file = Path("merged_mesh.obj")
    output_file = Path(args.output_file)

    out_dir = output_file.parent.joinpath('frames')
    out_dir.mkdir(parents=True, exist_ok=True)

    anim_mesh = trimesh.load_mesh(str(input_file))

    generate_frames(anim_mesh, args.output_file, num_frames=args.num_frames)

    render_video(os.path.join(out_dir,'frame_%05d.obj'), str(output_file))

