import argparse
import os
from tqdm import tqdm


parser = argparse.ArgumentParser(
    description="Preprocess Yago dataset."
)

parser.add_argument(
    "--list_dataset_literal",
    nargs="+", type=str,
    help='List of file names with literals.'
)

parser.add_argument(
    "--list_dataset_facts",
    nargs="+", type=str,
    help='List of file names with facts (relations).'
)

parser.add_argument(
    "--root_folder",
    type=str,
    help='Name of the root directory (it will be used even as output root.)'
)

if __name__ == "__main__":
    args_main = parser.parse_args()

    list_dataset_literal = args_main.list_dataset_literal
    list_dataset_facts = args_main.list_dataset_facts
    root_folder = args_main.root_folder

    list_literals = []

    for name in list_dataset_literal:
        with open("{}/{}".format(root_folder, name), 'r') as f:
            for l in tqdm(f):
                if l.startswith("#@"):
                    continue
                if "hasGloss" in l:
                    continue
                list_literals.append(l.rstrip(".\n").replace("<", "").replace(">", "")
                                     .replace("@eng", "").replace("@en", "").rstrip() + "\n")

    if not os.path.exists("{}/output/".format(root_folder)):
        os.mkdir("{}/output/".format(root_folder))

    with open("{}/output/attr_triples".format(root_folder), 'w') as f:
        f.writelines(list_literals)

    list_facts = []

    for name in list_dataset_facts:
        with open("{}/{}".format(root_folder, name), 'r') as f:
            for l in tqdm(f):
                if l.startswith("#@"):
                    continue
                if "hasGender" in l:  # Fix considering gender as a entity
                    continue
                list_facts.append(l.rstrip(".\n").replace("<", "").replace(">", "").rstrip() + "\n")

    with open("{}/output/rel_triples".format(root_folder), 'w') as f:
        f.writelines(list_facts)



