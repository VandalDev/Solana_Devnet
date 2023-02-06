from solathon import Client, PublicKey
from solathon.utils import sol_to_lamport
import time


class SolanaDevnet:
	def __init__(self, address, pause=20):
		self.client = Client("https://api.devnet.solana.com")
		self.address = PublicKey(address)
		self.pause = pause

	def send(amount):
		for i in range(amount // 2):
			self.client.request_airdrop(self.address, sol_to_lamport(2))
			time.sleep(self.pause)

		if amount % 2 != 0:
			self.client.request_airdrop(self.address, sol_to_lamport(1))


if __name__ == "__main__":
	devnet = SolanaDevnet("my_solana_address")
	devnet.send(50)