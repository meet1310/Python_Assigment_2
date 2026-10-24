logs = input("Enter log entries (SUCCESS/ERROR): ").upper().split()

window_size = int(input("Enter window size: "))
limit = int(input("Enter maximum allowed errors: "))

print("\nAnomalies:")

found = False

for i in range(len(logs) - window_size + 1):
    window = logs[i:i + window_size]

    errors = window.count("ERROR")

    if errors > limit:
        print("Window", i + 1, "->", window, "ERRORS =", errors)
        found = True

if not found:
    print("No anomaly found")