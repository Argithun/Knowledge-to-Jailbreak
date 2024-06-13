# CUDA_VISIBLE_DEVICES=6,7 nohup ./gen_ASR.sh 2>&1 > ASR.log &

python3 attack.py --model llama-2-7b --prompt_type original_prompt --subjects 公安学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type original_prompt --subjects 公安学
python3 attack.py --model llama-2-7b --prompt_type original_prompt --subjects 法学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type original_prompt --subjects 法学
python3 attack.py --model llama-2-7b --prompt_type original_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type original_prompt --subjects 政治经济学
python3 attack.py --model llama-2-7b --prompt_type original_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type original_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model llama-2-7b --prompt_type original_prompt --subjects 管理学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type original_prompt --subjects 管理学
python3 attack.py --model llama-2-7b --prompt_type original_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type original_prompt --subjects 计算机科学
python3 attack.py --model llama-2-7b --prompt_type original_prompt --subjects 地理学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type original_prompt --subjects 地理学
python3 attack.py --model llama-2-7b --prompt_type original_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type original_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学

python3 attack.py --model llama-2-7b --prompt_type knowledge_prompt --subjects 公安学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type knowledge_prompt --subjects 公安学
python3 attack.py --model llama-2-7b --prompt_type knowledge_prompt --subjects 法学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type knowledge_prompt --subjects 法学
python3 attack.py --model llama-2-7b --prompt_type knowledge_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type knowledge_prompt --subjects 政治经济学
python3 attack.py --model llama-2-7b --prompt_type knowledge_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type knowledge_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model llama-2-7b --prompt_type knowledge_prompt --subjects 管理学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type knowledge_prompt --subjects 管理学
python3 attack.py --model llama-2-7b --prompt_type knowledge_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type knowledge_prompt --subjects 计算机科学
python3 attack.py --model llama-2-7b --prompt_type knowledge_prompt --subjects 地理学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type knowledge_prompt --subjects 地理学
python3 attack.py --model llama-2-7b --prompt_type knowledge_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type knowledge_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学

python3 attack.py --model llama-2-7b --prompt_type generated_prompt --subjects 公安学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type generated_prompt --subjects 公安学
python3 attack.py --model llama-2-7b --prompt_type generated_prompt --subjects 法学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type generated_prompt --subjects 法学
python3 attack.py --model llama-2-7b --prompt_type generated_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type generated_prompt --subjects 政治经济学
python3 attack.py --model llama-2-7b --prompt_type generated_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type generated_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model llama-2-7b --prompt_type generated_prompt --subjects 管理学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type generated_prompt --subjects 管理学
python3 attack.py --model llama-2-7b --prompt_type generated_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type generated_prompt --subjects 计算机科学
python3 attack.py --model llama-2-7b --prompt_type generated_prompt --subjects 地理学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type generated_prompt --subjects 地理学
python3 attack.py --model llama-2-7b --prompt_type generated_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model llama-2-7b --config 'default-only' --prompt_type generated_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学


python3 attack.py --model llama-2-13b --prompt_type original_prompt --subjects 公安学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type original_prompt --subjects 公安学
python3 attack.py --model llama-2-13b --prompt_type original_prompt --subjects 法学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type original_prompt --subjects 法学
python3 attack.py --model llama-2-13b --prompt_type original_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type original_prompt --subjects 政治经济学
python3 attack.py --model llama-2-13b --prompt_type original_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type original_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model llama-2-13b --prompt_type original_prompt --subjects 管理学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type original_prompt --subjects 管理学
python3 attack.py --model llama-2-13b --prompt_type original_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type original_prompt --subjects 计算机科学
python3 attack.py --model llama-2-13b --prompt_type original_prompt --subjects 地理学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type original_prompt --subjects 地理学
python3 attack.py --model llama-2-13b --prompt_type original_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type original_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学

python3 attack.py --model llama-2-13b --prompt_type knowledge_prompt --subjects 公安学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type knowledge_prompt --subjects 公安学
python3 attack.py --model llama-2-13b --prompt_type knowledge_prompt --subjects 法学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type knowledge_prompt --subjects 法学
python3 attack.py --model llama-2-13b --prompt_type knowledge_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type knowledge_prompt --subjects 政治经济学
python3 attack.py --model llama-2-13b --prompt_type knowledge_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type knowledge_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model llama-2-13b --prompt_type knowledge_prompt --subjects 管理学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type knowledge_prompt --subjects 管理学
python3 attack.py --model llama-2-13b --prompt_type knowledge_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type knowledge_prompt --subjects 计算机科学
python3 attack.py --model llama-2-13b --prompt_type knowledge_prompt --subjects 地理学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type knowledge_prompt --subjects 地理学
python3 attack.py --model llama-2-13b --prompt_type knowledge_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type knowledge_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学

