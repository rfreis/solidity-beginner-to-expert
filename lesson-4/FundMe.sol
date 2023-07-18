// SPDX-License-Identifier: MIT
pragma solidity >=0.8.18 <0.9.0;

import {PriceConverter} from "./PriceConverter.sol";

error NotOwner();

contract FundMe {
    using PriceConverter for uint256;
    uint256 public constant MINIMUM_USD = 5e18;
    address[] public funders;
    mapping(address funder => uint256 amountFunded) public addressToAmountFunded;
    address public immutable i_owner;

    constructor() {
        i_owner = msg.sender;
    }

    receive() external payable {
        fund();
    }

    fallback() external payable {
        fund();
    }

    function fund() public payable {
        // require(msg.value > 1 ether, "didn't send enough ETH");
        require(msg.value.getConversionRate() > MINIMUM_USD, "didn't send enough ETH");
        funders.push(msg.sender);
        addressToAmountFunded[msg.sender] += msg.value;
    }

    function withdrawal() public onlyOwner {
        for(uint256 funderIndex = 0; funderIndex < funders.length; funderIndex++) {
            address funder = funders[funderIndex];
            addressToAmountFunded[funder] = 0;
        }
        funders = new address[](0);
        /*
        Reference: https://solidity-by-example.org/sending-ether/
        // transfer - fails if spends more than 2300 gas
        payable(msg.sender).transfer(address(this).balance);
        // send - returns bool
        bool sendSuccess = payable(msg.sender).send(address(this).balance);
        require(sendSuccess, "Send failed");
        */
        // call - recommended
        // (bool callSuccess, bytes memory dataReturned) = payable(msg.sender).call{value: address(this).balance}("");
        (bool callSuccess,) = payable(msg.sender).call{value: address(this).balance}("");
        require(callSuccess, "Call failed");
    }

    modifier onlyOwner() {
        // require(msg.sender == i_owner, "Must be owner!");
        if (msg.sender != i_owner) { // gas efficient
            revert NotOwner();
        }
        _;
    }
}
