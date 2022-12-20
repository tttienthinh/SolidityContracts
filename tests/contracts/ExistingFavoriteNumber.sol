// SPDX-License-Identifier: MIT
// https://medium.com/@blockchain101/calling-the-function-of-another-contract-in-solidity-f9edfa921f4c
pragma solidity >=0.4.22 <0.9.0;

contract FavoriteNumber {
    
    function getFavoriteNumber() external view returns(uint) {}
    
    function setFavoriteNumber(uint _favoriteNumber) external {}
    
}

contract ExistingFavoriteNumber  {
    
    FavoriteNumber dc;
    
    function existing(address _t) public {
        dc = FavoriteNumber(_t);
    }
 
    function getA() public view returns (uint result) {
        return dc.getFavoriteNumber();
    }
    
    function setA(uint _val) public {
        dc.setFavoriteNumber(_val);
    }
    
}