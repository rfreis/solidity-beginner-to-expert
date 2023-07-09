// SPDX-License-Identifier: MIT
pragma solidity >=0.8.18 <0.9.0;

import { SimpleStorage } from "./SimpleStorage.sol";

contract AddFiveStorage is SimpleStorage {
    function storeFavoriteNumber(uint256 _favoriteNumber) public override {
        myFavoriteNumber = _favoriteNumber + 5;
    }
}
