import hashlib
import time

# Control panel
difficulty = 4
print_switch = False


def proof_of_work(block_data, difficulty):
    target = "0" * difficulty
    if print_switch:
        print("target:", target)
    for i in range(100000000):
        test_nonce = str(i)
        hash_input_data = block_data + test_nonce
        hash_result = hashlib.sha256(hash_input_data.encode()).hexdigest()
        if print_switch:
            print(
                "||test nonce:",
                test_nonce,
                "||hash input data:",
                hash_input_data,
                "||hash value:",
                hash_result,
            )
        if hash_result[:difficulty] == target:
            return test_nonce
    return None


block_data = "Liza sends 5 BTC to Joe"
start_time = time.time()
nonce = proof_of_work(block_data, difficulty)
end_time = time.time()

print("Block:", block_data)
print("Matched nonce:", nonce)
print("Time taken:", end_time - start_time, "seconds")
