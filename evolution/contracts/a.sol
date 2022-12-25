// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract a {
  uint public favoriteNumber = 12;

  function getFavoriteNumber() external view returns(uint) {
    return favoriteNumber;
  }

  function getFavoriteNumber2() external pure returns(uint) {
    return 11;
  }
}