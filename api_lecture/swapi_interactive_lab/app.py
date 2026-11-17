import json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
SWAPI_BASE = "https://swapi.dev/api"

TASK_METADATA = [
    {"id": 1, "title": "Skywalker search", "difficulty": "easy", "category": "people"},
    {"id": 2, "title": "Planet summary", "difficulty": "easy", "category": "planets"},
    {"id": 3, "title": "People pagination", "difficulty": "medium", "category": "people"},
    {"id": 4, "title": "Film statistics", "difficulty": "medium", "category": "films"},
    {"id": 5, "title": "Connected characters", "difficulty": "medium", "category": "people"},
    {"id": 6, "title": "Starship comparison", "difficulty": "medium", "category": "starships"},
    {"id": 7, "title": "SWAPI dashboard", "difficulty": "hard", "category": "dashboard"},
    {"id": 8, "title": "Shared films", "difficulty": "hard", "category": "films"},
    {"id": 9, "title": "Data analyzer", "difficulty": "hard", "category": "analysis"},
    {"id": 10, "title": "Star Wars explorer", "difficulty": "hard", "category": "explorer"},
    {"id": 11, "title": "Resource graph analysis", "difficulty": "expert", "category": "graph"},
    {"id": 12, "title": "Advanced ranking engine", "difficulty": "expert", "category": "analytics"},
    {"id": 13, "title": "Path finder between characters", "difficulty": "expert", "category": "graph"},
    {"id": 14, "title": "Data quality audit", "difficulty": "expert", "category": "quality"},
    {"id": 15, "title": "SWAPI command center", "difficulty": "expert", "category": "dashboard"},
]


def fetch_json(url: str):
    request = Request(url, headers={"User-Agent": "SWAPI-Lab/1.0"})
    with urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_all_pages(endpoint: str):
    all_items = []
    next_url = f"{SWAPI_BASE}/{endpoint}/"

    while next_url:
        data = fetch_json(next_url)
        all_items.extend(data.get("results", []))
        next_url = data.get("next")

    return all_items


def task_01_skywalker_names():
    people = fetch_all_pages("people")
    names = [person["name"] for person in people if "skywalker" in person.get("name", "").lower()]

    return {
        "task_id": 1,
        "title": "Skywalker search",
        "status": "ready",
        "count": len(names),
        "results": names,
    }


def task_02_planets_summary():
    planets = fetch_all_pages("planets")
    summary = [
        {
            "name": planet.get("name", "Unknown"),
            "population": planet.get("population", "unknown"),
            "climate": planet.get("climate", "unknown"),
            "terrain": planet.get("terrain", "unknown"),
            "diameter": planet.get("diameter", "unknown"),
        }
        for planet in planets[:12]
    ]

    return {
        "task_id": 2,
        "title": "Planet summary",
        "status": "ready",
        "count": len(summary),
        "results": summary,
    }


def task_03_people_pages():
    people = fetch_all_pages("people")
    return {
        "task_id": 3,
        "title": "People pagination",
        "status": "ready",
        "total_people": len(people),
        "sample": [
            {"name": person["name"], "gender": person.get("gender", "unknown")}
            for person in people[:10]
        ],
        "message": "The pattern is: follow 'next' until it is None and accumulate results.",
    }


def task_04_film_statistics():
    films_data = fetch_json(f"{SWAPI_BASE}/films")
    films = films_data.get("results", [])

    film_stats = []
    for film in films:
        film_stats.append(
            {
                "title": film.get("title"),
                "release_date": film.get("release_date"),
                "director": film.get("director"),
                "character_count": len(film.get("characters", [])),
                "planet_count": len(film.get("planets", [])),
                "starship_count": len(film.get("starships", [])),
                "vehicle_count": len(film.get("vehicles", [])),
                "species_count": len(film.get("species", [])),
            }
        )

    sorted_films = sorted(film_stats, key=lambda item: item["character_count"], reverse=True)
    average_characters = (
        sum(item["character_count"] for item in film_stats) / len(film_stats)
        if film_stats
        else 0
    )

    return {
        "task_id": 4,
        "title": "Film statistics",
        "status": "ready",
        "top_film": sorted_films[0] if sorted_films else None,
        "average_characters": round(average_characters, 2),
        "results": film_stats,
    }


