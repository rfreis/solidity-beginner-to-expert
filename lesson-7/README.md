# Lesson 7 - Foundry Fund Me

This lessons teaches us how to do a lot of things with [Foundry](https://getfoundry.sh/). Tried to list some of them below:

- make our code modular to do dynamic deploys with scripts
- fork a test, using a contract on a testnet or mainnet
- unit tests
- integrations tests
- gas optimization
- understading storage

The original repository for this class can be found [here](https://github.com/Cyfrin/foundry-fund-me-f23)

## My personal on chain development

- Fund Me contract deployed on Sepolia (`make deploy`)
[0x68Ef3989F7282e86D663C1e3744B8847826667a2](https://sepolia.etherscan.io/address/0x68Ef3989F7282e86D663C1e3744B8847826667a2)
    - Transaction [0x50a193580d56aaa512fd57bb606e2401a1dba074ed97b4b408f6dfe57222a17c](https://sepolia.etherscan.io/tx/0x50a193580d56aaa512fd57bb606e2401a1dba074ed97b4b408f6dfe57222a17c)
- Fund contract with 0.1 ETH (`make contract-fund`)
    - Transaction [0x9f8a5b5ae05a3de219d4655214c74e92cc760a7085ba5d0a7fad6ed5796450ac](https://sepolia.etherscan.io/tx/0x9f8a5b5ae05a3de219d4655214c74e92cc760a7085ba5d0a7fad6ed5796450ac)
- Withdrawal TX (`make contract-withdraw`)
    - Transaction [0x52b9593b0cc8618c54e723e868bc79393974a8d4f1a44ec454d6abe0d3908baa](https://sepolia.etherscan.io/tx/0x52b9593b0cc8618c54e723e868bc79393974a8d4f1a44ec454d6abe0d3908baa)

# Extra mile

Added to the CI the code coverage report
