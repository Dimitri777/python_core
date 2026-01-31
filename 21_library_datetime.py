"""
Portfolio: datetime and timedelta
Topic: datetime, strftime, strptime, timedelta
"""

from datetime import datetime, timedelta


def main():
    print("=== datetime Module Demo ===\n")

    # Now
    now = datetime.now()
    print("  datetime.now():", now)
    print("  Formatted (strftime):", now.strftime("%Y-%m-%d %H:%M:%S"))
    print("  Formatted (date only):", now.strftime("%A, %B %d, %Y"))

    # Parse string
    s = "2025-01-15 14:30"
    dt = datetime.strptime(s, "%Y-%m-%d %H:%M")
    print("\n  strptime('2025-01-15 14:30'):", dt)

    # timedelta
    print("\n--- timedelta ---")
    tomorrow = now + timedelta(days=1)
    print("  now + timedelta(days=1):", tomorrow.date())
    diff = tomorrow - now
    print("  timedelta between now and tomorrow (seconds):", diff.total_seconds())


if __name__ == "__main__":
    main()
