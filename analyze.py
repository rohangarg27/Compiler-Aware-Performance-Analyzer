from analyzer.asm import analyze_assembly
from analyzer.heuristics import generate_insights

def analyze_pair(name):
    o0 = analyze_assembly(f"results/asm/{name}_O0.asm")
    o3 = analyze_assembly(f"results/asm/{name}_O3.asm")

    print(f"\n=== Analysis for {name} ===")
    for insight in generate_insights(o0, o3):
        print("-", insight)

def main():
    analyze_pair("array_add")
    analyze_pair("loop")

if __name__ == "__main__":
    main()

