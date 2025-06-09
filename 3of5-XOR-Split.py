import secrets
import itertools

# Function to generate random byte string for XOR sharing
def random_bytes(length):
    return bytes(secrets.randbelow(256) for _ in range(length))

# Function to create XOR shares from a secret
def create_shares(secret, num_shares=3):
    secret_bytes = secret.encode('utf-8')
    share1 = random_bytes(len(secret_bytes))
    share2 = random_bytes(len(secret_bytes))
    share3 = bytes([s ^ b1 ^ b2 for s, b1, b2 in zip(secret_bytes, share1, share2)])
    return [share1.hex(), share2.hex(), share3.hex()]

# Combinations of shareholders (1-5) choosing 3 at a time
shareholder_combinations = list(itertools.combinations(range(1, 6), 3))
set_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Prompt user for the secret
secret = input("Enter the secret to be split: ").strip()

# Dictionary to hold all shares for each shareholder
shareholder_shares = {i: {label: None for label in set_labels} for i in range(1, 6)}

# Create shares for each combination of shareholders
for set_label, combination in zip(set_labels, shareholder_combinations):
    shares = create_shares(secret)  # Create 3 shares from the secret
    for shareholder, share in zip(combination, shares):
        shareholder_shares[shareholder][set_label] = share  # Assign the share to the shareholder

# Print the results organized by shareholder
for shareholder, sets in shareholder_shares.items():
    print(f"Shareholder {shareholder}:")
    for set_label, share in sets.items():
        if share:
            print(f"  Set {set_label}: {share}")
    print()
