python3 run.py --do_eval --task qa --dataset .\data\rand_squad.jsonl --model .\trained_model_addonesent --output_dir ./eval_output_addonesent/rand_squad;
python3 run.py --do_eval --task qa --dataset .\data\rand_squad.jsonl --model .\trained_model_addsent --output_dir ./eval_output_addsent/rand_squad;
python3 run.py --do_eval --task qa --dataset .\data\rand_squad.jsonl --model .\trained_model_advall --output_dir ./eval_output_advall/rand_squad;
python3 run.py --do_eval --task qa --dataset .\data\rand_squad.jsonl --model .\trained_model_original --output_dir ./eval_output_original/rand_squad;
python3 run.py --do_eval --task qa --dataset .\data\rand_squad.jsonl --model .\trained_model_original_addone --output_dir ./eval_output_original_addone/rand_squad;
python3 run.py --do_eval --task qa --dataset .\data\rand_squad.jsonl --model .\trained_model_original_addsent --output_dir ./eval_output_original_addsent/rand_squad;
python3 run.py --do_eval --task qa --dataset .\data\rand_squad.jsonl --model .\trained_model_original_halfaddonesent --output_dir ./eval_output_halfaddone/rand_squad;
