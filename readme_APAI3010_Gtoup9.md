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

Improvement:
- **v0 are not used**
v0 are for back up or some initial version

- Usage

  - r_precision.py <br>
  For prompt seperation
  --text is for the prompt following the author of stable dream fusion
  --workspace is the workspace folder which will be created for every prompt fed into stable dreamfusion
  --latest is which ckpt is used. Stable dream fusion record every epoch data. Normally is ep0100 unless the training is not finished or we further extend the training
  --mode has choices of rgb and depth which is correspondent to color and texture result as original paper Figure 5: Qualitative comparison with baselines.
  --clip has choices of clip-ViT-B-32, CLIP B/16, CLIP L/14, same as original paper

    python Prompt.py --text "matte painting of a castle made of cheesecake surrounded by a moat made of ice cream" --workspace ../castle --latest ep0100 --mode rgb --clip clip-ViT-B-32

  - Prompt.py (model name case sensitive)
  For prompt seperation
  --text is for the prompt following the author of stable dream fusion
  --model is for choose the pretrain models

    python Prompt.py --text "a dog is in front of a rabbit" --model vlt5
    python Prompt.py --text "a dog is in front of a rabbit" --model bert
    python Prompt.py --text "a dog is in front of a rabbit" --model XLNet

  - RelNet.ipynb
  For original trial, run it in jupyter notebook

  - Relnet_data.py
  For generate some demo data for Relnet, 0 mean original, 1/-1 mean opposite direction in x/y/z axis. 99 mean random number for randomness

    python Relnet_data.py

  - mesh_to_video.py
  --center_obj IS THE CENTER OBJECT
  --surround_obj IS THE SURROUNDING OBJECT SUBJECT TO CHANGE
  --transform_vector THE X Y Z 3d vector for transform

    python mesh_to_video.py --center_obj 'mesh_whiterabbit/mesh.obj' --surround_obj 'mesh_snake/mesh.obj' --transform_vector [1,0,0]






RunningDemo:    
    All the prompt we run is in the ipynb files
