import os

def split_file(file_path, num_chunks):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    total_lines = len(lines)
    chunk_size = total_lines // num_chunks
    
    for i in range(num_chunks):
        chunk_start = i * chunk_size
        chunk_end = (i + 1) * chunk_size if i < num_chunks - 1 else total_lines
        chunk_lines = lines[chunk_start:chunk_end]

        chunk_file_name = f'/home/user/Downloads/DC/chunk32/chunk_{i+1}.txt'
        with open(chunk_file_name, 'w') as chunk_file:
            chunk_file.writelines(chunk_lines)
        print(f"Created {chunk_file_name} with {len(chunk_lines)} lines.")

# Example usage
split_file('master_file.txt', 32)