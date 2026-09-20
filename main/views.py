from django.shortcuts import render
from .optimizer import optimize

def warehouse(request):
    if request.method == "POST":
        names = request.POST.getlist("name")
        latitudes = request.POST.getlist("latitude")
        longitudes = request.POST.getlist("longitude")
        orders = request.POST.getlist("daily_orders")

        neighborhoods = []

        for i in range(len(names)):
            neighborhoods.append({
                "name": names[i],
                "latitude": float(latitudes[i]),
                "longitude": float(longitudes[i]),
                "orders": int(orders[i])
            })

        request.session["neighborhoods"] = neighborhoods

        k = int(request.POST["number_of_warehouses"])
        delivery_cost = float(request.POST["delivery_cost_per_km"])
        fuel_cost = float(request.POST["fuel_cost_per_km"])
        transport_mode = request.POST["transportation_mode"]
        max_radius = float(request.POST["maximum_service_radius"])

        result = optimize(neighborhoods, k, delivery_cost, fuel_cost, transport_mode, max_radius)

        return render(request, "main/results.html", {"result": result})

    neighborhoods = request.session.get("neighborhoods", [])

    return render(request, "main/index.html", {
        "neighborhoods": neighborhoods
    })
def index(request):
    return render(request,"main/home.html")