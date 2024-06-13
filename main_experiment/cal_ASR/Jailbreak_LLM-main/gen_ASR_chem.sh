# CUDA_VISIBLE_DEVICES=6,7 nohup ./gen_ASR_chem.sh 2>&1 > ASR_chem.log &

python3 attack_chem.py --model llama-2-7b --prompt_type knowledge_prompt --subjects 化学 --use_default
python3 evaluate_chem.py --model llama-2-7b --config 'default-only' --prompt_type knowledge_prompt --subjects 化学
python3 attack_chem.py --model llama-2-7b --prompt_type generated_prompt --subjects 化学 --use_default
python3 evaluate_chem.py --model llama-2-7b --config 'default-only' --prompt_type generated_prompt --subjects 化学

python3 attack_chem.py --model llama-2-13b --prompt_type knowledge_prompt --subjects 化学 --use_default
python3 evaluate_chem.py --model llama-2-13b --config 'default-only' --prompt_type knowledge_prompt --subjects 化学
python3 attack_chem.py --model llama-2-13b --prompt_type generated_prompt --subjects 化学 --use_default
python3 evaluate_chem.py --model llama-2-13b --config 'default-only' --prompt_type generated_prompt --subjects 化学

python3 attack_chem.py --model gpt-3.5-1106 --prompt_type knowledge_prompt --subjects 化学 --use_default
python3 evaluate_chem.py --model gpt-3.5-1106 --config 'default-only' --prompt_type knowledge_prompt --subjects 化学
python3 attack_chem.py --model gpt-3.5-1106 --prompt_type generated_prompt --subjects 化学 --use_default
python3 evaluate_chem.py --model gpt-3.5-1106 --config 'default-only' --prompt_type generated_prompt --subjects 化学

python3 attack_chem.py --model gpt-4-1106 --prompt_type knowledge_prompt --subjects 化学 --use_default
python3 evaluate_chem.py --model gpt-4-1106 --config 'default-only' --prompt_type knowledge_prompt --subjects 化学
python3 attack_chem.py --model gpt-4-1106 --prompt_type generated_prompt --subjects 化学 --use_default
python3 evaluate_chem.py --model gpt-4-1106 --config 'default-only' --prompt_type generated_prompt --subjects 化学

python3 attack_chem.py --model law-chat --prompt_type knowledge_prompt --subjects 化学 --use_default
python3 evaluate_chem.py --model law-chat --config 'default-only' --prompt_type knowledge_prompt --subjects 化学
python3 attack_chem.py --model law-chat --prompt_type generated_prompt --subjects 化学 --use_default
python3 evaluate_chem.py --model law-chat --config 'default-only' --prompt_type generated_prompt --subjects 化学

python3 attack_chem.py --model finance-chat --prompt_type knowledge_prompt --subjects 化学 --use_default
python3 evaluate_chem.py --model finance-chat --config 'default-only' --prompt_type knowledge_prompt --subjects 化学
python3 attack_chem.py --model finance-chat --prompt_type generated_prompt --subjects 化学 --use_default
python3 evaluate_chem.py --model finance-chat --config 'default-only' --prompt_type generated_prompt --subjects 化学

python3 attack_chem.py --model Mistral-7B --prompt_type knowledge_prompt --subjects 化学 --use_default
python3 evaluate_chem.py --model Mistral-7B --config 'default-only' --prompt_type knowledge_prompt --subjects 化学
python3 attack_chem.py --model Mistral-7B --prompt_type generated_prompt --subjects 化学 --use_default
python3 evaluate_chem.py --model Mistral-7B --config 'default-only' --prompt_type generated_prompt --subjects 化学

python3 attack_chem.py --model vicuna-7b --prompt_type knowledge_prompt --subjects 化学 --use_default
python3 evaluate_chem.py --model vicuna-7b --config 'default-only' --prompt_type knowledge_prompt --subjects 化学
python3 attack_chem.py --model vicuna-7b --prompt_type generated_prompt --subjects 化学 --use_default
python3 evaluate_chem.py --model vicuna-7b --config 'default-only' --prompt_type generated_prompt --subjects 化学