import numpy as np
from math import radians, sin, cos, sqrt, asin


R = 6371
KM_PER_DEGREE = 111.32


def calculate_distance(a, b):

    lat1 = radians(a["latitude"])
    lat2 = radians(b["latitude"])

    dlat = radians(b["latitude"] - a["latitude"])
    dlon = radians(b["longitude"] - a["longitude"])

    x = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

    return 2 * R * asin(sqrt(x))


mode_factor = {
    "bike": 0.5,
    "van": 1.0,
    "truck": 1.5
}


def optimize(neighborhoods, k, delivery_cost, fuel_cost, transport_mode, max_radius):

    fuel_factor = mode_factor.get(transport_mode, 1.0)

    lat0 = np.mean([n["latitude"] for n in neighborhoods])
    lon0 = np.mean([n["longitude"] for n in neighborhoods])

    points = []

    for neighborhood in neighborhoods:

        x = (neighborhood["longitude"] - lon0) * KM_PER_DEGREE * np.cos(np.radians(lat0))
        y = (neighborhood["latitude"] - lat0) * KM_PER_DEGREE

        points.append([x, y])

    points = np.array(points)

    indices = np.random.choice(len(points), k, replace=False)
    warehouses = points[indices].copy()

    learning_rate = 0.00001
    epochs = 10001

    for epoch in range(epochs):

        gradients = np.zeros((k, 2))

        for i, neighborhood in enumerate(neighborhoods):

            min_distance = np.inf
            nearest = -1

            for j, warehouse in enumerate(warehouses):

                dx = warehouse[0] - points[i][0]
                dy = warehouse[1] - points[i][1]

                distance = np.sqrt(dx**2 + dy**2)

                if distance < min_distance:

                    min_distance = distance
                    nearest = j

            weight = neighborhood["orders"] * (
                fuel_cost * fuel_factor + delivery_cost
            )

            dx = warehouses[nearest][0] - points[i][0]
            dy = warehouses[nearest][1] - points[i][1]

            if min_distance > 0:

                gradients[nearest][0] += weight * dx / min_distance
                gradients[nearest][1] += weight * dy / min_distance

        warehouses -= learning_rate * gradients

    best_warehouses = []

    for i, warehouse in enumerate(warehouses):

        latitude = lat0 + warehouse[1] / KM_PER_DEGREE

        longitude = lon0 + warehouse[0] / (
            KM_PER_DEGREE * np.cos(np.radians(lat0))
        )

        best_warehouses.append({
            "name": f"Warehouse {i + 1}",
            "latitude": latitude,
            "longitude": longitude
        })

    best_assignments = []
    best_cost = 0
    valid = True

    for neighborhood in neighborhoods:

        min_distance = float("inf")
        assigned_warehouse = None

        for warehouse in best_warehouses:

            distance = calculate_distance(neighborhood, warehouse)

            if distance < min_distance:

                min_distance = distance
                assigned_warehouse = warehouse

        if min_distance > max_radius:

            valid = False

        transport_cost = min_distance * fuel_cost * fuel_factor
        delivery_cost_total = min_distance * delivery_cost

        best_cost += (
            transport_cost + delivery_cost_total
        ) * neighborhood["orders"]

        best_assignments.append({
            "neighborhood": neighborhood["name"],
            "latitude": neighborhood["latitude"],
            "longitude": neighborhood["longitude"],
            "warehouse": assigned_warehouse["name"],
            "distance": min_distance
        })

    if valid:
        message = "A valid solution was found within the given service radius."
    else:
        message = (
            "According to the given warehouse and service radius conditions, "
            "a solution is not possible. If the service radius condition is "
            "disregarded, this is the best warehouse arrangement found."
        )

    return {
        "cost": best_cost,
        "warehouses": best_warehouses,
        "assignments": best_assignments,
        "valid": valid,
        "message": message
    }