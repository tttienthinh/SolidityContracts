// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract FavoriteAddress {
  address favoriteAddress;
  function getFavoriteAddress() external view returns(address) {
    return favoriteAddress;
  }

  function setFavoriteAddress(address _favoriteAddress) external {
    favoriteAddress = _favoriteAddress;
  }
}