python3 attack.py --model llama-2-13b --prompt_type generated_prompt --subjects 公安学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type generated_prompt --subjects 公安学
python3 attack.py --model llama-2-13b --prompt_type generated_prompt --subjects 法学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type generated_prompt --subjects 法学
python3 attack.py --model llama-2-13b --prompt_type generated_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type generated_prompt --subjects 政治经济学
python3 attack.py --model llama-2-13b --prompt_type generated_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type generated_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model llama-2-13b --prompt_type generated_prompt --subjects 管理学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type generated_prompt --subjects 管理学
python3 attack.py --model llama-2-13b --prompt_type generated_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type generated_prompt --subjects 计算机科学
python3 attack.py --model llama-2-13b --prompt_type generated_prompt --subjects 地理学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type generated_prompt --subjects 地理学
python3 attack.py --model llama-2-13b --prompt_type generated_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model llama-2-13b --config 'default-only' --prompt_type generated_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学


python3 attack.py --model gpt-3.5-1106 --prompt_type original_prompt --subjects 公安学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type original_prompt --subjects 公安学
python3 attack.py --model gpt-3.5-1106 --prompt_type original_prompt --subjects 法学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type original_prompt --subjects 法学
python3 attack.py --model gpt-3.5-1106 --prompt_type original_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type original_prompt --subjects 政治经济学
python3 attack.py --model gpt-3.5-1106 --prompt_type original_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type original_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model gpt-3.5-1106 --prompt_type original_prompt --subjects 管理学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type original_prompt --subjects 管理学
python3 attack.py --model gpt-3.5-1106 --prompt_type original_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type original_prompt --subjects 计算机科学
python3 attack.py --model gpt-3.5-1106 --prompt_type original_prompt --subjects 地理学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type original_prompt --subjects 地理学
python3 attack.py --model gpt-3.5-1106 --prompt_type original_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type original_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学

python3 attack.py --model gpt-3.5-1106 --prompt_type knowledge_prompt --subjects 公安学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type knowledge_prompt --subjects 公安学
python3 attack.py --model gpt-3.5-1106 --prompt_type knowledge_prompt --subjects 法学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type knowledge_prompt --subjects 法学
python3 attack.py --model gpt-3.5-1106 --prompt_type knowledge_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type knowledge_prompt --subjects 政治经济学
python3 attack.py --model gpt-3.5-1106 --prompt_type knowledge_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type knowledge_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model gpt-3.5-1106 --prompt_type knowledge_prompt --subjects 管理学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type knowledge_prompt --subjects 管理学
python3 attack.py --model gpt-3.5-1106 --prompt_type knowledge_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type knowledge_prompt --subjects 计算机科学
python3 attack.py --model gpt-3.5-1106 --prompt_type knowledge_prompt --subjects 地理学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type knowledge_prompt --subjects 地理学
python3 attack.py --model gpt-3.5-1106 --prompt_type knowledge_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type knowledge_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学

python3 attack.py --model gpt-3.5-1106 --prompt_type generated_prompt --subjects 公安学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type generated_prompt --subjects 公安学
python3 attack.py --model gpt-3.5-1106 --prompt_type generated_prompt --subjects 法学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type generated_prompt --subjects 法学
python3 attack.py --model gpt-3.5-1106 --prompt_type generated_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type generated_prompt --subjects 政治经济学
python3 attack.py --model gpt-3.5-1106 --prompt_type generated_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type generated_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model gpt-3.5-1106 --prompt_type generated_prompt --subjects 管理学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type generated_prompt --subjects 管理学
python3 attack.py --model gpt-3.5-1106 --prompt_type generated_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type generated_prompt --subjects 计算机科学
python3 attack.py --model gpt-3.5-1106 --prompt_type generated_prompt --subjects 地理学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type generated_prompt --subjects 地理学
python3 attack.py --model gpt-3.5-1106 --prompt_type generated_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model gpt-3.5-1106 --config 'default-only' --prompt_type generated_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学


