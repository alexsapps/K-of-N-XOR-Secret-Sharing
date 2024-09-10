# Function to reconstruct the secret from 3 shares
def reconstruct_secret(share1_hex, share2_hex, share3_hex):
    # Convert hex shares back to bytes
    share1 = bytes.fromhex(share1_hex)
    share2 = bytes.fromhex(share2_hex)
    share3 = bytes.fromhex(share3_hex)

    # XOR the 3 shares to recover the secret
    secret_bytes = bytes([b1 ^ b2 ^ b3 for b1, b2, b3 in zip(share1, share2, share3)])

    try:
        secret = secret_bytes.decode('utf-8')
        return secret
    except UnicodeDecodeError:
        return None

# Prompt the user for 3 shares
def prompt_for_shares():
    print("Enter 3 shares (hex format) to reconstruct the secret:")
    share1 = input("Share 1: ").strip()
    share2 = input("Share 2: ").strip()
    share3 = input("Share 3: ").strip()
    
    # Attempt to reconstruct the secret
    secret = reconstruct_secret(share1, share2, share3)
    if secret:
        print(f"\nReconstructed Secret: {secret}")
    else:
        print("\nError: Could not decode the secret, please check the input shares.")

# Run the prompt
if __name__ == "__main__":
    prompt_for_shares()
