from collections import Counter

VECTOR_KEYWORDS = [
    "ymm", "xmm",
    "vadd", "vmul", "vsub",
    "vbroadcast", "vmovups", "vmovaps"
]

SCALAR_KEYWORDS = [
    "add", "mul", "sub",
    "mov", "cmp"
]

def analyze_assembly(asm_file):
    instr_counter = Counter()
    vector_instr = 0
    scalar_instr = 0

    with open(asm_file) as f:
        for line in f:
            if "\t" not in line:
                continue

            instr = line.split("\t")[-1].strip()
            instr_counter[instr.split()[0]] += 1

            lowered = instr.lower()

            if any(k in lowered for k in VECTOR_KEYWORDS):
                vector_instr += 1
            elif any(k in lowered for k in SCALAR_KEYWORDS):
                scalar_instr += 1

    return {
        "total_instructions": sum(instr_counter.values()),
        "vector_instructions": vector_instr,
        "scalar_instructions": scalar_instr,
        "instruction_histogram": instr_counter
    }