python3 attack.py --model gpt-4-1106 --prompt_type original_prompt --subjects 公安学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type original_prompt --subjects 公安学
python3 attack.py --model gpt-4-1106 --prompt_type original_prompt --subjects 法学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type original_prompt --subjects 法学
python3 attack.py --model gpt-4-1106 --prompt_type original_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type original_prompt --subjects 政治经济学
python3 attack.py --model gpt-4-1106 --prompt_type original_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type original_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model gpt-4-1106 --prompt_type original_prompt --subjects 管理学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type original_prompt --subjects 管理学
python3 attack.py --model gpt-4-1106 --prompt_type original_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type original_prompt --subjects 计算机科学
python3 attack.py --model gpt-4-1106 --prompt_type original_prompt --subjects 地理学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type original_prompt --subjects 地理学
python3 attack.py --model gpt-4-1106 --prompt_type original_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type original_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学

python3 attack.py --model gpt-4-1106 --prompt_type knowledge_prompt --subjects 公安学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type knowledge_prompt --subjects 公安学
python3 attack.py --model gpt-4-1106 --prompt_type knowledge_prompt --subjects 法学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type knowledge_prompt --subjects 法学
python3 attack.py --model gpt-4-1106 --prompt_type knowledge_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type knowledge_prompt --subjects 政治经济学
python3 attack.py --model gpt-4-1106 --prompt_type knowledge_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type knowledge_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model gpt-4-1106 --prompt_type knowledge_prompt --subjects 管理学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type knowledge_prompt --subjects 管理学
python3 attack.py --model gpt-4-1106 --prompt_type knowledge_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type knowledge_prompt --subjects 计算机科学
python3 attack.py --model gpt-4-1106 --prompt_type knowledge_prompt --subjects 地理学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type knowledge_prompt --subjects 地理学
python3 attack.py --model gpt-4-1106 --prompt_type knowledge_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type knowledge_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学

python3 attack.py --model gpt-4-1106 --prompt_type generated_prompt --subjects 公安学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type generated_prompt --subjects 公安学
python3 attack.py --model gpt-4-1106 --prompt_type generated_prompt --subjects 法学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type generated_prompt --subjects 法学
python3 attack.py --model gpt-4-1106 --prompt_type generated_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type generated_prompt --subjects 政治经济学
python3 attack.py --model gpt-4-1106 --prompt_type generated_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type generated_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model gpt-4-1106 --prompt_type generated_prompt --subjects 管理学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type generated_prompt --subjects 管理学
python3 attack.py --model gpt-4-1106 --prompt_type generated_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type generated_prompt --subjects 计算机科学
python3 attack.py --model gpt-4-1106 --prompt_type generated_prompt --subjects 地理学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type generated_prompt --subjects 地理学
python3 attack.py --model gpt-4-1106 --prompt_type generated_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model gpt-4-1106 --config 'default-only' --prompt_type generated_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学


python3 attack.py --model law-chat --prompt_type original_prompt --subjects 公安学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type original_prompt --subjects 公安学
python3 attack.py --model law-chat --prompt_type original_prompt --subjects 法学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type original_prompt --subjects 法学
python3 attack.py --model law-chat --prompt_type original_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type original_prompt --subjects 政治经济学
python3 attack.py --model law-chat --prompt_type original_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type original_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model law-chat --prompt_type original_prompt --subjects 管理学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type original_prompt --subjects 管理学
python3 attack.py --model law-chat --prompt_type original_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type original_prompt --subjects 计算机科学
python3 attack.py --model law-chat --prompt_type original_prompt --subjects 地理学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type original_prompt --subjects 地理学
python3 attack.py --model law-chat --prompt_type original_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type original_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学

python3 attack.py --model law-chat --prompt_type knowledge_prompt --subjects 公安学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type knowledge_prompt --subjects 公安学
python3 attack.py --model law-chat --prompt_type knowledge_prompt --subjects 法学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type knowledge_prompt --subjects 法学
python3 attack.py --model law-chat --prompt_type knowledge_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type knowledge_prompt --subjects 政治经济学
python3 attack.py --model law-chat --prompt_type knowledge_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type knowledge_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model law-chat --prompt_type knowledge_prompt --subjects 管理学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type knowledge_prompt --subjects 管理学
python3 attack.py --model law-chat --prompt_type knowledge_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type knowledge_prompt --subjects 计算机科学
python3 attack.py --model law-chat --prompt_type knowledge_prompt --subjects 地理学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type knowledge_prompt --subjects 地理学
python3 attack.py --model law-chat --prompt_type knowledge_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type knowledge_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学

