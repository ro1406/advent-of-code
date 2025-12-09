def merge_overlapping_ranges(intervals):
    # Sort intervals by their starting points
    intervals.sort(key=lambda x: x[0])

    merged_intervals = []
    for current_start, current_end in intervals:
        if not merged_intervals or current_start > merged_intervals[-1][1]:
            # No overlap or first interval, add it directly
            merged_intervals.append([current_start, current_end])
        else:
            # Overlap exists, merge by updating the end point
            merged_intervals[-1][1] = max(merged_intervals[-1][1], current_end)

    return merged_intervals


ranges = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        s, e = map(int, line.strip().split("-"))
        ranges.append((s, e))

unoverlapped_ranges = merge_overlapping_ranges(ranges)

ans = sum(e - s + 1 for s, e in unoverlapped_ranges)
print("ANSWER:", ans)
