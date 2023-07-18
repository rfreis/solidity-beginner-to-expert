// SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;

import {AggregatorV3Interface} from "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

library PriceConverter {
    function getPrice() internal view returns(uint256) {
        // Address list available on https://docs.chain.link/data-feeds/price-feeds/addresses
        // feed address for BTC/USD on Sepolia: 0x1b44F3514812d835EB1BDB0acB33d3fA3351Ee43
        // ABI
        AggregatorV3Interface priceFeed = AggregatorV3Interface(
            0x1b44F3514812d835EB1BDB0acB33d3fA3351Ee43
        );
        (,int256 price,,,) = priceFeed.latestRoundData();
        return uint256(price * 1e10); // price comes with 8 decimal places
    }

    function getConversionRate(uint256 ethAmount) internal view returns(uint256) {
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1e18;
        return ethAmountInUsd;
    }

    function getVersion() internal view returns(uint256) {
        return AggregatorV3Interface(0x1b44F3514812d835EB1BDB0acB33d3fA3351Ee43).version();
    }
}