python3 attack.py --model law-chat --prompt_type generated_prompt --subjects 公安学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type generated_prompt --subjects 公安学
python3 attack.py --model law-chat --prompt_type generated_prompt --subjects 法学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type generated_prompt --subjects 法学
python3 attack.py --model law-chat --prompt_type generated_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type generated_prompt --subjects 政治经济学
python3 attack.py --model law-chat --prompt_type generated_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type generated_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model law-chat --prompt_type generated_prompt --subjects 管理学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type generated_prompt --subjects 管理学
python3 attack.py --model law-chat --prompt_type generated_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type generated_prompt --subjects 计算机科学
python3 attack.py --model law-chat --prompt_type generated_prompt --subjects 地理学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type generated_prompt --subjects 地理学
python3 attack.py --model law-chat --prompt_type generated_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model law-chat --config 'default-only' --prompt_type generated_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学


python3 attack.py --model finance-chat --prompt_type original_prompt --subjects 公安学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type original_prompt --subjects 公安学
python3 attack.py --model finance-chat --prompt_type original_prompt --subjects 法学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type original_prompt --subjects 法学
python3 attack.py --model finance-chat --prompt_type original_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type original_prompt --subjects 政治经济学
python3 attack.py --model finance-chat --prompt_type original_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type original_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model finance-chat --prompt_type original_prompt --subjects 管理学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type original_prompt --subjects 管理学
python3 attack.py --model finance-chat --prompt_type original_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type original_prompt --subjects 计算机科学
python3 attack.py --model finance-chat --prompt_type original_prompt --subjects 地理学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type original_prompt --subjects 地理学
python3 attack.py --model finance-chat --prompt_type original_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type original_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学

python3 attack.py --model finance-chat --prompt_type knowledge_prompt --subjects 公安学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type knowledge_prompt --subjects 公安学
python3 attack.py --model finance-chat --prompt_type knowledge_prompt --subjects 法学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type knowledge_prompt --subjects 法学
python3 attack.py --model finance-chat --prompt_type knowledge_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type knowledge_prompt --subjects 政治经济学
python3 attack.py --model finance-chat --prompt_type knowledge_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type knowledge_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model finance-chat --prompt_type knowledge_prompt --subjects 管理学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type knowledge_prompt --subjects 管理学
python3 attack.py --model finance-chat --prompt_type knowledge_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type knowledge_prompt --subjects 计算机科学
python3 attack.py --model finance-chat --prompt_type knowledge_prompt --subjects 地理学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type knowledge_prompt --subjects 地理学
python3 attack.py --model finance-chat --prompt_type knowledge_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type knowledge_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学

python3 attack.py --model finance-chat --prompt_type generated_prompt --subjects 公安学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type generated_prompt --subjects 公安学
python3 attack.py --model finance-chat --prompt_type generated_prompt --subjects 法学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type generated_prompt --subjects 法学
python3 attack.py --model finance-chat --prompt_type generated_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type generated_prompt --subjects 政治经济学
python3 attack.py --model finance-chat --prompt_type generated_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type generated_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model finance-chat --prompt_type generated_prompt --subjects 管理学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type generated_prompt --subjects 管理学
python3 attack.py --model finance-chat --prompt_type generated_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type generated_prompt --subjects 计算机科学
python3 attack.py --model finance-chat --prompt_type generated_prompt --subjects 地理学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type generated_prompt --subjects 地理学
python3 attack.py --model finance-chat --prompt_type generated_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model finance-chat --config 'default-only' --prompt_type generated_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学


python3 attack.py --model Mistral-7B --prompt_type original_prompt --subjects 公安学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type original_prompt --subjects 公安学
python3 attack.py --model Mistral-7B --prompt_type original_prompt --subjects 法学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type original_prompt --subjects 法学
python3 attack.py --model Mistral-7B --prompt_type original_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type original_prompt --subjects 政治经济学
python3 attack.py --model Mistral-7B --prompt_type original_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type original_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model Mistral-7B --prompt_type original_prompt --subjects 管理学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type original_prompt --subjects 管理学
python3 attack.py --model Mistral-7B --prompt_type original_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type original_prompt --subjects 计算机科学
python3 attack.py --model Mistral-7B --prompt_type original_prompt --subjects 地理学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type original_prompt --subjects 地理学
python3 attack.py --model Mistral-7B --prompt_type original_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type original_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学

