// SPDX-License-Identifier: MIT
pragma solidity >=0.8.18 <0.9.0;

import { SimpleStorage } from "./SimpleStorage.sol";

contract StorageFactory {
    SimpleStorage[] public listofSimpleStorageContracts;

    function createSimpleStorageContract() public {
        SimpleStorage newSimpleStorageContract = new SimpleStorage();
        listofSimpleStorageContracts.push(newSimpleStorageContract);
    }

    function addExistingSimpleStorageContract(address _contractAddress) public {
        SimpleStorage _simpleStorageFromAddress = SimpleStorage(_contractAddress);
        listofSimpleStorageContracts.push(_simpleStorageFromAddress);
    }

    function sfStore(uint256 _simpleStorageIndex, uint256 _newSimpleStorageFavoriteNumber) public {
        SimpleStorage mySimpleStorage = listofSimpleStorageContracts[_simpleStorageIndex];
        mySimpleStorage.storeFavoriteNumber(_newSimpleStorageFavoriteNumber);
    }

    function sfGet(uint256 _simpleStorageIndex) public view returns(uint256) {
        SimpleStorage mySimpleStorage = listofSimpleStorageContracts[_simpleStorageIndex];
        return mySimpleStorage.retrieve();
    }
}
