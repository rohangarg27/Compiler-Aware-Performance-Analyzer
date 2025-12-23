from analyzer.asm import analyze_assembly
from analyzer.heuristics import generate_insights

o0 = analyze_assembly("results/asm/array_add_O0.asm")
o3 = analyze_assembly("results/asm/array_add_O3.asm")

for insight in generate_insights(o0, o3):
    print("-", insight)