python3 attack.py --model Mistral-7B --prompt_type knowledge_prompt --subjects 公安学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type knowledge_prompt --subjects 公安学
python3 attack.py --model Mistral-7B --prompt_type knowledge_prompt --subjects 法学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type knowledge_prompt --subjects 法学
python3 attack.py --model Mistral-7B --prompt_type knowledge_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type knowledge_prompt --subjects 政治经济学
python3 attack.py --model Mistral-7B --prompt_type knowledge_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type knowledge_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model Mistral-7B --prompt_type knowledge_prompt --subjects 管理学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type knowledge_prompt --subjects 管理学
python3 attack.py --model Mistral-7B --prompt_type knowledge_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type knowledge_prompt --subjects 计算机科学
python3 attack.py --model Mistral-7B --prompt_type knowledge_prompt --subjects 地理学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type knowledge_prompt --subjects 地理学
python3 attack.py --model Mistral-7B --prompt_type knowledge_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type knowledge_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学

python3 attack.py --model Mistral-7B --prompt_type generated_prompt --subjects 公安学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type generated_prompt --subjects 公安学
python3 attack.py --model Mistral-7B --prompt_type generated_prompt --subjects 法学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type generated_prompt --subjects 法学
python3 attack.py --model Mistral-7B --prompt_type generated_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type generated_prompt --subjects 政治经济学
python3 attack.py --model Mistral-7B --prompt_type generated_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type generated_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model Mistral-7B --prompt_type generated_prompt --subjects 管理学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type generated_prompt --subjects 管理学
python3 attack.py --model Mistral-7B --prompt_type generated_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type generated_prompt --subjects 计算机科学
python3 attack.py --model Mistral-7B --prompt_type generated_prompt --subjects 地理学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type generated_prompt --subjects 地理学
python3 attack.py --model Mistral-7B --prompt_type generated_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model Mistral-7B --config 'default-only' --prompt_type generated_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学


python3 attack.py --model vicuna-7b --prompt_type original_prompt --subjects 公安学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type original_prompt --subjects 公安学
python3 attack.py --model vicuna-7b --prompt_type original_prompt --subjects 法学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type original_prompt --subjects 法学
python3 attack.py --model vicuna-7b --prompt_type original_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type original_prompt --subjects 政治经济学
python3 attack.py --model vicuna-7b --prompt_type original_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type original_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model vicuna-7b --prompt_type original_prompt --subjects 管理学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type original_prompt --subjects 管理学
python3 attack.py --model vicuna-7b --prompt_type original_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type original_prompt --subjects 计算机科学
python3 attack.py --model vicuna-7b --prompt_type original_prompt --subjects 地理学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type original_prompt --subjects 地理学
python3 attack.py --model vicuna-7b --prompt_type original_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type original_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学

python3 attack.py --model vicuna-7b --prompt_type knowledge_prompt --subjects 公安学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type knowledge_prompt --subjects 公安学
python3 attack.py --model vicuna-7b --prompt_type knowledge_prompt --subjects 法学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type knowledge_prompt --subjects 法学
python3 attack.py --model vicuna-7b --prompt_type knowledge_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type knowledge_prompt --subjects 政治经济学
python3 attack.py --model vicuna-7b --prompt_type knowledge_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type knowledge_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model vicuna-7b --prompt_type knowledge_prompt --subjects 管理学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type knowledge_prompt --subjects 管理学
python3 attack.py --model vicuna-7b --prompt_type knowledge_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type knowledge_prompt --subjects 计算机科学
python3 attack.py --model vicuna-7b --prompt_type knowledge_prompt --subjects 地理学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type knowledge_prompt --subjects 地理学
python3 attack.py --model vicuna-7b --prompt_type knowledge_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type knowledge_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学

python3 attack.py --model vicuna-7b --prompt_type generated_prompt --subjects 公安学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type generated_prompt --subjects 公安学
python3 attack.py --model vicuna-7b --prompt_type generated_prompt --subjects 法学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type generated_prompt --subjects 法学
python3 attack.py --model vicuna-7b --prompt_type generated_prompt --subjects 政治经济学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type generated_prompt --subjects 政治经济学
python3 attack.py --model vicuna-7b --prompt_type generated_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type generated_prompt --subjects 公安学 社会学 政治经济学 unknown 网络安全 法学 心理学
python3 attack.py --model vicuna-7b --prompt_type generated_prompt --subjects 管理学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type generated_prompt --subjects 管理学
python3 attack.py --model vicuna-7b --prompt_type generated_prompt --subjects 计算机科学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type generated_prompt --subjects 计算机科学
python3 attack.py --model vicuna-7b --prompt_type generated_prompt --subjects 地理学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type generated_prompt --subjects 地理学
python3 attack.py --model vicuna-7b --prompt_type generated_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学 --use_default
python3 evaluate.py --model vicuna-7b --config 'default-only' --prompt_type generated_prompt --subjects 化学 物理学 药学 地理学 计算机科学 管理学