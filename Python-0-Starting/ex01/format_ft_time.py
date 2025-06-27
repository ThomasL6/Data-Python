from datetime import datetime
now = datetime.now()
epoch_time = now.timestamp()

tms = f"{epoch_time:,.4f}"
sci = f"{epoch_time:,.2e}"

date_str = now.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {tms} or {sci} in scientific notation")
print(f"{date_str}")
