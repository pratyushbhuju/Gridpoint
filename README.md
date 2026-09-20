# GRIDPOINT 📍

### Where should the warehouses go?

GRIDPOINT is a warehouse location optimization platform designed to help businesses find efficient warehouse locations based on neighborhood demand, geographic distances, and transportation costs.

The project analyzes neighborhood locations and daily orders to determine warehouse placements and delivery assignments that can reduce overall delivery costs.

## Features

- Add neighborhoods using geographic coordinates.
- Specify daily orders for each neighborhood.
- Select the number of warehouses.
- Optimize warehouse locations using mathematical optimization.
- Assign neighborhoods to warehouses.
- Calculate delivery distances and costs.
- Consider transportation modes and cost for fuels
- Set a maximum service radius.
- Visualize neighborhoods, warehouses, and assignments on an interactive map.
- Display an alternative arrangement when the requested service constraints cannot be satisfied.

## 🛠️ Technologies Used

- Python(backend)
- Django 
- NumPy
- HTML(frontend)
- CSS(frontend)
- JavaScript(frontend)
- Leaflet.js(for map visualization)

## ⚙️ How It Works

GRIDPOINT uses geographic data from neighborhoods to determine suitable warehouse locations using gradient descent to minimize cost function.

The optimization process considers:

- Neighborhood coordinates
- Daily order volume
- Number of warehouses
- Delivery cost per kilometer
- Fuel cost per kilometer
- Transportation mode
- Maximum service radius

The system attempts to minimize the total weighted delivery distance, where neighborhoods with more daily orders have a greater influence on the optimization.

## 📂 Project Structure

```text
project/
├── manage.py
├── project/
│   ├── settings.py
│   └── urls.py
└── main/
    ├── templates/
    │   └── main/
    │       ├── home.html
    │       └── warehouse.html
    ├── optimizer.py
    ├── views.py
    ├── urls.py
    └── models.py
```

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/pratyushbhuju/Gridpoint.git
```

### 2. Open the project directory

```bash
cd YOUR_REPOSITORY
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install django numpy
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open the website at:

```text
http://127.0.0.1:8000/
```

## Optimization Approach

The project uses geographic distances and weighted delivery demand to evaluate warehouse arrangements.

Neighborhoods with higher daily order volumes contribute more to the total delivery cost. The optimization process updates warehouse locations to reduce the overall weighted distance.

The project is being developed as a learning-focused optimization system, with an emphasis on understanding the mathematical principles behind the algorithm.


