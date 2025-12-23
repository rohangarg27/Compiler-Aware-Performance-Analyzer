def generate_insights(o0, o3):
    insights = []

    if o3["vector_instructions"] > o0["vector_instructions"]:
        insights.append(
            "Auto-vectorization detected at higher optimization levels. "
            "Consider writing loop-friendly code (contiguous memory, no dependencies) to maximize SIMD gains."
        )

    if o3["total_instructions"] < o0["total_instructions"]:
        reduction = 100 * (1 - o3["total_instructions"] / o0["total_instructions"])
        insights.append(
            f"Instruction count reduced by approximately {reduction:.1f}%. "
            "This suggests effective loop unrolling and dead-code elimination."
        )

    if o3["scalar_instructions"] > 0 and o3["vector_instructions"] == 0:
        insights.append(
            "No vector instructions detected despite optimization. "
            "Loop-carried dependencies or data layout may be preventing vectorization."
        )

    return insights