def starter_task(task_id: int):
    task = next((item for item in TASK_METADATA if item["id"] == task_id), None)
    templates = {
        11: "def task_11_resource_graph():\n    people = fetch_all_pages('people')\n    films = fetch_json(f'{SWAPI_BASE}/films')\n    # TODO: build a graph of resource links and find the most connected item\n    return {'results': []}",
        12: "def task_12_advanced_ranking():\n    people = fetch_all_pages('people')\n    planets = fetch_all_pages('planets')\n    # TODO: normalize and weight multiple metrics before sorting the results\n    return {'results': []}",
        13: "def task_13_path_finder():\n    people = fetch_all_pages('people')\n    # TODO: find the shortest path between two characters using shared films/planets/resources\n    return {'results': []}",
        14: "def task_14_data_quality_audit():\n    people = fetch_all_pages('people')\n    # TODO: detect unknown / missing / empty values and normalize them before reporting\n    return {'results': []}",
        15: "def task_15_command_center():\n    endpoints = ['people', 'planets', 'films', 'species', 'starships', 'vehicles']\n    # TODO: collect metrics from all endpoints and build a summary dashboard\n    return {'results': []}",
    }
    prompt = {
        "task_id": task_id,
        "title": task["title"] if task else f"Task {task_id}",
        "status": "starter",
        "message": "This exercise is intentionally left for students to implement. Add the logic in this function in app.py and run the task from the browser.",
        "hint": "Use SWAPI endpoints, fetch JSON, transform the data, and return a dict or list that the frontend can display.",
        "starter_template": templates.get(task_id, "def task_05_connected_characters():\n    people = fetch_all_pages('people')\n    # TODO: calculate which character appears in the most films\n    return {'results': []}"),
    }

    return prompt


def task_05_connected_characters():
    return starter_task(5)


def task_06_starship_comparison():
    return starter_task(6)


def task_07_dashboard():
    return starter_task(7)


def task_08_shared_films():
    return starter_task(8)


def task_09_data_analyzer():
    return starter_task(9)


def task_10_explorer():
    return starter_task(10)


def task_11_resource_graph():
    return starter_task(11)


def task_12_advanced_ranking():
    return starter_task(12)


def task_13_path_finder():
    return starter_task(13)


def task_14_data_quality_audit():
    return starter_task(14)


def task_15_command_center():
    return starter_task(15)


def build_task_response(task_id: int):
    dispatch = {
        1: task_01_skywalker_names,
        2: task_02_planets_summary,
        3: task_03_people_pages,
        4: task_04_film_statistics,
        5: task_05_connected_characters,
        6: task_06_starship_comparison,
        7: task_07_dashboard,
        8: task_08_shared_films,
        9: task_09_data_analyzer,
        10: task_10_explorer,
        11: task_11_resource_graph,
        12: task_12_advanced_ranking,
        13: task_13_path_finder,
        14: task_14_data_quality_audit,
        15: task_15_command_center,
    }

    handler = dispatch.get(task_id, lambda: starter_task(task_id))
    return handler()


class SWAPILabHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == "/api/tasks":
            self.send_json({"tasks": TASK_METADATA})
            return

        if parsed.path.startswith("/api/task/"):
            task_id = parsed.path.rsplit("/", 1)[-1]
            try:
                response = build_task_response(int(task_id))
            except ValueError:
                response = {"error": "Unknown task ID"}
            self.send_json(response)
            return

        return super().do_GET()

    def send_json(self, payload):
        json_bytes = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(json_bytes)))
        self.end_headers()
        self.wfile.write(json_bytes)


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8000), SWAPILabHandler)
    print("SWAPI lab is running at http://127.0.0.1:8000")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping SWAPI lab server...")
    finally:
        server.server_close()
