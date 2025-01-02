import time

print("Cronómetro en formato hh:mm:ss.")
print("-------------------------------")

hours = 0
minutes = 0
seconds = 0

print("Presiona Ctrl+C para detener el cronómetro.")

try:
    while True:
        print(f"\r{hours:02}:{minutes:02}:{seconds:02}", end="")
        time.sleep(1)
        seconds += 1

        if seconds == 60:
            seconds = 0
            minutes += 1

        if minutes == 60:
            minutes = 0
            hours += 1

except KeyboardInterrupt:
    print("\nCronómetro detenido.")

print(f"Tiempo total: {hours:02}:{minutes:02}:{seconds:02}")
