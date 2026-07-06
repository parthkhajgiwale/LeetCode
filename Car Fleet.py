def carFleet(target, position, speed):
    # Pair each car's position with its time to reach the target
    cars = [(p, (target - p) / s) for p, s in zip(position, speed)]

    # Sort cars by position (closest to target first)
    cars.sort(reverse=True)

    fleets = 0
    last_time = 0

    for pos, time in cars:
        # This car cannot catch the fleet ahead
        if time > last_time:
            fleets += 1
            last_time = time
        # Otherwise, it joins the fleet ahead

    return fleets
