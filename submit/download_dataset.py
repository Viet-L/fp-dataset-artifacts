from datasets import load_dataset
import random
def download_d():
    dataset = load_dataset("squad")
    print(dataset)
    dataset.to_json("data/squad_adversarial_AddSent.jsonl")

def keep_ad():
    pass
    # dataset = load_dataset("data\squad_adversarial_AddOneSent.jsonl")
    dataset = load_dataset("json", data_files = "data\squad_adversarial_AddSent.jsonl",split="train")
    # filter_dataset = dataset.filter(lambda keep_id: keep_id["id"].count("-") > 0)
    # filter_dataset.to_json("data/only_adversarial_AddSent.jsonl")
    print(dataset)

def move_adv():
    dataset = load_dataset("json", data_files = "data/half_only_AddOneSent.jsonl",split="train")
    dataset = dataset.map(set_rand_pos_adv)
    # dataset = dataset.map(rand_pos)
    dataset.to_json("data/rand_half.jsonl")
    return

def download_squad():
    dataset = load_dataset("squad", split="validation")
    dataset.to_json("data/valid_squad.jsonl")
    print(dataset)

def set_rand_pos_adv(example):
    arr = example["context"].split(".")
    adversarial = arr[-1]
    drop = 1
    if adversarial == "" or adversarial ==" ":
        adversarial = arr[-2]
        drop = 2
    arr = arr[:len(arr) - drop]
    insert_i = random.randint(0, len(arr))
    arr.insert(insert_i, adversarial)
    sentence = ". ".join(arr)
    if sentence[-1] != ".":
        sentence += "."
    # print(sentence)
    example["context"] = sentence
    # print(dataset[i]["context"])
    return example
    # dataset.to_json("data/rand_only_adversarial_AddOneSent.jsonl")

def rand_pos(example):
    arr = example["context"].split(".")
    random.shuffle(arr)
    sentence = ". ".join(arr)
    # print(sentence)
    example["context"] = sentence
    # print(dataset[i]["context"])
    return example


move_adv()
# download_squad()