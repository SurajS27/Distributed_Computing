from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/pi_x', methods=['GET'])
def pi_x():
    x = float(request.args.get('x'))
    chunk_index =int(request.args.get('chunk_index'))
    
    # Open the chunk file based on the chunk_index
    try:
        f = open(f'chunk/chunk_{chunk_index}.txt', 'r')
    except FileNotFoundError:
        return jsonify({"error": f"Chunk file 'chunk_{chunk_index}.txt' not found"}), 400
    
    l = []
    pi_value = -1
    while True:
        li = f.readline()
        if not li:
            break
        li = li.strip().split()
        try:
            li[0] = float(li[0])
            if(li[0]>=x):
                pi_value = li[1]
                break
        except:
            continue
    f.close()

    
    return jsonify({"x": x, "pi_value": pi_value})

# Correct the __name__ check
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
