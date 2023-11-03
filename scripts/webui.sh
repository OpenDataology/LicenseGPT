#!/bin/bash

#微调
python webui.py \
    --load_8bit True \
    --base_model './chinese-alpaca-plus-7b-merged' \
    --lora_weights './outputs/your_checkpoint' \
    --prompt_template "license_master_v4" \
    --server_name "0.0.0.0" \
    --share_gradio True \

# #没微调
# python webui.py \
#     --load_8bit True \
#     --base_model './chinese-alpaca-plus-7b-merged' \
#     --lora_weights './outputs/your_checkpoint' \
#     --prompt_template "license_master_v4" \
#     --server_name "0.0.0.0" \
#     --share_gradio True \