import requests

def send_input_to_worker(worker_url, input_data):
    try:
        response = requests.post(worker_url, json={'input': input_data})
        if response.status_code == 200:
            print(f"Sent '{input_data}' to {worker_url}")
        else:
            print(f"Failed to send data to {worker_url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending data to {worker_url}: {e}")

if __name__ == "__main__":
    # Specify the single worker URL directly
    worker_url = "http://worker:5000/process"

    while True:
        user_input = input("Enter input for worker (or type 'exit' to stop): ")
        if user_input.lower() == "exit":
            break

        # Send input to the single worker
        send_input_to_worker(worker_url, user_input)
