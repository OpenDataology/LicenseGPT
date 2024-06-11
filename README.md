# LicenseGPT
An assistant fine-tunes using large model instructions(LLM) to determine the compliance and legality of licenses.

# Road Map
We will try our best to improve our work. 
There is our road map:
- [ ] 2023/11/1 -- 1.0

# Quick Start
We conducted research on various pretrained models, including Lawyer LLaMA (PKU), Legal-ChatGLM (NJU), LaWGPT (NJU), LexiLaw (Tsinghua), ChatLaw (PKU), DISC-LawLLM (FDU), and WisdomInterrogatory (ZJU). 
Due to its simplicity and influence, we attempted initial licensing fine-tuning based on [LaWGPT](https://github.com/pengxiao-song/LaWGPT/tree/main).

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

First, execute the service startup script: 
`bash scripts/webui.sh`

Secondly, visit http://127.0.0.1:7860

3.Description of scripts
```
During the model merging phase, the merge.sh script will be run. 
Among them, 
`--base-model` is the downloaded base model path. 
`--lora_model` is the trained lora parameter path provided by LawGPT. 
`--output_dir` is the saved path of the merged model after merging parameters.
```
```
During the instruction fine-tuning phase, the fintune.sh script will be run. 
Different fine-tuned versions are recorded by setting `experiment_name`. 
`--data_path` is the data path for instruction fine-tuning. 
`--output_dir` is the checkpoint storage address generated after fine-tuning the experimental command named experiment_name. 
`--prompt_template_name` is the selected prompt template version.
```
```
In the stage of running the interactive interface, the webui.sh script will be run. 
Among them, 
`--base_model` is the base model path you choose to run. 
`--lora_weights` is the path to obtain Lora parameters. The path selected before and after fine-tuning is different. 
`--server_name` is the server address after running. 
`--share_gradio` indicates whether to enable the share_gradio service.
```

# Model Merge
Due to the fact that both LLaMA and Chinese-LLaMA have not released their model weights as open source, in accordance with the corresponding open-source license, LaWGPT can only provide LoRA weights and cannot distribute the complete model weights. However, you can obtain the original weights and independently reconstruct the model using the provided merging instructions.

1. Get the Chinese-LLaMA-7B original model weights
First, you need to obtain the original model weights of Chinese-LLaMA-7B. Here are some ways to get it for reference:

- Manual merging: Manually merge model weights according to the merging steps provided by the [Chinese-LLaMA official document](https://github.com/ymcui/Chinese-LLaMA-Alpaca)

- Search and download: model search on [Hugging Face official website](https://huggingface.co/models?search=chinese-llama)

2. Get legal-lora-7b model weights
Second, download the [legal-lora-7b model weights](https://huggingface.co/entity303/legal-lora-7b/tree/main),

Move the model weight folder to the `models/lora_weights` directory, such as `models/lora_weights/legal-lora-7b`

3. Run the merge script
Finally, merge the original Chinese-LLaMA-7B model weights and the secondary trained legal-lora-7b weights:
```
sh scripts/merge.sh
```

# Instruction Finetune
1.Refer to `fintune_data_example/finetune_law_data` to construct the instruction fine-tuning data set
2.Run `scripts/finetune.sh`

## Model Training
![image](https://github.com/OpenDataology/LicenseGPT/blob/main/assets/Instruction%20Finetune%20Training.png)
The file of our checkpoint generated after we fine-tuned it is upload to [Google Drive](https://drive.google.com/drive/folders/1URY870taz1LU-kb2MCNp3xug11_Z6RMB).

## Prompt template
You can see the prompt we tried from the file  `prompt templates`. 
Up to now, we are using the file `prompt templates/license_master_v4.json `.

# Computing resources
NVIDIA GeForce RTX 3090

# Model Evaluation
We used ChatGPT to clean the license text, and tried 8 versions of instructions and 4 versions of prompts.

![image](https://github.com/OpenDataology/LicenseGPT/blob/main/assets/efficiency.png)

The accuracy of the judgment gradually increased from 0% to 43.75%, and now it has reached an accuracy of 64.30%.
Despite the smaller scale of LicenseGPT, its tailored fine-tuning process allowed it to outperform not only its directly related predecessor, LawGPT with manual confirmation, but also other general LLMs. 

![image](https://github.com/OpenDataology/LicenseGPT/blob/main/assets/efficiency.png)

The traditional way means software IP lawyers should manually invest a substantial amount of time consulting resources and legal literature, resulting in context-specific outcomes that can take anywhere from 10 minutes to an hour, with an average of 30 minutes per case. In stark contrast, the proposed LicenseGPT's inference time spans from a swift 1 millisecond to 70 seconds at the upper end, with an average of just 10 seconds. With the help of LicenseGPT, a substantial reduction translates to an average review time for software IP lawyers of 10 minutes, representing a notable efficiency gain and freeing up valuable time for legal professionals.

# Case Study
Details in CaseStudy.md

To confirm the validity of our model, we collected 10 additional datasets along with licenses and invited three batches of Software IP Lawyers to test, with the first batch annotating the collected data with "Lawyer Review Result" as the groudtruth value for the test. The second batch of lawyers perform experiment A: read and understand the license content of the data set and make judgments. The third group of lawyers conducted Experiment B: Read and understand the results of the LicenseGPT on the content of the license and make a judgment. During this period, the three groups of lawyers do not communicate with each other. Record the accuracy rate of lawyers A and B in the experiment and the time consumed for judgment.


# Future Work
In next stage,we plan to do this things:
- [ ] Use different large legal models and try multiple instruction fine-tuning techniques to improve accuracy;
- [ ] Use multiple methods to build data sets, collect more data, clean and expand data sets;

# Contributor
This project is maintained by the following authors : [Jingwen Tan](https://github.com/viviTjwan), [Jianshan Lin](https://github.com/san5167), [Zi Li](https://github.com/li-clement).

# Cite
LawGPT: https://github.com/pengxiao-song/LaWGPT/tree/main

Chinese-LLaMA-Alpaca: https://github.com/ymcui/Chinese-LLaMA-Alpaca

LLaMA: https://github.com/facebookresearch/llama

Alpaca: https://github.com/tatsu-lab/stanford_alpaca

alpaca-lora: https://github.com/tloen/alpaca-lora
