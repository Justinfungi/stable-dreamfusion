Instructor:
- Dr. Kai Han

Teaching Assistant:
- Mr. Hongjun Wang

Groupmates:
- Fung Ho Kit 3035779105
- Zhang Yuhan 3035771672
- Jing Jingderong 3035771775

Group Project topic:
- Dream fusion https://arxiv.org/pdf/2209.14988.pdf

### Improvement:
- **v0 are not used**
v0 are for back up or some initial version

- Usage

  - r_precision.py <br>
  For prompt seperation <br>
  --text is for the prompt following the author of stable dream fusion <br>
  --workspace is the workspace folder which will be created for every prompt fed into stable dreamfusion <br>
  --latest is which ckpt is used. Stable dream fusion record every epoch data. Normally is ep0100 unless the training is not finished or we further extend the training <br>
  --mode has choices of rgb and depth which is correspondent to color and texture result as original paper Figure 5: Qualitative comparison with baselines. <br>
  --clip has choices of clip-ViT-B-32, CLIP B/16, CLIP L/14, same as original paper <br>

      ```bash
      python Prompt.py --text "matte painting of a castle made of cheesecake surrounded by a moat made of ice cream" --workspace ../castle --latest ep0100 --mode rgb --clip clip-ViT-B-32
      ```

  - Prompt.py (model name case sensitive) <br>
  For prompt seperation <br> <br>
  --text is for the prompt following the author of stable dream fusion <br>
  --model is for choose the pretrain models <br>

      ```bash
      python Prompt.py --text "a dog is in front of a rabbit" --model vlt5
      python Prompt.py --text "a dog is in front of a rabbit" --model bert
      python Prompt.py --text "a dog is in front of a rabbit" --model XLNet
      ```

  - RelNet.ipynb <br>
  For original trial, run it in jupyter notebook <br>

  - Relnet_data.py <br>
  For generate some demo data for Relnet, 0 mean original, 1/-1 mean opposite direction in x/y/z axis. 99 mean random number for randomness <br>

      ```bash
      python Relnet_data.py
      ```

  - mesh_to_video.py <br>
  --center_obj IS THE CENTER OBJECT <br>
  --surround_obj IS THE SURROUNDING OBJECT SUBJECT TO CHANGE <br>
  --transform_vector THE X Y Z 3d vector for transform <br>

      ```bash
      python mesh_to_video.py --center_obj 'mesh_whiterabbit/mesh.obj' --surround_obj 'mesh_snake/mesh.obj' --transform_vector [1,0,0]
      ```

### RunningDemo:    
    All the prompt we run is in the ipynb files. While the prompt are similar
    There could be 3 part:

    # Training
    python main.py --text "a hamburger" --workspace trial -O

    # DMTet
    python main.py -O --text "a hamburger" --workspace trial_dmtet --dmtet --iters 5000 --init_ckpt trial/checkpoints/df.pth

    # For display
    import os
    import glob
    from IPython.display import HTML
    from base64 import b64encode

    def get_latest_file(path):
      dir_list = glob.glob(path)
      dir_list.sort(key=lambda x: os.path.getmtime(x))
      return dir_list[-1]

    def show_video(video_path, video_width = 600):

      video_file = open(video_path, "r+b").read()
      video_url = f"data:video/mp4;base64,{b64encode(video_file).decode()}"

      return HTML(f"""<video width={video_width} controls><source src="{video_url}"></video>""")

    rgb_video = get_latest_file(os.path.join(Workspace, 'resu
    lts', '*_rgb.mp4'))
    show_video(rgb_video)




import glob
def load_dataset(path, num_per_class):
    input = []
    labels = []
    for id, class_name in class_names.items():
        img_path_class = glob.glob(path + class_name + '/*')
        img_path_class = img_path_class[:num_per_class]
        labels.extend([id]*len(img_path_class))
        for filename in img_path_class:
            data.append(cv2.imread(filename, 0))
    return data, labels


n_train = 90
n_test = 90
train_data, train_label = load_dataset('./Q3/data/train/', n_train)
test_data, test_label = load_dataset('./Q3/data/test/', n_test)
