# LawRT
An assistant fine-tunes using large model instructions(LLM) to determine the compliance and legality of licenses.

# Version update
2023/10/30 -- version1

# Quick Start

We conducted research on various pretrained models, including Lawyer LLaMA (PKU), Legal-ChatGLM (NJU), LaWGPT (NJU), LexiLaw (Tsinghua), ChatLaw (PKU), DISC-LawLLM (FDU), and WisdomInterrogatory (ZJU). Due to its simplicity and influence, we attempted initial licensing fine-tuning based on LaWGPT.
1.Preliminary Preparation
```
# download LaWGPT code
git clone git@github.com:pengxiao-song/LaWGPT.git
cd LaWGPT

# create enviorment
conda create -n lawgpt python=3.10 -y
conda activate lawgpt
pip install -r requirements.txt
```

2.Start web ui

First, execute the service startup script: `bash scripts/webui.sh`

Secondly, visit http://127.0.0.1:7860

# Model Merge
Due to the fact that both LLaMA and Chinese-LLaMA have not released their model weights as open source, in accordance with the corresponding open-source license, LaWGPT can only provide LoRA weights and cannot distribute the complete model weights. However, you can obtain the original weights and independently reconstruct the model using the provided merging instructions.

1. Get the Chinese-LLaMA-7B original model weights
First, you need to obtain the original model weights of Chinese-LLaMA-7B. Here are some ways to get it for reference:

Manual merging: Manually merge model weights according to the merging steps provided by the Chinese-LLaMA official document
Search and download: model search on Hugging Face official website

Move the model weight folder to the `models/base_models` directory, such as `models/base_models/chinese-llama-7b-merged`

2. Get legal-lora-7b model weights
Second, download the legal-lora-7b model weights,

Move the model weight folder to the `models/lora_weights` directory, such as `models/lora_weights/legal-lora-7b`

3. Run the merge script
Finally, merge the original Chinese-LLaMA-7B model weights and the secondary trained legal-lora-7b weights:
```
sh scripts/merge.sh
```

# Instruction Finetune
1.Refer to `finetune_law_data` to construct the instruction fine-tuning data set
2.Run `scripts/finetune.sh`

## Model Training
pic
The file `chinese-alpaca-plus-7b-law-v6` is a checkpoint file generated after we fine-tuned it.

## Prompt template
You can see the prompt we tried from the file templates. 
Up to now, we are using the file `license_master_v4.json `.

# Computing resources
NVIDIA GeForce RTX 3090

# Model Evaluation
We used ChatGPT-3 to clean the license text, and tried 8 versions of instructions and 4 versions of prompts.
 The accuracy of the judgment gradually increased from 0% to 39.3%, and now it has reached an accuracy of 52.8%.

# Future Work
In Version 2,we plan to do this things:
Use different large legal models and try multiple instruction fine-tuning techniques to improve accuracy;
Use multiple methods to build data sets, collect more data, clean and expand data sets;

# Contributors

# Acknowledgment

# Cite
https://github.com/pengxiao-song/LaWGPT/tree/main
