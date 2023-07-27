// SPDX-License-Identifier: MIT
pragma solidity >=0.8.18 <0.9.0;

contract SimpleStorage {
    uint256 public myFavoriteNumber;

    struct Person {
        uint256 favoriteNumber;
        string name;
    }

    Person public favoritePerson;
    // Person[2] would be a static array with length of 2
    Person[] public listOfPeople;

    mapping(string => uint256) public nameToFavoriteNumber;

    function storeFavoriteNumber(uint256 _favoriteNumber) public {
        myFavoriteNumber = _favoriteNumber;
    }

    function storeFavoritePerson(
        string memory name,
        uint256 _favoriteNumber
    ) public {
        Person memory newPerson = Person({
            favoriteNumber: _favoriteNumber,
            name: name
        });
        favoritePerson = newPerson;
    }

    function retrieve() public view returns (uint256) {
        return myFavoriteNumber;
    }

    function addPerson(string memory name, uint256 _favoriteNumber) public {
        Person memory newPerson = Person({
            favoriteNumber: _favoriteNumber,
            name: name
        });
        listOfPeople.push(newPerson);
        nameToFavoriteNumber[name] = _favoriteNumber;
    }
}
