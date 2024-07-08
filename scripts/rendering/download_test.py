import objaverse
import objaverse.xl as oxl
from scripts.rendering.main import render_objects
import fire
from tqdm import tqdm
import time
print("Preparing to download annotations...")
annotations = oxl.get_alignment_annotations(
    download_dir="~/.objaverse" # default download directory
)
annotations = annotations[annotations["source"] == "github"].reset_index(drop=True) #only sketchfab and github
 
for i in tqdm(range(1600, 10000)):
    try:
        print(f"Processing render iteration {i:05d}...")
        render_objects(object_df=annotations[5*i:5*i+5],
                    render_dir="/home/v-shikao/data/",
                    render_timeout=900,
                    num_renders=100)
    except:
        time.sleep(500)