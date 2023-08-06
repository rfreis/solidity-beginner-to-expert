-include .env

build:; forge build

coverage:
	@forge coverage

contract-fund:
	@forge script script/Interactions.s.sol:FundFundMe --rpc-url $(SEPOLIA_RPC_URL) --private-key $(PRIVATE_KEY) --broadcast

contract-withdraw:
	@forge script script/Interactions.s.sol:WithdrawFundMe --rpc-url $(SEPOLIA_RPC_URL) --private-key $(PRIVATE_KEY) --broadcast

deploy:
	@forge script script/DeployFundMe.s.sol --rpc-url $(SEPOLIA_RPC_URL) --private-key $(PRIVATE_KEY) --broadcast --verify --etherscan-api-key $(ETHERSCAN_API_KEY)

snapshot:
	forge snapshot

tests:
	forge test

fork-sepolia:
	forge test --fork-url $SEPOLIA_RPC_URL
