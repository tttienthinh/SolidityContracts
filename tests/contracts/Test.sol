// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract Test {
    uint256 favoriteNumber;

    function getFavoriteNumber() external view returns (uint256) {
        return favoriteNumber;
    }
    function setFavoriteNumber(uint256 _favoriteNumber) external {
        favoriteNumber = _favoriteNumber;
    }

	function addition(uint256 _x) external pure returns (uint256) {
		return _x + 5;
	}
	function multiplication(uint256 _x, uint256 _y) external pure returns (uint256) {
		return _x*_y;
	}

	
}
