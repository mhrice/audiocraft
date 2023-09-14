from audiocraft.utils import export
import sys
import shutil

# Export
export.export_lm(sys.argv[1], "checkpoints/my_audio_lm/state_dict.bin")
export.export_pretrained_compression_model("facebook/encodec_32khz", "checkpoints/my_audio_lm/compression_state_dict.bin")
shutil.make_archive("my_audio_lm.zip", 'zip', "checkpoints/my_audio_lm/")
print("DONE")
print("Exported to my_audio_lm.zip")