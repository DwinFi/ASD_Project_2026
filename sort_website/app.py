from flask import Flask, render_template, request, jsonify
import importlib

app = Flask(__name__)

# Связка кнопок с файлами
ALGORITHMS = {
    "bubble": {"file": "BS_Py", "func": "beadsort", "has_logs": False},
    "gnome": {"file": "gnom_sort", "func": "gnome_sort", "has_logs": False}, # Логи убрали
    "piramida": {"file": "piramida_sort", "func": "heap_sort", "has_logs": False},
    "random": {"file": "random_sort", "func": "bogosort", "has_logs": True},
    "sleep": {"file": "sleep_sort", "func": "sleep_sort", "has_logs": False} # Новая сортировка
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort', methods=['POST'])
def sort():
    data = request.json
    algo_id = data.get('algorithm')
    arr_str = data.get('array', '')

    if algo_id not in ALGORITHMS:
        return jsonify({"error": "Алгоритм не найден!"})

    try:
        arr = [int(x) for x in arr_str.replace(',', ' ').split()]
    except ValueError:
        return jsonify({"error": "Введите только целые числа!"})

    algo_info = ALGORITHMS[algo_id]
    
    try:
        module = importlib.import_module(algo_info["file"])
        func = getattr(module, algo_info["func"])
        
        if algo_info["has_logs"]:
            result, extra = func(arr)
            if isinstance(extra, str) and extra.startswith("Ошибка"):
                return jsonify({"error": extra})
            return jsonify({"result": result, "log": extra})
        else:
            result = func(arr)
            if isinstance(result, str) and result.startswith("Ошибка"):
                return jsonify({"error": result})
            return jsonify({"result": result})
            
    except Exception as e:
        return jsonify({"error": f"Сбой в Python: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)