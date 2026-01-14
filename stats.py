import glob, json, re

num_graphs = 0
for f in glob.glob("graphs/*.g6"):
    with open(f) as g:
        num_graphs += sum(1 for _ in g)

num_decks = len(glob.glob("decks/*.json"))

with open("candidate_pairs.json") as f:
    cand = json.load(f)
num_candidates = len(cand)

num_plots = len(glob.glob("plots/*.png"))

with open("README.md") as f:
    text = f.read()

text = re.sub(r"\{\{NUM_GRAPHS\}\}", str(num_graphs), text)
text = re.sub(r"\{\{NUM_DECKS\}\}", str(num_decks), text)
text = re.sub(r"\{\{NUM_CANDIDATES\}\}", str(num_candidates), text)
text = re.sub(r"\{\{NUM_PLOTS\}\}", str(num_plots), text)

with open("README.md", "w") as f:
    f.write(text)
