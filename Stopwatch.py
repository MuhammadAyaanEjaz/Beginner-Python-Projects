import time

print("Simple Stopwatch. Press Enter to start and Enter again to stop.")
input("Press Enter to start")
start = time.time()
input("Press Enter to stop")
end = time.time()
print("Elapsed Time:", round(end - start, 2), "seconds")
