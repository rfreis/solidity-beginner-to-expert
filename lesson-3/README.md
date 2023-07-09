# Lesson 3 - Storage Factory

This quicker lesson extends the Lesson's 2 SimpleStorage contract to teach us few important things like:

- Importing contracts from other files
- Interacting with other contracts
- Contract inheritance
- Overriding functions

The original repository for this class can be found [here](https://github.com/cyfrin/remix-storage-factory-f23)

My personal on chain development

- Factory contract deployed on Sepolia
[0x0CA9249B341aeef7De960863EBf318ECF39428FD](https://sepolia.etherscan.io/address/0x0ca9249b341aeef7de960863ebf318ecf39428fd)
    - Transaction [0xed8b62d31ede7a2faf6aec0c631a49025965a02a932d9aa0598f858136f3c34d](https://sepolia.etherscan.io/tx/0xed8b62d31ede7a2faf6aec0c631a49025965a02a932d9aa0598f858136f3c34d)
- Add contract from Lesson 2 to the Storage Factory contract list
    - Transaction [0x611924a557df15807a1613de84e9f36fbdd9d263737de22eaac9a32688187b9d](https://sepolia.etherscan.io/tx/0x611924a557df15807a1613de84e9f36fbdd9d263737de22eaac9a32688187b9d)
- Update contract favorite number
    - Transaction [0xa69455ad260c2633db6e0919463db21cede4c5210a49ae35feae9f70d472f696](https://sepolia.etherscan.io/tx/0xa69455ad260c2633db6e0919463db21cede4c5210a49ae35feae9f70d472f696)
- Create a new SimpleStorage contract using the StorageFactory
    - Transaction [0x15deb57db378a28244d6ca013c88bd730733c8610f4011d52f39c0f12f95c47d](https://sepolia.etherscan.io/tx/0x15deb57db378a28244d6ca013c88bd730733c8610f4011d52f39c0f12f95c47d)

## Contract summary

- StorageFactory
    - [0x0CA9249B341aeef7De960863EBf318ECF39428FD](https://sepolia.etherscan.io/address/0x0ca9249b341aeef7de960863ebf318ecf39428fd)
- SimpleStorage
    - Lesson 2 contract [0x62c338BD5aC1CedfC6e7b5A2287443F0e1817931](https://sepolia.etherscan.io/address/0x62c338bd5ac1cedfc6e7b5a2287443f0e1817931)
    - Lesson 3 new contract [0xE35D087CD6F5f91507efA19570d147be920C3972](https://sepolia.etherscan.io/address/0xe35d087cd6f5f91507efa19570d147be920c3972)

# Extra mile

For this class, I thought would be a good idea to expand the lessons learned to add the pre existing contract created on Lesson 2 by address as an additional function. Adding it to the StorageFactory feature to handle new deployed contracts as well as the previously existing ones.
