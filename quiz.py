pairs = load_pairs(args.csv)
random.shuffle(pairs)

total = min(args.n, len(pairs))
correct = 0
wrong_examples = []

for i in range(total):
    pl, ua = pairs[i]
    direction = args.dir
    if direction == "both":
        direction = random.choice(["pl2ua","ua2pl"])

    if direction == "pl2ua":
        ok = ask(f"[{i+1}/{total}] Переклади польською→українською: {pl}", ua)
        if not ok: wrong_examples.append((pl, ua))
    else:
        ok = ask(f"[{i+1}/{total}] Переклади українською→польською: {ua}", pl)
        if not ok: wrong_examples.append((ua, pl))
    correct += int(ok)

print(f"Результат: {correct}/{total}")
if wrong_examples:
    print("Помилки для повтору:")
    for q,a in wrong_examples:
        print(f" - {q} → {a}")

# лог у CSV
with open("results.csv", "a", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    if f.tell() == 0:
        w.writerow(["timestamp","correct","total","direction"])
    w.writerow([datetime.datetime.now().isoformat(timespec="seconds"), correct, total, args.dir])
