from tnlearn import generate_for_combo
from tnlearn.random_formula import count_terms

candidates = generate_for_combo(
    term_target=1,
    x_target=2,
    count=3,
    max_attempts=40,
    random_state=42,
)
unique_candidates = list(dict.fromkeys(candidates))

if not unique_candidates:
    print("No matching formulas within this attempt budget.")
for formula in unique_candidates:
    assert count_terms(formula) == 1
    assert formula.count("x") == 2
    print(formula)
print("Candidates:", len(candidates), "Unique:", len(unique_candidates))
