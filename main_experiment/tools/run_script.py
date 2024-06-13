import subprocess
import os

# 定义参数
project_name = "SuffixTuningForAwareness"
# model_name_or_path = "/data/MODELS/gpt2"
model_name_or_path = "/data/MODELS/Mistral-7B-v0.1"
output_dir = "./outputs/suffixtuning"
num_virtual_tokens_list = [2, 4, 8, 16]
model_short_name = model_name_or_path.split("/")[-1]


# 循环不同的num_virtual_tokens值
for num_virtual_tokens in num_virtual_tokens_list:
    run_name = f"{model_short_name}_tokens_{num_virtual_tokens}"
    this_output_dir = os.path.join(output_dir, run_name)
    command = [
        "python", "train.py",
        "--model_name_or_path", model_name_or_path,
        "--output_dir", this_output_dir,
        "--run_name", run_name,
        "--num_train_epochs", "10",
        "--evaluation_strategy", "steps",
        "--save_total_limit", "1",
        "--bf16",
        "--load_best_model_at_end",
        "--overwrite_output_dir",
        "--metric_for_best_model", "eval_loss",
        "--eval_steps", "200",
        "--logging_steps", "100",
        "--save_steps", "200",
        "--log_level", "error",
        "--seed", "0",
        "--data_seed", "0",
        "--per_device_train_batch_size", "64",
        "--num_virtual_tokens", str(num_virtual_tokens),
        "--per_gpu_eval_batch_size", "256"
    ]

    env = os.environ.copy()
    env["CUDA_VISIBLE_DEVICES"] = "0,1,2"
    env["WANDB_PROJECT"] = project_name
    env["HTTP_PROXY"]="http://127.0.0.1:7898"
    env["HTTPS_PROXY"]="http://127.0.0.1:7898"
    env["TRANSFORMERS_OFFLINE"] = "1"

    # 构建日志文件名
    log_file = f"train_suffix_num_vtokens_{num_virtual_tokens}.log"

    # 执行命令，并将输出重定向到日志文件
    with open(log_file, "wb") as f:
        process = subprocess.Popen(command, stdout=f, stderr=subprocess.STDOUT, env=env)

    # 等待命令完成（可选，如果你想同时运行所有命令，就不要等待）
    process.wait()

# 注意：这段代码直接执行会导致同时启动所有训练进程，可能会因为资源限制而出现问题。根据实际情况调整。
