def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False

    if s == goal:
        # Check if there are any repeated characters that can be swapped
        return len(set(s)) < len(s)

    diff_positions = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            diff_positions.append(i)

    if len(diff_positions) == 2:
        i, j = diff_positions
        if s[i] == goal[j] and s[j] == goal[i]:
            return True
