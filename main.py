from eth_account import Account
from mnemonic import Mnemonic

# Enable HD wallet features
Account.enable_unaudited_hdwallet_features()

# Ask the user how many wallets to generate
num_wallets = int(input("How many Ethereum wallets do you want to create? "))

for i in range(num_wallets):
    mnemo = Mnemonic("english")
    mnemonic_phrase = mnemo.generate(strength=128)  # 12-word seed phrase
    account = Account.from_mnemonic(mnemonic_phrase)

    wallet_address = account.address
    private_key = account.key.hex()

    # Append wallet address to wallet.txt
    with open("wallet.txt", "a") as f:
        f.write(f"{wallet_address}\n")

    # Append private key and mnemonic phrase to eth_account.txt
    with open("eth_account.txt", "a") as f:
        f.write(f"Wallet {i+1}:\n")
        f.write(f"Address: {wallet_address}\n")
        f.write(f"Private Key: {private_key}\n")
        f.write(f"Seed Phrase: {mnemonic_phrase}\n")
        f.write("-" * 40 + "\n")  # Separator for readability

    print(f"Wallet {i+1} created By @itsmesatyavir: {wallet_address}")

print(f"{num_wallets} Ethereum wallets created successfully!")
