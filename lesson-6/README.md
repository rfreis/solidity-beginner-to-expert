# Lesson 6 - Foundry Simple Storage

This lessons teaches us how to use [Foundry](https://getfoundry.sh/) to setup a local development environment. Important topics from this lessons are:

- how to use Foundry
    - forge commands
    - anvil commands
    - cast commands
- how to use other tools
    - ganache to run a similar local node like anvil but with some UX
    - alchemy - node as a service
- using Foundry, how to deploy using [Scripts](./script/DeploySimpleStorage.s.sol) in Solidity

The original repository for this class can be found [here](https://github.com/Cyfrin/foundry-simple-storage-f23)


Some useful commands:

```bash
forge --init .
forge create SimpleStorage
forge build
forge compile
forge script script/DeploySimpleStorage.s.sol --rpc-url http://127.0.0.1:8545 --broadcast --private-key 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80 # anvil dummy key
forge fmt

anvil

cast call
cast send
```

# Extra mile

For this lesson, thought would be a good idea to setup a pre-commit hook to format `.sol` files using `forge fmt` and extend github action to do together with the tests a style checking on new commits/PRs to the main branch.
