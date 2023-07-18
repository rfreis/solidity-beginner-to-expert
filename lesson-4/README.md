# Lesson 4 - Fund me

This lesson teaches us how to deal with payable functions to receive ETH on a contract. Important topics from this lessons are:

- modifiers
- global keywords
- payable functions
- using oracles (Chainlink) to get on chain data like the ETH/USD rate from data feeds
- special functions `receive` and `fallback`
- couple examples of gas optimization with:
    - `constant` and `immutable` variables
    - withdrawal methods: `transfer`, `send` and `call`
    - conditional errors vs `require` and `revert`

The original repository for this class can be found [here](https://github.com/Cyfrin/remix-fund-me-f23)

## My personal on chain development

- Fund Me contract deployed on Sepolia
[0x20651C04f845C6673cE2e9756E27043d78cD1AE8](https://sepolia.etherscan.io/address/0x20651C04f845C6673cE2e9756E27043d78cD1AE8)
    - Transaction [0x4fe89be4d49a729ad6899f9ff5c1fd8503093dfb7113426efd226acf3b0d9faf](https://sepolia.etherscan.io/tx/0x4fe89be4d49a729ad6899f9ff5c1fd8503093dfb7113426efd226acf3b0d9faf)
- Failed TX due to not enough ETH (< 5 USD)
    - Transaction [0xb94b9bf42e5ecc65e45f8d3a41bcd41e489c1fe925da21d81cc8c9c3ed838894](https://sepolia.etherscan.io/tx/0xb94b9bf42e5ecc65e45f8d3a41bcd41e489c1fe925da21d81cc8c9c3ed838894)
- Successful TX with enough ETH (>= 5 USD)
    - Transaction [0x0f15bd9eb1e77ba3a3347efff61c255245074dd72445757ad1ef95e003dab928](https://sepolia.etherscan.io/tx/0x0f15bd9eb1e77ba3a3347efff61c255245074dd72445757ad1ef95e003dab928)
- Withdrawal TX
    - Transaction [0xb6e43c16a59d872b0e4dce74d7fa1781e7a7755d3423d67c16f30c01cf9c3611](https://sepolia.etherscan.io/tx/0xb6e43c16a59d872b0e4dce74d7fa1781e7a7755d3423d67c16f30c01cf9c3611)


# Extra mile

Instead of using Remix to deploy contracts with Metamask following the lesson's instructions, I decided to go all the way through to blockchain using python snippets
