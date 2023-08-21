import os
import shutil
import sys
from pathlib import Path

root_dir = Path(sys.argv[1])
audio_files = list(root_dir.rglob("**/*.mp3"))
print("Total audio files:", len(audio_files))
# 80/20 split
breakpoint = round(0.8 * len(audio_files))
train = audio_files[:breakpoint]
val = audio_files[breakpoint:]

train_dir = Path("data/train")
val_dir = Path("data/valid")
if train_dir.exists():
  shutil.rmtree(str(train_dir))
os.mkdir(train_dir)
for f in train:
  shutil.move(f, train_dir)
  shutil.move(f.with_suffix('.json'), train_dir)

if val_dir.exists():
  shutil.rmtree(str(val_dir))
os.mkdir(val_dir)
for f in val:
  shutil.move(f, val_dir)
  shutil.move(f.with_suffix('.json'), val_dir)

print("Train total audio:",  len(list(train_dir.rglob("**/*.mp3"))))
print("Train total json:", len(list(train_dir.rglob("**/*.json"))))
print("Valid total audio:", len(list(val_dir.rglob("**/*.mp3"))))
print("Valid total json:", len(list(val_dir.rglob("**/*.json"))))
